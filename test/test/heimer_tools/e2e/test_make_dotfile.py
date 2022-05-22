import unittest

from heimer_tools.HeimerMap import HeimerMap
from heimer_tools.reader import read_map
from heimer_tools.writer import write_dot


def read(file_name):
    with open(file_name) as f:
        contents = f.read()
    return contents


def convert(filename):
    map = read_map(filename)
    return write_dot(map)


class DotFilerTestCase(unittest.TestCase):
    def test_something(self):
        expected = read('/home/romilly/git/active/heimer-tools/data/test.dot')
        df = convert('/home/romilly/git/active/heimer-tools/data/test.alz')
        self.assertEqual(expected, df)  # add assertion here


if __name__ == '__main__':
    unittest.main()
