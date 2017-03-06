# model.py

from sklearn.naive_bayes import GaussianNB
from domain_model import *
from data import Data

# TODO: Implement these models to complete ensemble classifier
class TitleModel:
    def __init__(self):
        pass
class ContentModel:
    def __init__(self):
        pass

# TODO: Implement this blacklisting model against toxic users
class BlacklistModel:
    def __init__(self):
        pass

class Model:
    """
    [In Progress]
    Ensemble model using classifiers on article title, content, and URL
    """

    # ML models
    d_model = DomainModel()
    #t_model = TitleModel()

    # Data locations
    data_dir = "res/data/"
    data_interface = Data(data_dir)

    def __init__(self):
        # Do initial training
        self.train();

    def add_data(self, title, y, url, domain):
        """ Takes Facebook data and adds to model """

        # TODO: Train title and domain model
        #title_model

        # Append data to fb_data_loc file
        with open(self.fb_data_loc, "a") as f:
            y = y[0].upper() + y[1:] # Make upper
            line = ",," + y + "," + title + "," + domain + "," + url + "," + "\n"
            f.write(line)


    def classify(self, title, url, domain):
        """ Classify given Facebook post """

        # TODO: Classify using title and domain model

        #title_model
        credibility = self.d_model.classify(url)

        return credibility

    def test(self):
        """
        Test model using 75/25 holdout method on training data, ensuring a
        very close distribution between both the training and testing sets
        """

        # Scramble the training data around

        # Split the data 75/25

        # Train on the 75

        # Test on the 25
        num_correct = 0
        num_wrong = 0
        accuracy = num_correct / (num_correct + num_wrong)

        # Return accuracy
        return accuracy

    def train(self):
        """ Retrain on all stored examples in base and Facebook data """

        self.d_model.train(self.data_interface)

        pass
