from helpers.encoding_helper import string_to_array, return_genomic_sequence
from sklearn.preprocessing import LabelEncoder
import numpy as np


label_encoder = LabelEncoder()  # create a label encoder with 'acgtn' alphabet
label_encoder.fit(np.array(['a', 'c', 'g', 't', 'z']))  # A=0.25, C=0.50, G=0.75, T=1.00, n=0.00.


def ordinal_encoder(input_array):
    integer_encoded = label_encoder.transform(input_array)
    float_encoded = integer_encoded.astype(float)
    float_encoded[float_encoded == 0] = 0.25  # A
    float_encoded[float_encoded == 1] = 0.50  # C
    float_encoded[float_encoded == 2] = 0.75  # G
    float_encoded[float_encoded == 3] = 1.00  # T
    float_encoded[float_encoded == 4] = 0.00  # anything else, lets say n
    return float_encoded  # returns numpy array


# seq_test = 'TTCAGCCAGTG'
# print(ordinal_encoder(string_to_array(seq_test)))
print(ordinal_encoder((string_to_array(return_genomic_sequence()))))  # terminal printing ... due to length
