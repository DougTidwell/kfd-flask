# app.py - About the simplest web server you can create.
# Sets up a web server via Flask and listens on port 5000. 
# localhost:5000 returns "Hello, World!" 
# localhost:5000/?name=Doug returns "Hello, Doug!"

from flask import Flask, escape, request

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'

