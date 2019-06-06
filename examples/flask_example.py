from flask import Flask
app = Flask(__name__)

import sys
sys.path.append("..")

from quaff import quaff

def add(x, y):
    return x + y

@quaff(app, "/add")
def add_api(y: int = 0, x: int = 0) -> int:
    return add(x, y)

if __name__ == "__main__":
    app.run(host = '0.0.0.0',port=5556)
