#!/usr/bin/python3
""" Testing the falsk app"""

from flask import Flask

app = Flask(__name__)

@app.route('/')
def start_app():
    return "Hello World"
















if __name__ == "__main__":
    app.run(debug=True)
