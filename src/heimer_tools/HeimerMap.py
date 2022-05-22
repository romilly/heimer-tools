from typing import List


class Node:
    def __init__(self,index: int, text: str):
        self._index = index
        self.text = text


class HeimerMap:
    def __init__(self):
        self._node_dict = {}
        self._node_count = 0

    @property
    def nodes(self) -> List[Node]:
        return list(self._node_dict.values())

    def add_node(self, text: str):
        index = self._node_count
        self._node_dict[index] = Node(index, text)