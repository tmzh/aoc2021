from main import find_path, parse_input, Point, count_overlaps

sample_input = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2""".splitlines()

def test_parse_input():
    lines = parse_input(sample_input)
    assert len(lines) == 10
    assert all([isinstance(l[0], Point) for l in lines])
    assert all([isinstance(l[1], Point) for l in lines])

def test_find_path():
    points = list(find_path(Point(1,1),  Point(1,3)))
    print(points)
    assert points[0] == Point(1, 1) 
    assert points[1] == Point(1, 2) 
    assert points[2] == Point(1, 3)

def test_count_overlaps():
    paths = parse_input(sample_input)
    assert count_overlaps(paths) == 5
    assert count_overlaps(paths, include_diagonal=True) == 12