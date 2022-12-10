import sys
import json
from flask import Flask
from quickstart import *

import os
dir_path = os.path.dirname(os.path.realpath(__file__))

app = Flask(__name__)


@app.route("/")
def hello():
    value = {
        "test": "works"
    }
    return json.dumps(value)


@app.route("/test")
def test():
    data = testing()
    return json.dumps({"data": data})


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000)
