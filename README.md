# Quick start

## Install

<pre>
pip install git+https://github.com/perryism/flask-quaff.git
</pre>

<pre>
from flask import Flask, request
from flaskquaff import quaff

flask_app = Flask(__name__)

# Assume we already have some functionality implemented in the system
def add(x, y):
    return x + y

# We can create an endpoint quickly, and it will look up the inputs in query string or form variables
@quaff(flask_app, "/add")
def add_api(y: int = 0, x: int = 0):
    return add(x, y)

flask_app.run(host = '0.0.0.0',port=5555)
</pre>


<pre>
curl http://localhost:5000?x=10&y=11
</pre>
