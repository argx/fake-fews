# test_model.py

from model import *

class TestModel:

    def __init__(self):
        self.model = Model(testing = True)

    def test(self, fold_num):
        self.model.test(fold_num)

def main():

    fold_num = 4

    test_model = TestModel()
    test_model.test(fold_num)

main()
