# Takes test data and give it to model_knn to predict output using pre-trained ML model

# Importing required modules
import pickle
import pandas as pd
import datetime

from backtesting.model_knn import Model
from backtesting.fetch_stock_data import FetchData

# file path of saved pre-trained ML model 
MODEL_PATH = 'model.pkl'

# Function   :- takes test data from FetchData class 
# Returns    :- DataFrame containing test data
def get_test_data(stock,start_date,end_date):
    test = FetchData().execute(stock, start_date, end_date)
    return test

# Function   :- takes pre-trained ML model 
# Parameters :- model_path = file path of saved pre-trained model
# Returns    :- pre-trained ML model
def getModel(model_path=MODEL_PATH):
    with open(MODEL_PATH, 'rb') as f:
        model = pickle.load(f)
        return model

# Function   :- takes data from get_test_data function and calls pred function to predict output
# Parameters :- model - pre-trained ML model
# Returns    :- DataFrame containing output predicted by ML model
def execute(model,stock,start_date,end_date):
    # TODO get prediction data
    test = get_test_data(stock,start_date,end_date)
    X = test.drop(['Volume'], axis=1)

    # TODO get predictions
    y_pred = model.pred(X)

    # TODO print predictions
    test["pred"] = y_pred
    print("X")
    print(test.pred.value_counts())

    return test

# Function   :- takes pre-trained model from getModel() and give it to execute() to predict output
# Returns    :- DataFrame containing output predicted by ML model
def calls(stock,start_date,end_date):
    model = getModel()
    return execute(model,stock,start_date,end_date)