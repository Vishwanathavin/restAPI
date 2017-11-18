from flask import Flask,jsonify,request
from flask_pymongo import PyMongo


app=Flask(__name__)
app.config['MONGO_DBNAME'] = 'vishwa_restDB'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/vishwa_restDB'
mongo = PyMongo(app)

@app.route('/')
def home():
	response = {'message': "Welcome to RESTAPI!"}
	return jsonify(response)

@app.route('/register', methods=['POST'])
def register():

    # Get data from form/postman

    input_ = {

      'firstName':request.form.get('firstName'),
      'lastName':request.form.get('lastName'),
      'emailId':request.form.get('emailId'),
      'password':request.form.get('password')
                    }

    print(input_)
    # Put in database
    output = mongo.db.users.insert(input_)


    return

if __name__ == "__main__":
	app.run(host="0.0.0.0")