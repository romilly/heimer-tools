import io

from heimer_tools.HeimerMap import HeimerMap

DOT_PREFIX = 'graph {\n'
DOT_SUFFIX = '}'


def write_contents(map: HeimerMap, r: io.StringIO):
    for node in map.nodes:
        r.write('    %s;\n' % node.text)
    for link in map.links:
        r.write('    %s -- %s;\n' % (map.node_text(link.start), map.node_text(link.end)))

def write_dot(map: HeimerMap) -> str:
    r = io.StringIO()
    r.write(DOT_PREFIX)
    write_contents(map, r)
    r.write(DOT_SUFFIX)
    result = r.getvalue()
    r.close()
    return result
