import os
from itertools import chain, product
from collections import Counter

def neighbhors(i, j, w, h):
    for x in [-1, 1]:
        if 0 <= (i + x) < h:
            yield [i + x, j]
        if 0 <= (j + x) < w:
            yield [i, j + x] 

def label_neighbhors(grid, labels, i, j,  label):
    h, w = len(grid), len(grid[0])
    for m, n in neighbhors(i, j, w, h):
        if grid[m][n] < 9 and labels[m][n] == 0:
            labels[m][n] = label
            label_neighbhors(grid, labels, m, n, label)

def three_largest_basins(grid):
    label = 0
    h, w = len(grid), len(grid[0])
    labels = [[0]*w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if all([grid[i][j] < grid[m][n] for m, n in neighbhors(i, j, w, h)]):
                label = label + 1
                labels[i][j] = label
                label_neighbhors(grid, labels, i, j, label)
    counts = Counter(chain.from_iterable(labels))
    del counts[0]
    result = 1
    for _, v in counts.most_common(3):
        result *= v
    return result



def sum_lowest_points(grid):
    s = 0
    h, w = len(grid), len(grid[0])
    for i, row in enumerate(grid):
        for j, v in enumerate(row):
            if all([v < grid[m][n] for m, n in neighbhors(i, j, w, h)]):
                s += v + 1
    return s

if __name__ == "__main__":
    script_dir = os.path.dirname(__file__)

    input_file = "input.txt"
    input_file_path = os.path.join(script_dir, input_file)

    # input = open(input_file_path).readlines()
    input_grid = [list(map(int, x.strip())) for x in open(input_file_path).readlines()]

    print("day 9a: ", sum_lowest_points(input_grid))
    print("day 9b: ", three_largest_basins(input_grid))