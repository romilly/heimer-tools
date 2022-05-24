import io

from heimer_tools.HeimerMap import HeimerMap

DOT_PREFIX = 'digraph {\n'
DOT_SUFFIX = '}'


def filter_text(node_text: str):
    lines = node_text.split('\n')
    html = io.StringIO()
    html.write('<<TABLE border="0">')
    for (count, line) in enumerate(lines):
        if line.endswith('.png'):
            html.write('<TR><TD><IMG SRC="%s"/></TD></TR>' % line)
        elif count == 0:
            html.write('<TR><TD><B>%s</B></TD></TR>' % line)
        else:
            html.write('<TR><TD>%s</TD></TR>' % line)
    html.write('</TABLE>>')
    result = html.getvalue()
    html.close()
    return result


def write_contents(map: HeimerMap, r: io.StringIO):
    for node in map.nodes:
        text = filter_text(node.text)
        r.write('    %d [label = %s];\n' % (node.idx, text))
    for link in map.links:
        r.write('    %d -> %d;\n' % (link.start, link.end))

def write_dot(map: HeimerMap) -> str:
    r = io.StringIO()
    r.write(DOT_PREFIX)
    write_contents(map, r)
    r.write(DOT_SUFFIX)
    result = r.getvalue()
    r.close()
    return result
