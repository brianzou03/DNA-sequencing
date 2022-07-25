import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

# Creating a classifier model to differentiate DNA type

# TODO: convert human, chimp, and dog_data.txt to FASTA format (beware pandas cant read fasta)
# https://stackoverflow.com/questions/19436789/biopython-seqio-to-pandas-dataframe


# Helper k-mer conversion function
def kmers_function(seq, size=6):  # all k-mers converted to lowercase and size 6
    return [seq[x:x + size].lower() for x in range(len(seq) - size + 1)]


# Converting human DNA into k-mer form to fit the model
def human_conversion(dataset, cv):
    # lambda applies kmers function to all rows within the specified dataset
    dataset['words'] = dataset.apply(lambda x: kmers_function(x['sequence']), axis=1)
    dataset = dataset.drop('sequence', axis=1)  # remove the word sequence

    human_texts = list(dataset['words'])  # list of 'words' in the human DNA
    for item in range(len(human_texts)):
        human_texts[item] = ' '.join(human_texts[item])  # joining the words with space in between

    # separate x and y labels
    y_human = dataset.iloc[:, 0].values  # integer location indexing

    x_human = cv.fit_transform(human_texts)  # performs fit and transform on the input data

    return [x_human, y_human]  # returns a list, so access index for specific x or y


# Converting chimp DNA into k-mer form to fit the model
def chimp_conversion(dataset, cv):  # works the same as human_conversion
    dataset['words'] = dataset.apply(lambda x: kmers_function(x['sequence']), axis=1)
    dataset = dataset.drop('sequence', axis=1)

    chimp_texts = list(dataset['words'])
    for item in range(len(chimp_texts)):
        chimp_texts[item] = ' '.join(chimp_texts[item])

    y_chimp = dataset.iloc[:, 0].values

    x_chimp = cv.transform(chimp_texts)

    return [x_chimp, y_chimp]


# Converting dog DNA into k-mer form to fit the model
def dog_conversion(dataset, cv):  # works the same as human_conversion
    dataset['words'] = dataset.apply(lambda x: kmers_function(x['sequence']), axis=1)
    dataset = dataset.drop('sequence', axis=1)

    dog_texts = list(dataset['words'])
    for item in range(len(dog_texts)):
        dog_texts[item] = ' '.join(dog_texts[item])

    y_dog = dataset.iloc[:, 0].values

    x_dog = cv.transform(dog_texts)

    return [x_dog, y_dog]


human_dna = pd.read_table('../text_data/human_data.txt')
chimp_dna = pd.read_table('../text_data/chimp_data.txt')
dog_dna = pd.read_table('../text_data/dog_data.txt')


count_vectorizer = CountVectorizer(ngram_range=(4, 4))

# Method return index 0 = x, 1 = y
print(human_conversion(human_dna, count_vectorizer)[0].shape)  # (4380, 23214) -> genes of uniform length
print(chimp_conversion(chimp_dna, count_vectorizer)[0].shape)
print(dog_conversion(dog_dna, count_vectorizer)[0].shape)

