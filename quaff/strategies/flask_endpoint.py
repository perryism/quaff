from flask import request
from .strategy_base import StrategyBase
from .. import annotations_items
from jinja2 import Template


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
    {{ element[0] }}: <input type="input" name="{{ element[0] }}" /><br />
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

class FlaskEndpoint(StrategyBase):
    def __init__(self, app, rule, template=FORM_TEMPLATE, css=CSS_TEMPLATE):
        self.rule = rule
        self.app = app
        self.renderer = FormRenderer(template, css)

    def before_setup(self, func):
        pass

    def before_return(self, func, wrapped_f):
        self.app.add_url_rule(self.rule, func.__name__, wrapped_f, methods=["GET", "POST"])

    def perform(self, func):
        if request.method == "GET":
            elements = [k for k, v in annotations_items(func)]
            return self.renderer.render(elements, func.__name__)
        else:
            return super().perform(func)

    def get_var(self, var_name):
        global request
        if request.is_json:
            return request.get_json()
        elif request.method == "POST":
            return request.form[var_name]
        else:
            return request.args.get(var_name)

