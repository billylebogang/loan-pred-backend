import flask
from flask import Flask, render_template, json, jsonify, request
import os
import numpy as np
import helper
from helper import preprocessdata, get_test_json

app = Flask(__name__)


#testing the prediction model







#testing the the end point data

data_ = [{
	"id":0,
	"name":"billy",
	"surname":"lebogang"
}, 
{
	"id":1,
	"name":"Nonofo",
	"surname":"Mathambo"
},
{
	"id":2,
	"name":"Popo",
	"surname":"lebogang"
}

]

test_data = get_test_json()

@app.route('/') # my home end point returns the main index
def home():
	return render_template('index.html')




@app.route('/data/test/', methods = ['GET', 'POST'])
def test():
	if request.method == 'GET':	
		return(test_data.to_json(orient='records') ), 201
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