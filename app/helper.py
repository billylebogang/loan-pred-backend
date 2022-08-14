import numpy as np
import pandas as pd
import joblib
import sklearn
import flask
from flask import jsonify

print('hello from me to you')

def preprocessdata( gender, married, education, self_employed, applicant_income, co_applicant_income, loan_amount, loan_amount_term, credit_history, property_area):

    if (gender.lower() == 'male'):
        gender = 1
    else:
        gender == 0 
   
    if (married.lower()  == 'yes'):
        married = 1
    else:
        married = 0 

    if (education.lower()  == 'graduate'):
        education = 1
    else:
        education = 0 

    if (self_employed.lower()  == 'yes'):
        self_employed = 1
    else:
        self_employed = 0 

    if (property_area.lower()  == 'urban'):
        property_area = 1
    else:
        property_area = 0 





    test_data = [[gender, married, education, self_employed, applicant_income, co_applicant_income, loan_amount, loan_amount_term, credit_history, property_area]]

    trained_model = joblib.load('./model_1.pkl') #loading the model

    prediction = trained_model.predict(test_data) # making a prediction

    return prediction




#results = preprocessdata( 'male', 'no', 'graduate', 'no', 100000, 100000, 1000, 360, 2, 'urban' )

def get_test_json():

    df = pd.read_csv("./data/train.csv")
   # print( jsonify(df.iloc[0]))
    #return(df.head().to_json(orient='records'))
    return(df.head())
    








