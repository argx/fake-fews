from naiveBayesClassifier import tokenizer
from naiveBayesClassifier.trainer import Trainer
from naiveBayesClassifier.classifier import Classifier
import csv
import nltk
from nltk.corpus import stopwords

class DomainModel:

    training_data = []
    newsTrainer = Trainer(tokenizer.Tokenizer(stop_words = [], signs_to_remove = ["?!#%&"]))
    newClassifier = None

    def __init__(self):
        self.train()

    # TODO: Train on FB data too
    def train(self):
        with open('src/URL.csv', 'r') as csv_file:
                reader = csv_file.readlines()
                for line in reader:
                        read_dict = {}
                        line_split = line.split(',')
                        if len(line_split) < 2 or len(line_split[0]) == 0:
                                continue
                        read_dict['text'] = line_split[0].strip()
                        read_dict['class'] = line_split[1].strip()
                        
                        self.training_data.append(read_dict)

        #print training_data
        for data in self.training_data:
            self.newsTrainer.train(data['text'], data['class'])

        self.newsClassifier = Classifier(self.newsTrainer.data, tokenizer.Tokenizer(stop_words = [], signs_to_remove = ["?!#%&"]))

    def classify(self, unknownInstance):
        classification = self.newsClassifier.classify(unknownInstance)
        return classification
