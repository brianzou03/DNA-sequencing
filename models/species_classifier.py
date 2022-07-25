import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# Creating a classifier model to differentiate DNA type

# TODO: convert human, chimp, and dog_data.txt to FASTA format (beware pandas cant read fasta)
# https://stackoverflow.com/questions/19436789/biopython-seqio-to-pandas-dataframe


human_dna = pd.read_table('../text_data/human_data.txt')
human_dna.head()