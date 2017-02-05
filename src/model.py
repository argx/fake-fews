from sklearn.naive_bayes import GaussianNB

# Comes from Anand
class DomainModel:
    def __init__(self):
        pass

# Comes from Giridhar
class TitleModel:
    def __init__(self):
        pass

class Model:

    title_model = TitleModel()
    domain_model = DomainModel()

    # Data locations
    data_dir = "../res/data/"
    base_data_loc = data_dir + "base_data.csv" 
    fb_data_loc = data_dir + "fb_data.csv" 

    def __init__(self):
        # Do initial training
        self.train();
   
    def fit(self, x, y, url):
        """Takes Facebook data and adds to model"""

        # TODO: Train title and domain model
        # TODO: Append data to fb_data_loc file

        pass

    def classify(self, x):
        """Classify given Facebook post"""

        # TODO: Classify using title and domain model

        pass

    def train(self):
        """Retrain on all stored examples in base and Facebook data"""

        # TODO: Train title and domain model with local data

        pass
