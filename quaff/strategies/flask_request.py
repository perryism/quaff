from flask import request

def get_var(var_name):
    global request
    if request.method == "POST":
        return request.form[var_name]
    else:
        return request.args.get(var_name)
