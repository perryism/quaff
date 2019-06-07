class quaff(object):
    def __init__(self, strategy):
        self.strategy = strategy

    def __call__(self, func):
        self.strategy.before_setup(func)
        #args will be ignored on purpose
        def wrapped_f(*args):
            args = self._get_args(func)
            result = func(**args)
            return str(result)

        self.strategy.before_return(func, wrapped_f)

        return wrapped_f

    def _get_args(self, func):
        args = {}
        for var_name, tipe in func.__annotations__.items():
            if var_name == "return" : continue
            args[var_name] = tipe(self.strategy.get_var(var_name))
        return args
