
from main import sum_lowest_points, three_largest_basins


sample_input = """2199943210
3987894921
9856789892
8767896789
9899965678"""

sample_grid = [list(map(int, x)) for x in sample_input.splitlines()]

def test_sum_lowest_points():
    assert sum_lowest_points(sample_grid) == 15


def test_three_largest_basins():
    assert three_largest_basins(sample_grid) == 1134