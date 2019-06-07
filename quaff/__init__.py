__all__ = ["annotations_items", "quaff"]

def annotations_items(func):
    for var_name, tipe in func.__annotations__.items():
       if var_name == "return" : continue
       yield var_name, tipe

from .quaff import quaff
