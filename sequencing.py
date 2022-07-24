import Bio
import numpy as np
import re
from sklearn.preprocessing import LabelEncoder


# Approaching Sequencing Data:

# 1. Ordinal encoding DNA Sequence

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
    return float_encoded


seq_test = 'TTCAGCCAGTG'
print(ordinal_encoder(string_to_array(seq_test)))


# 2. One-hot encoding DNA Sequence



# 3. DNA sequence as a “language”, known as k-mer counting
