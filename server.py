
from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/resume')
def resume():
    return render_template('resume.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

app.run(debug = True)
