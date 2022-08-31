from crypt import methods
from unittest import result
from flask import Flask, render_template, json, jsonify, request
from flask_cors import CORS, cross_origin
import os
import sys
sys.path.insert(0, './data/')
from nc_data import user_data, jobs_data

app = Flask(__name__)


@app.route('/') # my home end point returns the main index
def home():
	return render_template('index.html')




@app.route('/users', methods = ['GET', 'POST'])
def getUser():
	if request.method == 'GET':
		return jsonify(user_data)
	else:
		'nothing found', 404


#get a speacific job by id
@app.route('/users/<int:job_id>', methods=['GET'])
def users(job_id):

	python_user_object = (users_data["data"])
	
	for a in python_user_object:
		if a["id"] == job_id:
			return (a)
		else:
			return "nothing found", 404

#adding a user
@app.route('/user/newuser', methods =['POST'])
def add_new_user():

	new_user = {
		id: request.json["id"],
		email:request.json["email"],
        password:request.json["password"],
        username: request.json["username"]
	}

	user_data["data"].append(new_user)

	return jsonify(user_data)


#authenticating during log in
@app.route('/user/authorise', methods =['POST'])
def auth_new_user():

	email = request.json["email"]
	password = request.json["password"]
    
	username =  request.json["username"]

	for user in user_data["data"]:
		if username == user["username"] and password == user["passworc"]:
			return jsonify( { result : "authorized"})
		else:
			return jsonify({ result: "unathorised"})



#get a specific job
@app.route('/jobs/<int:job_id>', methods=['GET'])
def jobs(job_id):

	python_job_object = (jobs_data["data"])
	

	for a in python_job_object:
		if a["id"] == job_id:
			return (a)
		else:
			return "nothing found", 404


@app.route('/getjobs/', methods = ['GET', 'POST'])
def get_jobs():
	if request.method == 'GET':
		return jsonify(jobs_data)
	else:
		'nothing found', 404


#adding a job
@app.route('/jobs/newjob', methods =['POST'])
def add_new_job():

	new_job = {
		"id": request.json["id"],
        "title":request.json["title"],
        "description":request.json["description"],
        "amount": request.json["amount"],
        "location":request.json[ "location"],
        "from": request.json["from"],
        "to":request.json["to"],
        "employer": request.json["employer"]
	}

	jobs_data["data"].append(new_job)

	return jsonify(user_data)



	

if __name__ == "__main__":
	app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))               