from flask import request
from .strategies import flask_request

class quaff(object):
    def __init__(self, app, rule, strategy=None):
        self.rule = rule
        self.app = app

        if strategy is None:
            self.strategy = flask_request

    def __call__(self, func):
        #args will be ignored on purpose
        def wrapped_f(*args):
            args = self._get_args(func)
            result = func(**args)
            return str(result)

        self.app.add_url_rule(self.rule, func.__name__, wrapped_f)
        return wrapped_f

    def _get_var(self, var_name):
        if request.method == "POST":
            return request.form[var_name]
        else:
            return request.args.get(var_name)

    def _get_args(self, func):
        args = {}
        for var_name, tipe in func.__annotations__.items():
            if var_name == "return" : continue
            args[var_name] = tipe(self.strategy(var_name))
        return args
