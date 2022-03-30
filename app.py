import nltk
# !/usr/bin/python
import train_chatbot
import waitress
# app.py
from flask import Flask  # import flask
from chatapp import *


SERVER_NAME = "0.0.0.0"

app = Flask(__name__)  # create an app instance


@app.route("/<lang>/<response>")               # at the end point
def create_response(lang, response):          # call method to find response
    return chatbot_response(lang, response)   # Get response using flask

@app.route("/<response>")               # at the end point
def create_responses(response):          # call method to find response
    return chatbot_response("en", response)   # Get response using flask

if __name__ == "__main__":              # on running python app.py
    from waitress import serve
    serve(app, host=SERVER_NAME, port=5000)
