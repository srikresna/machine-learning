import json
import numpy as np
import tensorflow as tf
from flask import Flask, request

app = Flask(__name__)

MODEL_PATH = "fashion-mnist"
model = tf.keras.models.load_model('C:\Users\ACER\Documents\wahyuninrd-pipeline\serving_model_dir')

@app.route("/")
def hello_world():
    return "Hello, World!"

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
    app.run(debug=True)
