import io

from heimer_tools.HeimerMap import HeimerMap

DOT_PREFIX = 'digraph {\n'
DOT_SUFFIX = '}'


def write_contents(map: HeimerMap, r: io.StringIO):
    for node in map.nodes:
        r.write('    %d [label="%s"];\n' % (node.idx, node.text))
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
