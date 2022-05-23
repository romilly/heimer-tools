from heimer_tools.HeimerMap import HeimerMap

import xml.etree.ElementTree as ET


def read_map(filename) -> HeimerMap:
    map = HeimerMap()
    document = ET.parse(filename)
    graph = document.find('graph')
    nodes = graph.findall('node')
    for node in nodes:
        map.add_node(int(node.get('index')), node.find('text').text)
    for edge in graph.findall('edge'):
        map.add_edge(int(edge.get('index0')), int(edge.get('index1')))
    return map
