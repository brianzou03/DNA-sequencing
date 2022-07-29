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
# TODO: Consider using seaborn, numpy for graph display in README

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
    word_list = []  # stores the 6-letter words as individual elements

    for item in range(len(human_texts)):
        human_texts[item] = ' '.join(human_texts[item])

    for item in human_texts:  # iterate to create the 6-letter word list
        temp_arr = item.split(' ')
        for elem in temp_arr:
            word_list.append(elem)

    # separate x and y labels
    y_human = dataset.iloc[:, 0].values  # select specific row/col in dataset
    x_human = cv.fit_transform(human_texts)  # performs fit and transform on the input data
    return [x_human, y_human, human_texts, word_list]  # returns a list, so access index for specific x or y


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


strand_b = 'gcatgn'  # an example strand from the human dna txt
# new_strand_b = replace_n(strand_b, 'c')


# TODO: need to filter matches to in-order sequence matches because it still matches regardless of letter order
def generate_matches(target_list, match_strand):  # stores all matches with 5 or more letters in common

    six_letter_list = []
    diff_list = []

    for elem in target_list:  # add all the 6-letter words to new list in lowercase
        six_letter_list.append(elem.lower())

    current_max = 0  # current highest sequence seq_ratio
    current_max_seq = ''
    current_max_index = 0
    seq_match_dict = {}  # dictionary storing key (index of elem) : value (DNA strand sequence)

    # This function takes a while to load, so don't close out if it doesn't immediately output
    for index, elem in enumerate(six_letter_list):  # all k-mer results diff with test strand_b
        seq = difflib.SequenceMatcher(None, elem, match_strand)
        seq_ratio = seq.ratio() * 100
        diff_list.append(seq_ratio)

        if seq_ratio > current_max:  # setting new current max
            current_max = seq_ratio
            current_max_seq = elem
            current_max_index = index
        elif seq_ratio > 83:  # adds all 6-letter sequences that have 5 or more matching letters
            # TODO: Match by 5 letters that match at the same indexes
            index_match = 0
            for iterator, char in enumerate(elem):  # this additional for loop increases time complexity by a lot
                if elem[iterator] == match_strand[iterator]:
                    index_match += 1
            if index_match >= 5:  # match 5 or more letters in the right index to be added
                seq_match_dict[index] = elem
            # TODO: create list to store total A, T, C, G appearance in the matches
            # Use that ratio to feed info to the ML model

    seq_match_dict[current_max_index] = current_max_seq  # add the max

    print(seq_match_dict)

    return seq_match_dict


generate_matches(human_conversion(human_dna, count_vectorizer)[3], strand_b)

# Multinomial Naive Bayes classifier (MultinomialNB)
classifier = MultinomialNB(alpha=0.1)
classifier.fit(x_train, y_train)  # Training the model with human DNA
