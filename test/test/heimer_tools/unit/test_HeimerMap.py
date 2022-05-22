import unittest

from heimer_tools.HeimerMap import HeimerMap


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.map = HeimerMap()

    def test_new_map_is_empty(self):
        self.assertEqual(len(self.map.nodes), 0)

    def test_can_add_node(self):
        node_index = self.map.add_node(0, 'foo')
        self.assertEqual(1, len(self.map.nodes))
        self.assertEqual(0, node_index)

    def test_can_add_link(self):
        n1 = self.map.add_node(1, 'One')
        n2 = self.map.add_node(2, 'Two')
        self.map.add_edge(n1, n2)
        self.assertEqual(1, len(self.map.links))


if __name__ == '__main__':
    unittest.main()
