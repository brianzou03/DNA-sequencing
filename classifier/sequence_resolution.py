from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score
import joblib
from sequence_preprocessing import *

# This is the file where the model is fitted and trained

human_dna = pd.read_table('../data/text_data/human_data.txt')
gap_human_dna = pd.read_table('../data/text_data/gap_human_dna.txt')

count_vectorizer = CountVectorizer(ngram_range=(4, 4))

# fit the model
x_human = count_vectorizer.fit_transform(human_conversion(human_dna)[0])  # replace with 1 1 if doesnt work
y_human = count_vectorizer.fit_transform(human_conversion(gap_human_dna)[0])

x_train, x_test, y_train, y_test = train_test_split(x_human, y_human,
                                                    test_size=0.20, random_state=42)

# Multinomial Naive Bayes classifier
classifier = MultinomialNB(alpha=0.1)
# classifier.fit(x_train, y_train)  # training the model

