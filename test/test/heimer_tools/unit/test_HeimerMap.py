import unittest

from heimer_tools.HeimerMap import HeimerMap


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.map = HeimerMap()

    def test_new_map_is_empty(self):
        self.assertEqual(len(self.map.nodes), 0)

    def test_can_add_node(self):
        self.map.add_node('foo')
        self.assertEqual(1, len(self.map.nodes))



if __name__ == '__main__':
    unittest.main()
