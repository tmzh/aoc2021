import os
from typing import List
from collections import Counter
from itertools import zip_longest


class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other: object) -> bool:
        if isinstance(other, self.__class__):
            return self.x == other.x and self.y == other.y
        else:
            return False

    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)

    def __hash__(self) -> int:
        return hash((self.x, self.y))

    def __repr__(self) -> int:
        return f'Point({self.x}, {self.y})'

def parse_point(point):
    x, y = point.split(',')
    return Point(int(x), int(y))

def parse_input(lines):
    points = []
    lines = [l.split(' -> ') for l in lines]
    for start, end in lines:
        start = parse_point(start)
        end = parse_point(end)
        points.append([start, end])
    return points

def steps_to(start, end):
    if start > end:
        return range(start, end - 1, -1)
    else:
        return range(start, end + 1)

def find_path(start: Point, end: Point, include_diagonal=False) -> List[Point]:
    if start.x == end.x:
        return [Point(start.x, y) for y in steps_to(start.y, end.y)]
    elif start.y == end.y:
        return [Point(x, start.y) for x in steps_to(start.x, end.x)]
    elif abs(start.x - end.x) == abs(start.y - end.y) and include_diagonal:
        return [Point(i, j) for i, j in zip_longest(steps_to(start.x, end.x), steps_to(start.y, end.y))]
    else:
        pass

def count_overlaps(paths, include_diagonal=False):
    c = Counter()
    for start, end in paths:
        c.update(find_path(start, end, include_diagonal))
    return len([c for x in c if c[x] > 1])


if __name__ == "__main__":
    script_dir = os.path.dirname(__file__)

    input_file = "input.txt"
    input_file_path = os.path.join(script_dir, input_file)

    input = [x.strip() for x in open(input_file_path).readlines()]
    paths = parse_input(input)

    print("day 5a", count_overlaps(paths))
    print("day 5b", count_overlaps(paths, include_diagonal=True))