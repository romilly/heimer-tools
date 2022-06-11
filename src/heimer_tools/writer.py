import io
import os

from heimer_tools.HeimerMap import Node, Edge, HeimerMap
from heimer_tools.visitor import DotMaker


class IllustratedDotMaker(DotMaker):

    def visit_node(self, node: Node):
        self.graph.node(name=str(node.idx),label=self.filter_text(node.text),shape='rect')

    def visit_edge(self, edge: Edge):
        self.graph.edge(str(edge.start), str(edge.end))

    def table_row(self, text: str, bold: bool = False, align = 'LEFT'):
        if bold:
            text = '<B>%s</B>' % text
        return '<TR><TD  ALIGN="%s">%s</TD></TR>' % (align, text)

    def filter_text(self, node_text: str):
        lines = node_text.split('\n')
        html = io.StringIO()
        html.write('<<TABLE border="0">')
        for (count, line) in enumerate(lines):
            filename, ext = os.path.splitext(line.strip())
            if ext in ['.png','.jpg','jpeg']:
                html.write(self.table_row('<IMG SRC="%s"/>' % line))
            elif count == 0:
                html.write(self.table_row(line, bold=True, align="CENTER"))
            else:
                html.write(self.table_row(line))
        html.write('</TABLE>>')
        result = html.getvalue()
        html.close()
        return result


def get_graph_body(map: HeimerMap, maker: DotMaker):
    maker.visit(map)
    return maker.body()


def wrap_body(lines):
    lines = ['digraph {\n']+lines+['}']
    result = ''.join(lines)
    result = result.replace('\t', '    ')
    return result


def illustrated_dot(map: HeimerMap):
    return wrap_body(get_graph_body(map, IllustratedDotMaker()))
