import sys
import json
from flask import Flask
from quickstart import *


app = Flask(__name__)


@app.route("/")
def hello():
    value = {
        "test": "works"
    }
    return json.dumps(value)


@app.route("/test")
def test():
    testing()
    return json.dumps('tested')


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000)
