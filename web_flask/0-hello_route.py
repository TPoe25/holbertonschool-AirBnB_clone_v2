#!/usr/bin/python3
"""
Starts Flask application
"""

from flask import Flask
import sys
print(sys.path)

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ shows output of Flask application """
    return 'Hello HBNB!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
