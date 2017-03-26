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

    # Data
    data_dir = "res/data/"

    def __init__(self, testing = False):

        # Grab data
        self.data_interface = Data(data_dir)

        # Models
        self.d_model = DomainModel(data_interface)

        # Do initial training
        if not testing: self.train();

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

    def test(self, fold_num):
        """
        Test model using variable holdout method on training data, ensuring a
        very close distribution between both the training and testing sets
        """

        # TODO: Look at running a FRESH classifier in the background
        # TODO: Integrate with testModel API call

        # Split the data based on holdout percentage
        data_arr = self.data_interface.arr
        split_index = int(len(data_arr) * (1 - self.test_holdout))
        train_data = data_arr[:split_index]
        test_data = data_arr[split_index:]

        # Train
        # TODO

        # Test
        num_correct = 0
        num_wrong = 0
        accuracy = num_correct / (num_correct + num_wrong)
        # TODO

        # Return accuracy
        return accuracy

    def train(self):
        """ Retrain on all stored examples in base and Facebook data """

        self.d_model.train()
