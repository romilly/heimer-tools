from heimer_tools.reader import read_map
from heimer_tools.writer import write_dot


def convert(filename):
    map = read_map(filename)
    return write_dot(map)
