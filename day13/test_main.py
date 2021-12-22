import unittest
from main import *

sample_input = """6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5""".splitlines()

class TestDay13(unittest.TestCase):
    def test_parse_input(self):
        grids, instructions = parse_input(sample_input)
        self.assertEqual(len(grids), 18)
        self.assertTrue(all(len(g) ==  2 for g in grids))
        self.assertEqual(len(instructions), 2)

    def test_count_dots(self):
        assert count_dots_1(sample_input) == 17

if __name__ == "__main___":
    unittest.main()