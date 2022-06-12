from abc import ABC, abstractmethod

import graphviz

from heimer_tools.HeimerMap import HeimerMap, Node, Edge


class HeimerVisitor(ABC):
    def visit(self, heimer_map: HeimerMap):
        for node in heimer_map.nodes:
            self.visit_node(node)
        for edge in heimer_map.edges:
            self.visit_edge(edge)

    @abstractmethod
    def visit_node(self, node: Node):
        pass

    @abstractmethod
    def visit_edge(self, edge: Edge):
        pass


class DotMaker(HeimerVisitor, ABC):
    def __init__(self):
        HeimerVisitor.__init__(self)
        self.graph = graphviz.Digraph('G')

    def visit_edge(self, edge: Edge):
        self.graph.edge(str(edge.start), str(edge.end))

    def source(self):
        return self.graph.source
