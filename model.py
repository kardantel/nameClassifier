import nltk
from utils import Utils

utils = Utils()


class NBC:
    '''
    Class that performs the prediction of male or female names by means of the
    Naive Bayes classifier.
    '''

    def __init__(self, data):
        self.data_augmented = data

        fset = [(utils.atributos7(n), g) for (n, g) in self.data_augmented]

        train, test = fset[500:], fset[:500]

        self.span_clf = nltk.NaiveBayesClassifier.train(train)

        print(f'Model Accuracy: {nltk.classify.accuracy(self.span_clf, test)}')

    def prediction(self, name):
        '''
        Make the prediction of female or male names.
        '''
        print()
        print(f'Name: {name}')
        print(f'Prediction: {self.span_clf.classify(utils.atributos7(name))}')
