import flask
from flask import Flask, render_template, json, jsonify, request
import os
import numpy as np
import pandas as pd
import joblib
import sklearn

app = Flask(__name__)


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


def get_test_json():
    df = pd.read_csv("./app/data/train.csv")
    return(df.head())

#testing the the end point data

test_data = get_test_json()

@app.route('/') # my home end point returns the main index
def home():
	return render_template('index.html')




@app.route('/data/test/', methods = ['GET', 'POST'])
def test():
	if request.method == 'GET':	
		return app.response_class( response = test_data.to_json(orient='records'), status = 200, mimetype = 'application/json')
	else:
		'nothing found', 404



@app.route('/predict/', methods = ['GET', 'POST'] ) #the prediction point
def predict():
	if request.method == 'GET':
		if len(data_) > 0:
			return jsonify("prediction here")
		else: 
			'nothing found', 404

	
	if request.method == 'POST':


		gender = request.form['gender']
		married = request.form['married']
		education = request.form['education']
		self_employed = request.form['self_employed']
		applicant_income = request.form['applicant_income']
		co_applicant_income = request.form['co_applicant_income']
		loan_amount = request.form['loan_amount']
		loan_amount_term = request.form['loan_amount_term']
		credit_history = request.form['credit_history']
		property_area = request.form['property_area']

		new_object = {
			'gender':gender ,
			'married': married,
			'education': education,
			'self_employed': self_employed,
			'applicant_income': applicant_income,
			'co_applicant_income':co_applicant_income ,
			'loan_amount': loan_amount,
			'loan_amount_term': loan_amount_term,
			'credit_history': credit_history,
			'property_area': property_area
		}

		prediction_results = preprocessdata(gender, married, education, self_employed, applicant_income, co_applicant_income, loan_amount, loan_amount_term, credit_history, property_area)

		arr = np.array(prediction_results)

		results = np.array_str(arr)

		no = {
			'loan_status':'denied'
		}
		yes = {
			'loan_status':'Approved'
		}	

		if results[(len(results)-1)//2:(len(results)+2)//2] == 1:
			 return jsonify(yes)
		else:
			return jsonify(no), 201





if __name__ == "__main__":
	app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))               