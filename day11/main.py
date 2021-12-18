import os
from typing import List


def neighbours(x, y, points):
    return filter(
        points.get,
        [
            (x + 1, y + 1),
            (x + 1, y),
            (x + 1, y - 1),
            (x, y + 1),
            (x, y - 1),
            (x - 1, y + 1),
            (x - 1, y),
            (x - 1, y - 1),
        ],
    )

def increase_energy(points, points_to_energize) -> List[int]:
    points_to_flash = [] 
    for point in points_to_energize:
        points[point] = 0
        for n in neighbours(*point, points):
            points[n] += 1
            if points[n] > 9:
                points_to_flash.append(points[n])
    return points_to_flash

def tick(points, flashes):
    for p in points:
        points[p] += 1
    points_to_flash = {p for p in points if points[p] > 9}

    while points_to_flash:
        flashes += 1
        p = points_to_flash.pop()
        points[p] = 0
        for n in neighbours(*p, points):
            points[n] += 1
            if points[n] > 9:
                points_to_flash.add(n)
                
    return points, flashes

def grid_to_dict(g):
    return {(i, j): e for i, x in enumerate(g) for j, e in enumerate(x)}


if __name__ == "__main__":
    script_dir = os.path.dirname(__file__)

    input_file = "input.txt"
    input_file_path = os.path.join(script_dir, input_file)
    input_lines = [l.strip() for l in open(input_file_path).readlines()]

    state = [[int(x) for x in r] for r in input_lines]
    points = grid_to_dict(state)
    flashes = 0
    for _ in range(100):
        points, flashes = tick(points, flashes)

    steps = 100
    while sum(points.values()) != 0:
        points, flashes = tick(points, flashes)
        steps += 1


    print("day 11a: ", flashes)
    print("day 11b: ", steps)