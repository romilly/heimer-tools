import io
import os

from heimer_tools.HeimerMap import Node, Edge, HeimerMap
from heimer_tools.reader import read_map
from heimer_tools.visitor import DotMaker


class IllustratedDotMaker(DotMaker):

    def visit_node(self, node: Node):
        self.graph.node(name=str(node.idx),label=self.filter_text(node.text),shape='rect')

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


def get_graph_source(heimer_map: HeimerMap, maker: DotMaker):
    maker.visit(heimer_map)
    return maker.source()


def replace_tabs(text):
    result = text.replace('\t', '    ')
    return result


def illustrated_dot(heimer_map: HeimerMap):
    return replace_tabs(get_graph_source(heimer_map, IllustratedDotMaker()))


def illustrated_dot_data(heimer_file: str):
    map = read_map(heimer_file)
    return illustrated_dot(map)



class SimpleDotMaker(DotMaker):
    def visit_node(self, node: Node):
        self.graph.node(name=str(node.idx), label=node.text)


def simple_dot(heimer_map: HeimerMap):
    return replace_tabs(get_graph_source(heimer_map, SimpleDotMaker()))


def simple_dot_data(heimer_file: str):
    map = read_map(heimer_file)
    return simple_dot(map)