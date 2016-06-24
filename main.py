# We'll render HTML templates and access data sent by GET
# using the request object from flask. jsonify is required
# to send JSON as a response of a request
from flask import Flask, render_template, request
from classify import classified
import os
 

# Initialize the Flask application
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods = ['GET','POST'])
def tell():
	handle = request.form['twitterHandle']
	py_obj = classified(handle)
	age = py_obj[1] 	
	gender = py_obj[2]
	print gender, age
	if gender == 'female':		
		return render_template('female.html', py_obj= py_obj) 
	else:
		return render_template('male.html', py_obj= py_obj)

@app.route('/how')
def how_we_do():
	return render_template('how_we_do.html')

@app.route('/who')
def who_we_are():
	return render_template('who_we_are.html')

port = os.getenv('PORT', '4000')
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(port), debug=True)




