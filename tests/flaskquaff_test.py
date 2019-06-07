import unittest
from quaff import quaff

from flask import Flask
app = Flask(__name__)
from quaff.strategies import FlaskEndpoint

def add(x, y):
    return x + y

@quaff(FlaskEndpoint(app, "/add"))
def add_api(y: int = 0, x: int = 0) -> int:
    return add(x, y)

class FlaskQuaffTest(unittest.TestCase):
    def setUp(self):
        global app
        app.testing = True
        self.client = app.test_client()

    def test_quaff(self):
        # TODO: handle errors
        # self.assertRaises(TypeError, self.client.get('/add'))

        rv = self.client.get('/add?x=3&y=10')
        self.assertEqual(b"13", rv.data)
