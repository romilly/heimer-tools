import os.path
import unittest

from hamcrest import assert_that, contains_string

from heimer_tools.convert import illustrated_dot_data
from heimer_tools.convert import simple_dot_data

DATA_DIR = '/home/romilly/git/active/heimer-tools/data'


def path_to(relative_path: str):
    return os.path.join(DATA_DIR, relative_path)


def read(file_name):
    with open(file_name) as f:
        contents = f.read()
    return contents


class IllustratedDotFileTestCase(unittest.TestCase):
    def test_small_map(self):
        expected = read(path_to('test.dot'))
        df = illustrated_dot_data(path_to('test.alz'))
        self.assertEqual(expected, df)

    def test_big_map(self):
        dot_data = illustrated_dot_data(path_to('exponential.alz'))
        assert_that(dot_data, contains_string('digraph G {'))
        assert_that(dot_data, contains_string('Becoming an Expert'))


class SimpleDotFileTestCase(unittest.TestCase):
    def test_small_map(self):
        expected = read(path_to('simple.dot'))
        df = simple_dot_data(path_to('test.alz'))
        self.assertEqual(expected, df)



if __name__ == '__main__':
    unittest.main()
