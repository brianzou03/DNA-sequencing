from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
from sklearn.naive_bayes import MultinomialNB
from sklearn import datasets
import numpy as np
import pandas as pd
from sequence_preprocessing import *

# This is the file where the model is fitted and trained

human_dna = pd.read_table('../data/text_data/human_data.txt')


# After teaching the model a few hundred strands, save to models/ folder
# Preprocessing takes in ACTN
# Preprocessing of each strand should generate the base which is most likely to be the missing base
# TODO: parse gap_human_dna.txt


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
