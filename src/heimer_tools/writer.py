import io
import os

import graphviz

from heimer_tools.HeimerMap import HeimerMap

DOT_PREFIX = 'digraph {\n'
DOT_SUFFIX = '}'



def table_row(text: str, bold: bool = False, align = 'LEFT'):
    if bold:
        text = '<B>%s</B>' % text
    return '<TR><TD  ALIGN="%s">%s</TD></TR>' % (align, text)


def filter_text(node_text: str):
    lines = node_text.split('\n')
    html = io.StringIO()
    html.write('<<TABLE border="0">')
    for (count, line) in enumerate(lines):
        filename, ext = os.path.splitext(line.strip())
        if ext in ['.png','.jpg','jpeg']:
            html.write(table_row('<IMG SRC="%s"/>' % line))
        elif count == 0:
            html.write(table_row(line, bold=True, align="CENTER"))
        else:
            html.write(table_row(line))
    html.write('</TABLE>>')
    result = html.getvalue()
    html.close()
    return result


def get_dot(map):
    g = graphviz.Digraph('G')
    for node in map.nodes:
        g.node(name=str(node.idx),label=filter_text(node.text),shape='rect')
    for link in map.links:
        g.edge(str(link.start), str(link.end))
    return g


def prettyfy(lines):
    lines = ['digraph {\n']+lines+['}']
    result = ''.join(lines)
    result = result.replace('\t', '    ')
    return result


def prettify_dot(map: HeimerMap):
    g = get_dot(map)
    return prettyfy(g.body)
