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
x_human = count_vectorizer.fit_transform(human_conversion(human_dna)[0])
y_human = human_conversion(human_dna)[2]

gx_human = count_vectorizer.fit_transform(human_conversion(gap_human_dna)[0])

x_train, x_test, y_train, y_test = train_test_split(x_human, y_human, test_size=0.20, random_state=42)

# Multinomial Naive Bayes classifier
classifier = MultinomialNB(alpha=0.1)
classifier.fit(x_train, y_train)  # training the model


# Produces score based on results vs predictions
def get_metrics(y_test, y_predicted):  # takes the test result and the predicted result
    accuracy = accuracy_score(y_test, y_predicted)
    precision = precision_score(y_test, y_predicted, average='weighted')
    recall = recall_score(y_test, y_predicted, average='weighted')
    f1 = f1_score(y_test, y_predicted, average='weighted')
    return [accuracy, precision, recall, f1]


# Predicting the gaps in the sequence
def predict_human():
    print("\nConfusion matrix for predictions on human DNA sequence without gaps\n")

    y_prediction_human = classifier.predict(human_conversion(gap_human_dna)[0])  # or try gx_human

    # Output accuracy matrix for human DNA with gaps
    print(pd.crosstab(pd.Series(y_test, name='Actual'), pd.Series(y_prediction_human, name='Predicted')))

    accuracy = get_metrics(y_test, y_prediction_human)[0]
    precision = get_metrics(y_test, y_prediction_human)[1]
    recall = get_metrics(y_test, y_prediction_human)[2]
    f1 = get_metrics(y_test, y_prediction_human)[3]

    # Accuracy matrix for Human DNA
    print("accuracy = %.3f \nprecision = %.3f \nrecall = %.3f \nf1 = %.3f" % (accuracy, precision, recall, f1))


predict_human()

