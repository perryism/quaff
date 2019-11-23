from flask import Flask, request
from quaff import quaff
from quaff.strategies import FlaskForm

flask_app = Flask(__name__)

# Assume we already have some functionality implemented in the system
def add(x, y):
    return x + y

# Use jiaja2 template to customize the form
FORM_TEMPLATE = """
{% block content %}
<form method="POST">
  <div id="params">
  {% for element in elements %}
    <div class="param">
    {{ element[0] }}: <textarea name="{{ element[0] }}"></textarea><br />
    </div>
  {% endfor %}
  </div>
  <div name="action">
    <input type="submit" value="{{ action_name }}" />
  </div>
</form>
{% endblock %}
"""

CSS_TEMPLATE = """
<style>
    .param {
      margin: 5px;
    }

    textarea {
      width: 50%;
      height: 150px;
      padding: 12px 20px;
      box-sizing: border-box;
      border: 2px solid #ccc;
      border-radius: 4px;
      background-color: #f8f8f8;
      resize: none;
    }
</style>
"""

# It auto-generates a simple form
@quaff(FlaskForm(flask_app, "/add", template=FORM_TEMPLATE, css=CSS_TEMPLATE))
def add_api(y: int, x: int):
    return add(x, y)

flask_app.run(host = '0.0.0.0',port=5555)
