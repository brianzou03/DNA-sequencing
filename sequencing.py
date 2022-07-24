import Bio
import numpy as np
import re
from sklearn.preprocessing import LabelEncoder, OneHotEncoder


# Approaching Sequencing Data:

# 1. Ordinal encoding DNA Sequence
# Nitrogen base is ordinal value

def string_to_array(seq_string):
    seq_string = seq_string.lower()  # removes capitalization discrepancies
    seq_string = re.sub('[^acgt]', 'n', seq_string)  # A=0.25, C=0.50, G=0.75, T=1.00, n=0.00.
    seq_string = np.array(list(seq_string))
    return seq_string


label_encoder = LabelEncoder()  # create a label encoder with 'acgtn' alphabet
label_encoder.fit(np.array(['a', 'c', 'g', 't', 'z']))


def ordinal_encoder(input_array):
    integer_encoded = label_encoder.transform(input_array)
    float_encoded = integer_encoded.astype(float)
    float_encoded[float_encoded == 0] = 0.25  # A
    float_encoded[float_encoded == 1] = 0.50  # C
    float_encoded[float_encoded == 2] = 0.75  # G
    float_encoded[float_encoded == 3] = 1.00  # T
    float_encoded[float_encoded == 4] = 0.00  # anything else, lets say n
    return float_encoded  # returns NumPy array


seq_test = 'TTCAGCCAGTG'
print(ordinal_encoder(string_to_array(seq_test)))


# 2. One-hot encoding DNA Sequence
# One-hot works well with CNN

def one_hot_encoder(seq_string):  # transforms ACTG to [0,0,0,1], [0,0,1,0], [0,1,0,0], or [1,0,0,0]
    int_encoded = label_encoder.transform(seq_string)
    onehot_encoder = OneHotEncoder(sparse=False, dtype=int)
    int_encoded = int_encoded.reshape(len(int_encoded), 1)
    onehot_encoded = onehot_encoder.fit_transform(int_encoded)
    onehot_encoded = np.delete(onehot_encoded, -1, 1)
    return onehot_encoded  # returns a 2d matrix


seq_test = 'GAATTCTCGAA'
print(one_hot_encoder(string_to_array(seq_test)))


# 3. DNA sequence as a “language”, known as k-mer counting
# The problem with 2 and 3 is that the results are not uniform length, necessary for classification and regression
# k-mer solves this with with NLP, breaking down sequences into words of a specific length

def kmers_function(seq, size):
    return [seq[x:x + size].lower() for x in range(len(seq) - size + 1)]


mySeq = 'GTGCCCAGGTTCAGTGAGTGACACAGGCAG'
print(kmers_function(mySeq, size=7))  # produces sequences of kmer "words"

# we can then join the kmer words into sentences
# letters ^ length = possible words .. e.g. 4 ^ 6 = 4096 possible words

words = kmers_function(mySeq, size=6)
joined_sentence = ' '.join(words)
print(joined_sentence)

mySeq1 = 'TCTCACACATGTGCCAATCACTGTCACCC'
mySeq2 = 'GTGCCCAGGTTCAGTGAGTGACACAGGCAG'
sentence1 = ' '.join(kmers_function(mySeq1, size=6))
sentence2 = ' '.join(kmers_function(mySeq2, size=6))

