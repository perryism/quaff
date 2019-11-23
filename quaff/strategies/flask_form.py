from flask import request
from .. import annotations_items
from jinja2 import Template
from .flask_endpoint import FlaskEndpoint

CSS_TEMPLATE = """
<style>
    .param {
        margin: 5px;
    }
</style>
"""

FORM_TEMPLATE = """
{% block content %}
<form method="POST">
  <div id="params">
  {% for element in elements %}
    <div class="param">
    {{ element }}: <input type="input" name="{{ element }}" /><br />
    </div>
  {% endfor %}
  </div>
  <div name="action">
    <input type="submit" value="{{ action_name }}" />
  </div>
</form>
{% endblock %}
"""

class FormRenderer:
    def __init__(self, template_script, css):
        self.template = Template(css + template_script)

    def render(self, elements, action_name):
        return self.template.render(elements=elements, action_name=action_name)

class FlaskForm(FlaskEndpoint):
    def __init__(self, app, rule, template=FORM_TEMPLATE, css=CSS_TEMPLATE):
        super().__init__(app, rule)
        self.renderer = FormRenderer(template, css)

    def perform(self, func):
        if request.method == "GET":
            elements = [k for k, v in annotations_items(func)]
            return self.renderer.render(elements, func.__name__)
        else:
            return super().perform(func)
