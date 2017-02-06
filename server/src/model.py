from sklearn.naive_bayes import GaussianNB
from domain_model import *

# Comes from Giridhar
class TitleModel:
    def __init__(self):
        pass

class Model:

    #t_model = TitleModel()
    d_model = DomainModel()

    # Data locations
    data_dir = "res/data/"
    base_data_loc = data_dir + "base_data.csv" 
    fb_data_loc = data_dir + "fb_data.csv" 

    def __init__(self):
        # Do initial training
        self.train();
   
    def add_data(self, title, y, url, domain):
        """Takes Facebook data and adds to model"""

        # TODO: Train title and domain model
        #title_model

        # Append data to fb_data_loc file
        with open(self.fb_data_loc, "a") as f:
            y = y[0].upper() + y[1:] # Make upper
            line = ",," + y + "," + title + "," + domain + "," + url + "," + "\n"
            f.write(line)
        

    def classify(self, title, url, domain):
        """Classify given Facebook post"""

        # TODO: Classify using title and domain model

        #title_model
        credibility = self.d_model.classify(url)

        return credibility 

    def train(self):
        """Retrain on all stored examples in base and Facebook data"""

        # TODO: Train title and domain model with local data

        pass
