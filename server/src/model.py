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

    # Models
    d_model = DomainModel()
    #t_model = TitleModel()
    test_holdout = 0.25 # Portion of data to use for testing

    # Data
    data_dir = "res/data/"
    data_interface = Data(data_dir)

    def __init__(self):
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

    def test(self):
        """
        Test model using 75/25 holdout method on training data, ensuring a
        very close distribution between both the training and testing sets
        """

        #test_holdout

        # Split the data based on holdout percentage

        # Train

        # Test
        num_correct = 0
        num_wrong = 0
        # TODO: Test
        accuracy = num_correct / (num_correct + num_wrong)

        # Return accuracy
        return accuracy

    def train(self):
        """ Retrain on all stored examples in base and Facebook data """

        self.d_model.train(self.data_interface)
