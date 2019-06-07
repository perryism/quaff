import unittest

if __name__ == "__main__":
    import sys, os
    sys.path.append(os.path.abspath(os.path.join(__file__, os.pardir, os.pardir)))

from quaff import quaff
from quaff.strategies import CommandArgs

def add(x, y):
    return x + y

@quaff(CommandArgs("Add"))
def add_api(y: int, x: int):
    return add(x, y)

import subprocess
class CommandTest(unittest.TestCase):
    def test_command(self):
        command = "python %s -x 3 -y 4"%__file__
        stdoutdata = subprocess.getoutput(command)
        self.assertEqual(stdoutdata, "7")

if __name__ == "__main__":
    print(add_api())
