import unittest

from hamcrest import assert_that, contains_string

from heimer_tools.convert import convert


def read(file_name):
    with open(file_name) as f:
        contents = f.read()
    return contents


class DotFilerTestCase(unittest.TestCase):
    def test_small_map(self):
        expected = read('/home/romilly/git/active/heimer-tools/data/test.dot')
        df = convert('/home/romilly/git/active/heimer-tools/data/test.alz')
        self.assertEqual(expected, df)  # add assertion here

    def test_big_map(self):
        dot_data = convert('/home/romilly/git/active/heimer-tools/data/exponential.alz')
        assert_that(dot_data, contains_string('graph {'))
        assert_that(dot_data, contains_string('Becoming an Expert'))


if __name__ == '__main__':
    unittest.main()
