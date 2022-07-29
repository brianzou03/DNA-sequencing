import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score
# from sklearn.externals import joblib
import joblib

# Creating a classifier model to differentiate DNA type by species

# TODO: convert human, chimp, and dog_data.txt to FASTA format (beware pandas cant read fasta)
# TODO: apply gap resolution to other species post-classification
# TODO Classify species -> resolve gaps in dna based on what species has been predicted
# https://stackoverflow.com/questions/19436789/biopython-seqio-to-pandas-dataframe

human_dna = pd.read_table('../data/text_data/human_data.txt')
chimp_dna = pd.read_table('../data/text_data/chimp_data.txt')
dog_dna = pd.read_table('../data/text_data/dog_data.txt')
# Transforms a given text into a vector on the basis of the frequency of each word that occurs in the text
count_vectorizer = CountVectorizer(ngram_range=(4, 4))


# Helper k-mer conversion function
def kmers_function(seq, size=6):  # all k-mers converted to lowercase and size 6
    return [seq[x:x + size].lower() for x in range(len(seq) - size + 1)]


# Converting human DNA into k-mer form to fit the model
def human_conversion(dataset, cv):
    # lambda applies kmers function to all rows within the specified dataset
    dataset['words'] = dataset.apply(lambda x: kmers_function(x['sequence']), axis=1)
    dataset = dataset.drop('sequence', axis=1)  # remove the 'sequence' label

    human_texts = list(dataset['words'])  # list of 'words' in the human DNA
    for item in range(len(human_texts)):
        human_texts[item] = ' '.join(human_texts[item])  # joining the words with space in between

    # separate x and y labels
    y_human = dataset.iloc[:, 0].values  # select specific row/col in dataset

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


# Splitting the human dataset into the training set and test set
x_train, x_test, y_train, y_test = train_test_split(human_conversion(human_dna, count_vectorizer)[0],
                                                    human_conversion(human_dna, count_vectorizer)[1],
                                                    test_size=0.20, random_state=42)

# Multinomial Naive Bayes classifier (MultinomialNB)
classifier = MultinomialNB(alpha=0.1)
classifier.fit(x_train, y_train)  # Training the model with human DNA using data and iloc


# Save the model to the model folder
def save_model(clf):  # takes in a classifier
    # Save trained model to model.sav
    filename = "models/species_model.sav"
    joblib.dump(clf, filename)  # pipeline, dir name

    classifier = joblib.load(filename)  # open the model and set classifier to the existing model


# Produces score based on results vs predictions
def get_metrics(y_test, y_predicted):  # takes the test result and the predicted result
    accuracy = accuracy_score(y_test, y_predicted)
    precision = precision_score(y_test, y_predicted, average='weighted')
    recall = recall_score(y_test, y_predicted, average='weighted')
    f1 = f1_score(y_test, y_predicted, average='weighted')
    return [accuracy, precision, recall, f1]


# Predicting the human sequence based on the classifier trained on 20% of the human DNA dataset
def predict_human():
    print("\nConfusion matrix for predictions on human test DNA sequence\n")

    y_prediction_human = classifier.predict(x_test)  # using classifier to predict human DNA (x_test)

    # Output accuracy matrix for human DNA
    print(pd.crosstab(pd.Series(y_test, name='Actual'), pd.Series(y_prediction_human, name='Predicted')))

    # Setting the performance values manually (otherwise, results in 0.96 flat a.p.r.f value)
    accuracy = get_metrics(y_test, y_prediction_human)[0]
    precision = get_metrics(y_test, y_prediction_human)[1]
    recall = get_metrics(y_test, y_prediction_human)[2]
    f1 = get_metrics(y_test, y_prediction_human)[3]

    # Accuracy matrix for Human DNA
    print("accuracy = %.3f \nprecision = %.3f \nrecall = %.3f \nf1 = %.3f" % (accuracy, precision, recall, f1))


# Predicting the chimp sequence based on trained classifier
def predict_chimp():
    print("\nConfusion matrix for predictions on Chimpanzee test DNA sequence\n")

    # Using classifier to predict chimp DNA
    y_prediction_chimp = classifier.predict(chimp_conversion(chimp_dna, count_vectorizer)[0])

    # Output accuracy matrix for chimp DNA
    print(pd.crosstab(pd.Series(chimp_conversion(chimp_dna, count_vectorizer)[1], name='Actual'),
                      pd.Series(y_prediction_chimp, name='Predicted')))

    # Setting the scores for the prediction values
    accuracy, precision, recall, f1 = \
        get_metrics(chimp_conversion(chimp_dna, count_vectorizer)[1], y_prediction_chimp)

    # Output prediction statistics
    print("accuracy = %.3f \nprecision = %.3f \nrecall = %.3f \nf1 = %.3f" % (accuracy, precision, recall, f1))


# Predicting the dog sequence based on the trained classifier
def predict_dog():
    print("\nConfusion matrix for predictions on Dog test DNA sequence\n")

    # Using classifier to predict dog DNA
    y_prediction_dog = classifier.predict(dog_conversion(dog_dna, count_vectorizer)[0])

    # Output accuracy matrix for dog DNA
    print(pd.crosstab(pd.Series(dog_conversion(dog_dna, count_vectorizer)[1], name='Actual'),
                      pd.Series(y_prediction_dog, name='Predicted')))

    # Setting the scores for the prediction values
    accuracy, precision, recall, f1 = get_metrics(dog_conversion(dog_dna, count_vectorizer)[1], y_prediction_dog)

    # Output prediction statistics
    print("accuracy = %.3f \nprecision = %.3f \nrecall = %.3f \nf1 = %.3f" % (accuracy, precision, recall, f1))


predict_human()
predict_chimp()
predict_dog()  # dog performance is worse than chimp because it is more divergent from human than chimp
