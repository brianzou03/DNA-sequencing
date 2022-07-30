import pandas as pd
import random


human_dna = pd.read_table('../data/text_data/human_data.txt')


def kmers_function(seq, size=6):  # all k-mers converted to lowercase and size 6
    return [seq[x:x + size].lower() for x in range(len(seq) - size + 1)]


# Create gaps in DNA by inserting n base randomly into the 6-letter k-mer words
def human_conversion(dataset):
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
    random.shuffle(word_list)  # randomizes list order
    return word_list


f = open('../data/text_data/gap_human_dna.txt', 'w')  # Note: have to remove config every time re-creating the file

for elem in human_conversion(human_dna):  # outputs all the k-mer results
    f.write(elem + ' ')

f.close()


