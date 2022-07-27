import numpy as np
import re
from Bio import SeqIO


# Returning genomic sequence for use in encoders
def return_genomic_sequence():
    for sequence in SeqIO.parse('../data/fasta_data/GRCh38_genomic_test.fna', 'fasta'):
        return str(sequence.seq)


def string_to_array(seq_string):
    seq_string = seq_string.lower()  # removes capitalization discrepancies
    seq_string = re.sub('[^acgt]', 'n', seq_string)
    seq_string = np.array(list(seq_string))
    return seq_string
