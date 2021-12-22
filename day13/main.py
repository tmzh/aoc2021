import os


def parse_input(input_lines):
    grids = {
        tuple(map(int, x.split(','))): 1
        for x in filter(lambda x: ',' in x, input_lines)
    }
    instructions = list(filter(lambda x: x.startswith('fold'), input_lines))
    return grids, instructions


def fold_grid(grid, x_fold, y_fold):
    grid2 = {}
    for x, y in grid:
        if x_fold == 0:
            if y > y_fold:
                grid2[(x, 2 * y_fold - y)] = grid.get((x, 2 * y_fold - y), 0) | grid[(x, y)]
            else:
                grid2[(x, y)] = grid[(x, y)]
        if y_fold == 0:
            if x > x_fold:
                grid2[(2 * x_fold - x, y)] = grid.get((2 * x_fold - x, ), 0) | grid[(x, y)]
            else:
                grid2[(x, y)] = grid[(x, y)]
    return grid2


def parse_instruction(instruction):
    pos = int(instruction[13:])
    if instruction[11] == 'x':
        return pos, 0
    else:
        return 0, pos

def plot_grid(grid):
    X, Y = map(max, zip(*grid.keys()))
    for y in range(Y): 
        print(*[' #'[(x,y) in grid] for x in range(X)])


def count_dots_1(lines):
    grid, instructions = parse_input(lines)
    x_fold, y_fold = parse_instruction(instructions[0])
    grid = fold_grid(grid, x_fold, y_fold)
    return sum(grid.values())

def count_dots_2(lines):
    grid, instructions = parse_input(lines)
    for instruction in instructions:
        x_fold, y_fold = parse_instruction(instruction)
        grid = fold_grid(grid, x_fold, y_fold)
    plot_grid(grid)

if __name__ == "__main__":
    script_dir = os.path.dirname(__file__)

    input_file = "input.txt"
    input_file_path = os.path.join(script_dir, input_file)
    input_lines = [l.strip() for l in open(input_file_path).readlines()]
    print("day 13a: ", count_dots_1(input_lines))
    print("day 13b: ")
    count_dots_2(input_lines)
