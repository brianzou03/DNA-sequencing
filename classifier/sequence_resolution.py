from Bio import SeqIO
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn import datasets
import numpy as np
import difflib

# TODO: publish to BioRxiv when completed
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

    # separate x and y labels
    y_human = dataset.iloc[:, 0].values  # select specific row/col in dataset
    x_human = cv.fit_transform(human_texts)  # performs fit and transform on the input data
    return [x_human, y_human, human_texts]  # returns a list, so access index for specific x or y


x_train, x_test, y_train, y_test = train_test_split(human_conversion(human_dna, count_vectorizer)[0],
                                                    human_conversion(human_dna, count_vectorizer)[1],
                                                    test_size=0.20, random_state=42)


# Helper function to replace the N with A, T, C, or G
def replace_n(strand, base):
    new_strand = ''
    for letter in strand.lower():
        if letter == 'n':
            new_strand += base  # replace where N was with the guessed base
        else:
            new_strand += letter

    return new_strand


# Basically trying to guess if the N is an A, T, C, or G
# Train the model on human_texts that contains the 6-letter k-mer sequences

strand_a = 'atcgaa'
strand_b = 'atcgna'

seq = difflib.SequenceMatcher(None, strand_a, strand_b)
seq_ratio = seq.ratio() * 100
print(seq_ratio)
# Output: 83.33 repeating

new_strand_b = replace_n(strand_b, 'a')
print(new_strand_b)

seq = difflib.SequenceMatcher(None, strand_a, new_strand_b)
seq_ratio = seq.ratio() * 100
print(seq_ratio)
# Output: 100


for elem in human_conversion(human_dna, count_vectorizer)[2]:  # outputs all the k-mer results
    print(elem)

diff_list = []

for elem in human_conversion(human_dna, count_vectorizer)[2]:  # all k-mer results diff with test strand_b
    seq = difflib.SequenceMatcher(None, elem, strand_b)
    seq_ratio = seq.ratio() * 100
    diff_list.append(seq_ratio)
    print(seq_ratio)

diff_dictionary = {}  # hashmap that contains the values with highest similarity percentage and their index in diff_list

# Multinomial Naive Bayes classifier (MultinomialNB)
classifier = MultinomialNB(alpha=0.1)
classifier.fit(x_train, y_train)  # Training the model with human DNA

