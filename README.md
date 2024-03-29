# Quick start

## Install

<pre>
pip install git+https://github.com/perryism/quaff.git
</pre>


## Flask form

<pre>
from flask import Flask, request
from quaff import quaff
from quaff.strategies import FlaskForm

flask_app = Flask(__name__)

# Assume we already have some functionality implemented in the system
def add(x, y):
    return x + y

# It auto-generates a simple form
@quaff(FlaskForm(flask_app, "/add")
def add_api_json(y: int, x: int):
    return add(x, y)

flask_app.run(host = '0.0.0.0',port=5555)
</pre>


<pre>
curl http://localhost:5000/add?x=10&y=11
</pre>

### Customize html, and CSS

See examples folder

## Flask endpoint

<pre>
from flask import Flask, request
from quaff import quaff
from quaff.strategies import FlaskEndpoint

flask_app = Flask(__name__)

# Assume we already have some functionality implemented in the system
def add(x, y):
    return x + y

# We can create an endpoint quickly, and it will look up the inputs in query string or form variables
@quaff(FlaskEndpoint(flask_app, "/add"))
def add_api(y: int, x: int):
    return add(x, y)

# It supports JSON
@quaff(FlaskEndpoint(flask_app, "/add_json"))
def add_api(body: dict):
    return add(body["x"], body["y"])

flask_app.run(host = '0.0.0.0',port=5555)
</pre>


<pre>
curl http://localhost:5000?x=10&y=11
</pre>

## Command args

<pre>
from quaff.strategies import CommandArgs
from quaff import quaff

def add(x, y):
    return x + y

@quaff(CommandArgs("Add"))
def add_api(y: int, x: int):
    return add(x, y)

print(add_api())
</pre>

<pre>
python add.py -x 3 -y 26
</pre>
