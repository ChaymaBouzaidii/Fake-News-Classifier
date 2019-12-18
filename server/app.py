# -*- coding: utf-8 -*-
"""app.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1F8nrSCnArvHBXrS90CeW-M5Pw8xm6TIP
"""

from google.colab import drive
drive.mount('/content/drive')

import os
os.chdir('/content/drive/My Drive/FakeNews')

!pip install flask-ngrok

!pip install flask-cors

from flask_ngrok import run_with_ngrok
from flask import Flask, jsonify, request, render_template
from flask_cors import CORS, cross_origin
from predict import Predict
import pandas as pd
import json
from random import randrange
import codecs

app = Flask(__name__, static_folder="./public/static", template_folder="./public")
cors = CORS(app)
run_with_ngrok(app)  #Make api public

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/random', methods=['GET'])
def random():
    data = pd.read_csv("data/fake_or_real_news_test.csv")
    index = randrange(0, len(data)-1, 1)
    response = jsonify({'title': data.loc[index].title, 'text': data.loc[index].text})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/predict', methods=['POST'])
def predict():
    param = jsonify((request.data).decode('utf-8'))
    param = json.loads(param.json)
    param = param['article']
    model = Predict(param)
    response = jsonify(model.predict())
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

# Only for local running
if __name__ == '__main__':
    app.run()

