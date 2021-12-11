import os
from itertools import product


def parse_input(input):
    lots = [int(s) for s in input[0].split(',')]
    grids, grid = [], []
    for line in input[2:]:
        if line == '':
            grids.append(grid)
            grid = []
        else:
            grid.append([int(g.strip()) for g in line.split()])
    grids.append(grid)
    return lots, grids 

def bingo(grid):
    for i in range(5):
        if all(grid[i][j] == -1 for j in range(5)):
            return True
        if all(grid[j][i] == -1 for j in range(5)):
            return True
    return False
 
def last_winning_score(lines):
    lots, grids = parse_input(lines)
    for draw in lots:
        for grid in grids:
            for i, j in product(range(5), range(5)):
                if grid[i][j] == draw:
                    grid[i][j] = -1
            if bingo(grid):
                last_draw, last_score =  draw , sum(grid[i][j] for i, j in product(range(5), range(5)) if grid[i][j] != -1)
        for n, grid in enumerate(grids):
            if bingo(grid):
                del(grids[n])
    return last_draw * last_score

def winning_score(lines):
    lots, grids = parse_input(lines)
    for draw in lots:
        for grid in grids:
            for i, j in product(range(5), range(5)):
                if grid[i][j] == draw:
                    grid[i][j] = -1
            if bingo(grid):
                return draw * sum(grid[i][j] for i, j in product(range(5), range(5)) if grid[i][j] != -1)

if __name__ == "__main__":
    script_dir = os.path.dirname(__file__)

    input_file = "input.txt"
    input_file_path = os.path.join(script_dir, input_file)

    input = [x.strip() for x in open(input_file_path).readlines()]
    print("day 4a", winning_score(input))
    print("day 4b", last_winning_score(input))