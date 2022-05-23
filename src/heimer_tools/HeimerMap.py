from typing import List


class Node:
    def __init__(self, idx: int, text: str):
        self.idx = idx
        self.text = text


class Edge:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end


class HeimerMap:
    def __init__(self):
        self._nodes = {}
        self._edges = []
        self._node_count = 0

    @property
    def nodes(self) -> List[Node]:
        return sorted(self._nodes.values(), key=lambda node: node.idx)

    def add_node(self, index: int, text: str) -> int:
        # text = text.replace(' ','_')
        self._nodes[index] = Node(index, text)
        return index

    @property
    def links(self) -> List[Edge]:
        return self._edges

    def add_edge(self, start, end):
        self._edges.append(Edge(start, end))

    def node_text(self, index: int):
        return self._nodes[index].text