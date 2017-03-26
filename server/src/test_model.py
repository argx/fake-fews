#!/bin/bash
# test_model.py

from model import *

class TestModel:
    def __init__(self):
        pass

    def find_accuracy(self, training_data, test_data):
        train_fold_interface = Data(data_list = training_data)
        test_fold_interface = Data(data_list = test_data)

        fold_model = Model(data_interface = train_fold_interface)

        correct_predictions = 0
        wrong_predictions = 0
        for test_instance in test_fold_interface.arr:
                title = test_instance[3]
                url = test_instance[4]
                actual_credibility = test_instance[2]
                instance_prediction = fold_model.classify(title, url, url)
                if (instance_prediction == actual_credibility):
                    correct_predictions += 1
                else: wrong_predictions += 1

        return correct_predictions/len(test_fold_interface.arr)


    def test(self, fold_num):
        """
        Test model using variable holdout method on training data, ensuring a
        very close distribution between both the training and testing sets
        """

        # TODO: Look at running a FRESH classifier in the background
        # TODO: Integrate with testModel API call
        # TODO: Run different training/testing configs for folds
        # TODO: Ensure uniform distribution of fake-to-real news in folds

        # Split the data based on holdout percentage
        main_data = Data(data_dir = "res/data/")
        data_arr = main_data.arr

        # Train
        # Splitup data into folds
        data_len = len(main_data.arr)
        fold_len = math.floor(data_len / fold_num)
        fold_list = [[] for i in range(fold_num)]
        for i in range(0, data_len):
            fold_list[i % fold_num].append(data_arr[i])

        test_fold = fold_list[-1]
        train_folds = fold_list[:-1]
        training_data = list()
        for train_fold in train_folds:
            training_data += train_fold

        current_fold_accuracy = self.find_accuracy(training_data, test_fold)
        print("Accuracy (k = {}, L = {}) = {}".format(fold_num, data_len, \
            current_fold_accuracy))

        print("Fold lengths", [len(x) for x in fold_list])

def main():
    fold_num = 5
    test_model = TestModel()
    test_model.test(fold_num)

main()
