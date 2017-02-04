from sklearn.naive_bayes import GaussianNB

class Model():

    # Gaussian Naive Bayes is classifier
    gnb = GaussianNB()

    # Data locations
    data_dir = "../res/data/"
    base_data_loc = data_dir + "base_data.csv" 
    fb_data_loc = data_dir + "fb_data.csv" 

    def __init__(self):
        pass
   
    def fit(x, y):
        """Takes Facebook data and adds to model"""

        pass

    def classify(x):
        """Classify given Facebook post"""

        pass

    def train():
        """Retrain on all examples in base and Facebook data"""

        pass
