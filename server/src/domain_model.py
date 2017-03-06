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

    def train(self):
        """Train on base and FB data"""

        with open('res/data/base_data.csv', 'r') as csv_file:

            reader = csv.reader(csv_file)
            i = 0
            for line in reader:

                    i += 1

                    line_split = line
                    read_dict = {}

                    if i == 1 or len(line_split) <= 2 or len(line_split[0]) == 0:
                        continue

                    read_dict['class'] = line_split[2].strip()
                    # Accounting for our inconsistency in Spreadsheet
                    if read_dict["class"] == "Real":
                        read_dict['text'] = line_split[6].strip()
                    else:
                        read_dict['text'] = line_split[5].strip()

                    print(read_dict)

                    self.training_data.append(read_dict)


        print('---->>>>>><<<<<<<-------')

        with open('res/data/fb_data.csv', 'r') as csv_file:

            reader = csv.reader(csv_file)
            i = 0
            for line in reader:

                    i += 1

                    line_split = line
                    read_dict = {}

                    if i == 1 or len(line_split) <= 2:
                        continue

                    read_dict['class'] = line_split[2].strip()
                    read_dict['text'] = line_split[5].strip()

                    print(read_dict)

                    self.training_data.append(read_dict)

        #print training_data
        for data in self.training_data:
            self.newsTrainer.train(data['text'], data['class'])

        self.newsClassifier = Classifier(self.newsTrainer.data, tokenizer.Tokenizer(stop_words = [], signs_to_remove = ["?!#%&"]))

    def classify(self, unknownInstance):
        classification = self.newsClassifier.classify(unknownInstance)
        return classification
