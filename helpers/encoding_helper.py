import numpy as np
import re


def string_to_array(seq_string):
    seq_string = seq_string.lower()  # removes capitalization discrepancies
    seq_string = re.sub('[^acgt]', 'n', seq_string)
    seq_string = np.array(list(seq_string))
    return seq_string
