from collections import deque
from typing import List
import os

pairs = {
    '{': '}',
    '[': ']',
    '(': ')',
    '<': '>' 
}


def find_first_corrupted(s: str) -> str:
    stack = deque()
    for c in s:
        if c in pairs:
            stack.appendleft(c)
        elif c == pairs[stack[0]]:
            stack.popleft()
        else:
            return c


def auto_completion_score(s: str) -> int:
    points = {
        '(' : 1,
        '[' : 2,
        '{' : 3,
        '<' : 4
    }
    stack = deque()
    score = 0
    for c in s:
        if c in pairs:
            stack.appendleft(c)
        elif c == pairs[stack[0]]:
            stack.popleft()
        else:
            return -1
    for c in stack:
        score *= 5
        score += points[c]
    return score

def calc_part_a_score(lines: List[str])-> int:
    points = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137
    }
    return sum(points.get(find_first_corrupted(line), 0) for line in lines)

def calc_part_b_score(lines: List[str])-> int:
    scores = [auto_completion_score(l) for l in lines]
    scores = sorted(filter(lambda x: x != -1, scores))
    size = len(scores)
    return scores[size // 2]


if __name__ == "__main__":
    script_dir = os.path.dirname(__file__)

    input_file = "input.txt"
    input_file_path = os.path.join(script_dir, input_file)

    input_lines = [l.strip() for l in open(input_file_path).readlines()]
    print("day 10a:", calc_part_a_score(input_lines))
    print("day 10b:", calc_part_b_score(input_lines))