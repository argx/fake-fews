# domain_model.py

from naiveBayesClassifier import tokenizer
from naiveBayesClassifier.trainer import Trainer
from naiveBayesClassifier.classifier import Classifier
import csv
import nltk
from nltk.corpus import stopwords
from data import Data

class DomainModel:

    data_interface = []
    newsTrainer = Trainer(tokenizer.Tokenizer(stop_words = [], signs_to_remove = ["?!#%&"]))
    newClassifier = None

    def __init__(self, data_interface):
        """
        Constructor:
        Store data interface on creation,
        Don't train yet, let parent decide when
        """

        if not isinstance(data_interface, Data):
            raise ValueError("Data is not properly interfaced through class Data")

        self.data_interface = data_interface

    def train(self):
        """Train on base and FB data"""

        # Run through each training example in data interface and
        # feed them into model
        for data_point in self.data_interface:
            data_class = data_point[2].strip()  # Class is "Credibility"
            data_text = data_point[4].strip()   # Text is "Content URL"
            self.newsTrainer.train(data_text, data_class)

        self.newsClassifier = Classifier(self.newsTrainer.data, \
            tokenizer.Tokenizer(stop_words = [], signs_to_remove = ["?!#%&"]))

    def classify(self, unknownInstance):
        classification = self.newsClassifier.classify(unknownInstance)
        return classification
