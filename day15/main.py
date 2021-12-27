import math
import os
from heapq import heappop, heappush
from itertools import product


def parse_input(lines):
    return {(i, j): int(v)
            for i, line in enumerate(lines)
            for j, v in enumerate(line.strip())}


def get_neighbors(grid, i, j):
    for m, n in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        if (i + m, j + n) in grid:
            yield i + m, j + n


def shortest_path(grid):
    dim = int(math.sqrt(len(grid)))
    distance = [[math.inf] * dim for _ in range(dim)]
    q = [(0, (0, 0))]

    while q:
        curr_dist, (curr_i, curr_j) = heappop(q)

        if curr_i == dim - 1 and curr_j == dim - 1:
            return curr_dist

        for i, j in filter(lambda p: distance[p[0]][p[1]] == math.inf,
                           get_neighbors(grid, curr_i, curr_j)):
            new_distance = curr_dist + grid[(i, j)]
            heappush(q, (new_distance, (i, j)))
            distance[i][j] = new_distance
    return math.inf


def expand_grid(grid, n_tiles):
    dim = int(math.sqrt(len(grid)))
    for i, j, x, y in product(range(dim), range(dim), range(n_tiles), range(n_tiles)):
        v = grid[(i, j)] + x + y
        if v > 9:
            v = v - 9
        grid[(i + dim * x, j + dim * y)] = v


if __name__ == "__main__":
    script_dir = os.path.dirname(__file__)
    file_path = os.path.join(script_dir, 'input.txt')
    input_grid = parse_input(open(file_path).readlines())
    # input_grid = np.genfromtxt(file_path, delimiter=1, dtype=int)
    print("day 15a: ", shortest_path(input_grid))
    expand_grid(input_grid, 5)
    print("day 15b: ", shortest_path(input_grid))
