import os.path
import unittest

from hamcrest import assert_that, contains_string

from heimer_tools.convert import convert

DATA_DIR = '/home/romilly/git/active/heimer-tools/data'


def path_to(relative_path: str):
    return os.path.join(DATA_DIR, relative_path)


def read(file_name):
    with open(file_name) as f:
        contents = f.read()
    return contents


class DotFilerTestCase(unittest.TestCase):
    def test_small_map(self):
        expected = read(path_to('test.dot'))
        df = convert(path_to('test.alz'))
        self.assertEqual(expected, df)

    def test_big_map(self):
        dot_data = convert(path_to('exponential.alz'))
        assert_that(dot_data, contains_string('graph {'))
        assert_that(dot_data, contains_string('Becoming an Expert'))


if __name__ == '__main__':
    unittest.main()
