"""
Sequencing is the process of finding the primary structure whether it is DNA, RNA.

Four bases: adenine (A), guanine (G), cytosine (C) and thymine (T)

DNA sequencing is the method of determining the order of nucleotide in a DNA.
RNA sequencing is the method to find the quantity of RNA in a biological sample.
Protein sequencing is the method of determining the amino acid sequence of all or part of a protein or peptide.

"""

from Bio import SeqIO  # biopython

# Example dataset used is: Cypripedioideae, a subfamily of orchids
# The code can be applied to other datasets


row = 0
for sequence in SeqIO.parse('data/orchid.fasta', 'fasta'):
    print('Sequence ID: ' + sequence.id)
    print('DNA Sequence: ' + sequence.seq)
    print('Number of nucleotides: {}'.format(len(sequence)) + '\n')
    row += 1

print('Total sequences in file: {}'.format(row))