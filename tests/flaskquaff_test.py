import unittest
from quaff import quaff
from quaff.strategies import FlaskEndpoint

from flask import Flask
app = Flask(__name__)

def add(x, y):
    return x + y

@quaff(FlaskEndpoint(app, "/add"))
def add_api(y: int, x: int) -> int:
    return add(x, y)


@quaff(FlaskEndpoint(app, "/json"))
def json(body: dict):
    return add(body["x"], body["y"])

class FlaskQuaffTest(unittest.TestCase):
    def setUp(self):
        global app
        app.testing = True
        self.client = app.test_client()

    def test_quaff(self):
        # TODO: handle errors
        # self.assertRaises(TypeError, self.client.get('/add'))

        rv = self.client.post('/add', data=dict(x=3, y=10))
        self.assertEqual(b"13", rv.data)

    def test_json(self):
        rv = self.client.post("/json", json={"x": 3, "y": 9})
        self.assertEqual(b"12", rv.data)
