import argparse
from .strategy_base import StrategyBase
from .. import annotations_items

class CommandArgs(StrategyBase):
    """
    This is a simple argparse. it's by no means to replace the full implementation of argparse
    """
    def __init__(self, description):
        self.parser = argparse.ArgumentParser(description=description)

    def before_setup(self, func):
        for var_name, tipe in annotations_items(func):
           self.parser.add_argument('-%s'%var_name, type=tipe)

        self.args = self.parser.parse_args()

    def before_return(self, func, wrapped_f):
        pass

    def get_var(self, var_name):
        return getattr(self.args, var_name)
