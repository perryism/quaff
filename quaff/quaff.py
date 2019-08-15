from . import annotations_items

class quaff(object):
    def __init__(self, strategy, output=str):
        self.strategy = strategy
        self.output = output

    def __call__(self, func):
        self.strategy.before_setup(func)
        #args will be ignored on purpose
        def wrapped_f(*args):
            args = self.strategy.get_args(func)
            result = func(**args)
            return self.output(result)

        self.strategy.before_return(func, wrapped_f)

        return wrapped_f
