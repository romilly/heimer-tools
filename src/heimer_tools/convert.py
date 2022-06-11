from heimer_tools.reader import read_map
from heimer_tools.writer import illustrated_dot


def illustrated_dot_data(heimer_file: str):
    map = read_map(heimer_file)
    return illustrated_dot(map)
