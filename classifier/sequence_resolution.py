from Bio import SeqIO
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn import datasets
import numpy as np
import difflib

# TODO: publish to BioRxiv when completed

# You are given a strand with gaps, represented by unknown base N
# Model Idea: Train model on human DNA k-mer words...
# letters ^ length = possible words. 4 (ATCG) ^ 6 (len) = 4096 potential words
# Model then tries to predict what k-mer word the test_sequence is closest to matching
# When it figures out which 6 letter word the sequence matches, we then know our unknown base N

# TODO: replace with fasta data, need to figure out how to do with pandas
human_dna = pd.read_table('../data/text_data/human_data.txt')

count_vectorizer = CountVectorizer(ngram_range=(4, 4))


# Helper k-mer conversion function
def kmers_function(seq, size=6):  # all k-mers converted to lowercase and size 6
    return [seq[x:x + size].lower() for x in range(len(seq) - size + 1)]


# Converting human DNA into k-mer form to fit the model
def human_conversion(dataset, cv):
    # lambda applies kmers function to all rows within the specified dataset
    dataset['words'] = dataset.apply(lambda x: kmers_function(x['sequence']), axis=1)
    dataset = dataset.drop('sequence', axis=1)  # remove the 'sequence' label

    human_texts = list(dataset['words'])  # list of 'words' in the human DNA
    for item in range(len(human_texts)):
        human_texts[item] = ' '.join(human_texts[item])
        print(human_texts[item])

    # separate x and y labels
    y_human = dataset.iloc[:, 0].values  # select specific row/col in dataset
    x_human = cv.fit_transform(human_texts)  # performs fit and transform on the input data
    return [x_human, y_human, human_texts]  # returns a list, so access index for specific x or y


human_conversion(human_dna, count_vectorizer)  # this prints the 6 letter k-mer words

# Splitting the human dataset into the training set and test set
x_train, x_test, y_train, y_test = train_test_split(human_conversion(human_dna, count_vectorizer)[0],
                                                    human_conversion(human_dna, count_vectorizer)[1],
                                                    test_size=0.20, random_state=42)

# Look at classifier prediction and see if you can try inserting 6 letter k-mer and predict
# From there try predicting with a 6 letter k-mer with N gaps
# The list to parse through and match is human_texts... (use word similarity to match to a word in human_texts)


a = 'ATCGAA'
b = 'ATCGNA'

seq = difflib.SequenceMatcher(None, a, b)
d = seq.ratio() * 100
print(d)
# OUTPUT: 83.33 repeating

a = 'ATCGAA'
b = 'ATCGNN'

seq = difflib.SequenceMatcher(None, a, b)
d = seq.ratio() * 100
print(d)
# OUTPUT: 66.66 repeating
