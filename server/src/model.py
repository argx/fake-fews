# model.py

from sklearn.naive_bayes import GaussianNB
from domain_model import *
from data import Data
import math

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

    # Data
    data_dir = "res/data/"

    def __init__(self, data_interface = None):

        # Grab data
        if data_interface is None:
            self.data_interface = Data(self.data_dir)
        else: self.data_interface = data_interface

        # Models
        self.d_model = DomainModel(self.data_interface)

        # Do initial training
        self.train();

    def add_data(self, title, y, url, domain, user_id):
        """ Takes Facebook data and adds to model """

        # Store Facebook data
        data_type = "Article"
        y = y[0].upper() + y[1:] # Make uppercase
        line = data_type + ",," + y + "," + title + "," + \
            domain + "," + url + "," + ("#" + user_id)  + "\n"

        data_interface.store(line)

    def classify(self, title, url, domain):
        """ Classify given Facebook post using certain fields """

        credibility = self.d_model.classify(url)
        return credibility

    def train(self):
        """ Retrain on all stored examples in base and Facebook data """

        self.d_model.train()
