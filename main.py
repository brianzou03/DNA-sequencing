from Bio import SeqIO  # biopython
from Bio.SeqUtils import GC


# terminal: Squiggle data/GRCh38_latest_protein.faa --method=gates

# Produces general info about the sequence to terminal
def output_sequence_info():
    row = 0
    for sequence in SeqIO.parse('data/fasta_data/GRCh38_protein_test.faa', 'fasta'):
        print('Sequence ID: ' + str(sequence.id))
        print('DNA Sequence: ' + str(sequence.seq))
        print('Guanine-Cytosine Content: ' + str(GC(sequence.seq)))
        print('Number of nucleotides: {}'.format(len(sequence)) + '\n')  # DNA Sequencing
        row += 1

    print('Total sequences in file: {}'.format(row))


# Displays complement and reverse complement of the sequence to terminal
def dna_complement():
    row = 1
    for sequence in SeqIO.parse('data/fasta_data/GRCh38_genomic_test.fna', 'fasta'):
        print('Row ' + str(row))
        print('Original Sequence:  {} '.format(sequence.seq))
        print('Complement Sequence: {}: '.format(sequence.seq.complement()))
        print('Reverse Complement Sequence: {}: '.format(sequence.seq.reverse_complement()) + '\n')
        row += 1


output_sequence_info()
dna_complement()

