import numpy as np
from sklearn.preprocessing import OneHotEncoder
from helpers.encoding_helper import string_to_array, return_genomic_sequence
from encoders.ordinal import label_encoder


def one_hot_encoder(seq_string):  # transforms ACTG to [0,0,0,1], [0,0,1,0], [0,1,0,0], or [1,0,0,0]
    int_encoded = label_encoder.transform(seq_string)
    onehot_encoder = OneHotEncoder(sparse=False, dtype=int)
    int_encoded = int_encoded.reshape(len(int_encoded), 1)
    onehot_encoded = onehot_encoder.fit_transform(int_encoded)
    onehot_encoded = np.delete(onehot_encoded, -1, 1)
    return onehot_encoded  # returns a 2d matrix


# print(one_hot_encoder(string_to_array(seq_test)))
print(one_hot_encoder(string_to_array(return_genomic_sequence())))
