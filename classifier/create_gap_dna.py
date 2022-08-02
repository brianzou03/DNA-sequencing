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
                        new_elem += 'n'  # replace the randomly selected letter with n
                word_list.append(new_elem)
        except IndexError:  # when reaching the end of a temp array
            continue

    # list of word
    # random.shuffle(word_list)  # randomizes list order
    return word_list


def insert_random():
    import random
    counter = 0
    min_no_space = 0
    max_no_space = 6  # if max sequence length without space
    no_space = 0
    with open('../data/text_data/human_data.txt', 'r') as f, open('../data/text_data/gap_human_dna.txt', 'w') as w:
        for line in f:
            for c in line:
                if c.isalpha() and counter > 1:  # ensure that we are only altering the dna
                    if no_space > min_no_space:
                        if random.randint(1, 6) == 1 or no_space >= max_no_space:

                            w.write("n")
                            no_space = 0
                    else:
                        no_space += 1
                        w.write(c)
                else:
                    w.write(c)
            counter += 1


insert_random()

