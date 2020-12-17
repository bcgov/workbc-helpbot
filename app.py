# !/usr/bin/python
import train_chatbot
# app.py
from flask import Flask  # import flask
from chatapp import *


app = Flask(__name__)  # create an app instance


@app.route("/<response>")               # at the end point
def create_response(response):          # call method to find response
    return chatbot_response(response)   # Get response using flask

if __name__ == "__main__":              # on running python app.py
    app.run(debug=True)                 # run the flask app
