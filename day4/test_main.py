from main import bingo, parse_input, winning_score, last_winning_score


input = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7"""

def test_parse_input():
    lines = [x for x in input.splitlines()]
    lots, grids = parse_input(lines)
    print(grids)
    assert len(grids) == 3
    assert all(len(g) == 5 for g in grids)
    assert lots ==  [7, 4, 9, 5, 11, 17, 23, 2, 0, 14, 21, 24, 10, 16, 13, 6, 15, 25, 12, 22, 18, 20, 8, 19, 3, 26, 1]

def test_last_winning_score():
    lines = [x for x in input.splitlines()]
    score = last_winning_score(lines)
    assert score == 1924 

def test_winning_score():
    lines = [x for x in input.splitlines()]
    score = winning_score(lines)
    assert score == 4512

def test_bingo():
    grid = [[-1]* 5, [list(range(5))] * 4]
    assert bingo(grid)
    grid = [[-1, 0, 1, 2, 3]] * 5
    assert bingo(grid)
    grid = [[1, -1, 1, 2, 3]] * 5
    assert bingo(grid)
    grid = [[1, 1, -1, 2, 3]] * 5
    assert bingo(grid)
    grid = [[1, 1, 1, -1, 3]] * 5
    assert bingo(grid)
    grid = [list(range(5))]*5
    assert not bingo(grid)