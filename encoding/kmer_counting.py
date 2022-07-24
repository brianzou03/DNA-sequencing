import Bio
import numpy as np
import re
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
import matplotlib.pyplot as plt
from main import return_genomic_sequence

from encoding import *


def kmers_function(seq, size):
    return [seq[x:x + size].lower() for x in range(len(seq) - size + 1)]


mySeq = return_genomic_sequence()

print(kmers_function(mySeq, size=7))  # produces sequences of kmer "words"

# we can then join the kmer words into sentences
# letters ^ length = possible words .. e.g. 5 ^ 5 = 3125 possible words


words = kmers_function(mySeq, size=6)
joined_sentence = ' '.join(words)
print(joined_sentence)

mySeq1 = 'TCTCACACATGTGCCAATCACTGTCACCC'
mySeq2 = 'GTGCCCAGGTTCAGTGAGTGACACAGGCAG'
sentence1 = ' '.join(kmers_function(mySeq1, size=6))
sentence2 = ' '.join(kmers_function(mySeq2, size=6))

# creating the bag of words model
cv = CountVectorizer()
X = cv.fit_transform([joined_sentence, sentence1, sentence2]).toarray()
