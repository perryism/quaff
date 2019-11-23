from flask import request
from .strategy_base import StrategyBase

class FlaskEndpoint(StrategyBase):
    def __init__(self, app, rule):
        self.rule = rule
        self.app = app

    def before_setup(self, func):
        pass

    def before_return(self, func, wrapped_f):
        self.app.add_url_rule(self.rule, func.__name__, wrapped_f, methods=["GET", "POST"])

    def get_var(self, var_name):
        global request
        if request.is_json:
            return request.get_json()
        elif request.method == "POST":
            return request.form[var_name]
        else:
            return request.args.get(var_name)
