import unittest

from main import parse_input, get_neighbors, shortest_path, expand_grid

sample_input = """1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581""".splitlines()


class Day15TestCase(unittest.TestCase):
    def test_parse_input(self):
        grid = parse_input(sample_input)
        self.assertEqual(100, len(grid))

    def test_get_neighbors(self):
        param_list = [
            ((0, 0), [(1, 0), (0, 1)]),
            ((1, 0), [(0, 0), (2, 0), (1, 1)]),
            ((0, 9), [(1, 9), (0, 8)]),
            ((5, 5), [(4, 5), (6, 5), (5, 4), (5, 6)]),
        ]
        grid = parse_input(sample_input)
        for param, expected in param_list:
            with self.subTest():
                self.assertEqual(list(get_neighbors(grid, *param)), expected)

    def test_shorted_path_part_a(self):
        grid = parse_input(sample_input)
        self.assertEqual(40, shortest_path(grid))

    def test_shorted_path_part_b(self):
        grid = parse_input(sample_input)
        expand_grid(grid, 5)
        self.assertEqual(315, shortest_path(grid))


if __name__ == '__main__':
    unittest.main()
