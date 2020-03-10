from flask import Flask, request
import requests
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/report', methods=['POST'])
def process_report():
    print(request.form)
    return 200

app.run(host='0.0.0.0');