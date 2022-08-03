import pandas as pd
import random

from classifier.sequence_preprocessing import kmers_function

human_dna = pd.read_table('../data/text_data/human_data.txt')


# Create gaps in DNA by inserting n base randomly into the 6-letter k-mer words (but it makes separate words)
def insert_n(dataset):
    dataset['words'] = dataset.apply(lambda x: kmers_function(x['sequence']), axis=1)
    dataset = dataset.drop('sequence', axis=1)
    human_texts = list(dataset['words'])
    word_list = []

    for item in range(len(human_texts)):
        human_texts[item] = ' '.join(human_texts[item])

    for item in human_texts:
        temp_arr = item.split(' ')
        try:
            for temp_elem in temp_arr:
                new_elem = ''
                random_num = random.randrange(0, 6, 1)
                for i in range(6):  # 3 nested for loops ... awful complexity
                    if i != random_num:
                        new_elem += temp_elem[i]
                    else:
                        new_elem += 'N'  # replace the randomly selected letter with n
                word_list.append(new_elem)
        except IndexError:  # when reaching the end of a temp array
            continue

    # list of word
    # random.shuffle(word_list)  # randomizes list order
    return word_list


def insert_random():
    with open('../data/text_data/human_data.txt', 'r') as f, open('../data/text_data/gap_human_dna.txt', 'w') as w:
        for line in f:
            for c in line:
                if c.isnumeric() or c == ' ' or c == c.lower():  # catches nums and spaces and lowercase
                    w.write(c)  # don't touch nums spaces and lowercases
                elif random.randint(1, 6) == 1:  # 1/6 chance randomly insert 'N'
                    w.write('N')
                else:
                    w.write(c)


insert_random()

