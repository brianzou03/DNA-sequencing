import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
from sklearn.naive_bayes import MultinomialNB
from sklearn import datasets
import numpy as np
import difflib

# TODO: publish to BioRxiv when completed
# TODO: replace with fasta data, need to figure out how to do with pandas
# TODO: Consider using seaborn, numpy for graph display in README
# TODO: Consider making sequence resolution into a library/package

human_dna = pd.read_table('../data/text_data/human_data.txt')


# Helper k-mer conversion function
def kmers_function(seq, size=6):  # all k-mers converted to lowercase and size 6
    return [seq[x:x + size].lower() for x in range(len(seq) - size + 1)]


# Converting human DNA into k-mer form to fit the model ... preprocessing
def human_conversion(dataset):
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

    # Index 0: unsplit lists of DNA, 1: list of DNA split into 6-letter k-mer sequences
    return [human_texts, word_list]


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

    for elem in target_list:  # add all the 6-letter words to new list in lowercase
        six_letter_list.append(elem.lower())

    current_max = 0  # current highest sequence seq_ratio
    current_max_seq = ''
    current_max_index = 0
    seq_match_dict = {}  # dictionary storing key (index of elem) : value (DNA strand sequence)
    base_count = []
    a_count, c_count, g_count, t_count = 0, 0, 0, 0

    # This function takes a while to load, so don't close out if it doesn't immediately output
    for index, elem in enumerate(six_letter_list):  # all k-mer results diff with test strand_b
        seq = difflib.SequenceMatcher(None, elem, match_strand)
        seq_ratio = seq.ratio() * 100

        if seq_ratio > current_max:  # setting new current max
            current_max = seq_ratio
            current_max_seq = elem
            current_max_index = index
        elif seq_ratio > 83:  # adds all 6-letter sequences that have 5 or more matching letters
            # TODO: Match by 5 letters that match at the same indexes
            index_match = 0
            missing_base = ''
            for iterator, char in enumerate(elem):  # this additional for loop increases time complexity by a lot
                if elem[iterator] == match_strand[iterator]:
                    index_match += 1
                else:
                    missing_base = elem[iterator]
            if index_match >= 5:  # match 5 or more letters in the right index to be added
                seq_match_dict[index] = elem
                # count missing bases, add to base_count
                if missing_base == 'a':
                    a_count += 1
                elif missing_base == 'c':
                    c_count += 1
                elif missing_base == 'g':
                    g_count += 1
                elif missing_base == 't':
                    t_count += 1

    # append a, c, t, g count to base count list
    max_base = 0
    max_base_char = ''
    base_count.append(a_count)
    if a_count > max_base:
        max_base_char = 'a'  # setting the max base character
    base_count.append(c_count)
    if c_count > max_base:
        max_base_char = 'c'
    base_count.append(g_count)
    if a_count > max_base:
        max_base_char = 'g'
    base_count.append(t_count)
    if a_count > max_base:
        max_base_char = 't'

    seq_match_dict[current_max_index] = current_max_seq  # add the max to dict

    # print(seq_match_dict)  # print sequence hashmap
    print('\n' + '|  A  |  C  |  T  |  G  |')
    print(''.join(str(base_count)))  # print basecount
    print('\n' + 'The base with the highest count is: ' + max_base_char)

    # Index 0: dict matching sequences to index, 1: list with acgt total count, 2: base which occurs the most
    return [seq_match_dict, base_count, max_base_char]


generate_matches(human_conversion(human_dna)[1], strand_b)

# Use the ACTG ratio to feed info to the ML model

# Note: downside is complexity. Each strand takes upwards of one minute. Limit test size to 10 strands initially?
# After teaching the model a few hundred strands, save to models/ folder
# Preprocessing takes in ACTN
# Preprocessing of each strand should generate the base which is most likely to be the missing base


# Two approaches:
# One) You train the model on the existing 6-letter k-mer strands (x)
#      You then try and predict the gapped strands (y)

# Two: You train the model with the gapped strands and the most likely fit (x)
#      You then try and predict other gapped strands based on similar occurrences (y)


"""
X is a matrix of the features values, each column being one feature, and being known values.
Each column of X is an independent variable.
y is a vector of the target values, being the values you want to try to predict.
y has only one column and is the dependant/target variable.
A row in X anf y is one data sample.
"""

# Try KNN (k-nearest neighbor model) vs Multinomial Naive Bayes

# count_vectorizer = CountVectorizer(ngram_range=(4, 4))
# Multinomial Naive Bayes classifier
# classifier = MultinomialNB(alpha=0.1)
# classifier.fit(x_train, y_train)  # Training the model with human DNA
