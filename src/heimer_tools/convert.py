from heimer_tools.reader import read_map
from heimer_tools.writer import prettify_dot


def convert(heimer_file: str):
    map = read_map(heimer_file)
    return prettify_dot(map)
