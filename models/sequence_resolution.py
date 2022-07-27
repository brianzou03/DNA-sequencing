from Bio import SeqIO
import pandas as pd
from helpers.encoding_helper import string_to_array

test_sequence = 'ATCNAACGTACGTANATCG'  # resolving the unknown bases N

new_sequence = string_to_array(test_sequence)  # convert sequence to array separate chars in lowercase

print(new_sequence)

# Prerequisite: You are given a strand with gaps, represented by unknown base N
# Model Idea: Train model on human DNA sequence without gaps
# Given a sequence, predict A/T/C/G chance after training
# Original is 0.25% by random chance, but after training should be much higher

# human_dna = pd.read_table('../fasta_data/GRCh38_genomic_test.fna')

with open('../data/fasta_data/GRCh38_genomic_test.fna') as fasta_file:  # this will close handle cleanly
    identifiers = []
    lengths = []
    for seq_record in SeqIO.parse(fasta_file, 'fasta'):
        identifiers.append(seq_record.id)  # Sequence: NC_000001.11
        lengths.append(len(seq_record.seq))  # length of sequence ..
        print('DNA Sequence: ' + str(seq_record.seq))


