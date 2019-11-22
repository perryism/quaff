from .. import annotations_items

class StrategyBase:
    def before_setup(self, func):
        raise NotImplementedError
    def before_return(self, func, wrapped_f):
        raise NotImplementedError
    def get_var(self, var_name):
        raise NotImplementedError

    def get_args(self, func):
        args = {}
        for var_name, tipe in annotations_items(func):
            if var_name == "return" : continue
            args[var_name] = tipe(self.get_var(var_name))
        return args

    def perform(self, func):
        args = self.get_args(func)
        result = func(**args)
        return result
