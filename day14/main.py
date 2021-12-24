import os
from collections import Counter
from itertools import tee
from operator import itemgetter
from math import ceil

def parse_input(lines):
    template = lines[0].strip()
    rules = dict([line.strip().split(' -> ') for line in lines[2:]])
    return template, rules

def count_pairs(s):
    a, b = tee(s)
    next(b, None)
    return Counter([x + y for x, y in zip(a, b)])

def insert_polymer_using_count(polymer, rules, chars):
    new_polymer = {}
    for pair, count in polymer.items():
        c = rules[pair]
        left, right = pair[0] + c, c + pair[1]
        new_polymer[left] = new_polymer.get(left, 0) + count
        new_polymer[right] = new_polymer.get(right, 0) + count
        chars[c] += count
    return new_polymer, chars

def insert_n_times_using_count(template, rules, count):
    polymer = count_pairs(template)
    c = Counter(template)
    for _ in range(count):
        polymer, c = insert_polymer_using_count(polymer, rules, c)
    return c

def part_1(lines):
    template, rules = parse_input(lines)
    new_template_count = insert_n_times_using_count(template, rules, 10)
    c = sorted(new_template_count.items(), key=itemgetter(1))
    return c[-1][1] - c[0][1]

def part_2(lines):
    template, rules = parse_input(lines)
    new_template_count = insert_n_times_using_count(template, rules, 40)
    c = sorted(new_template_count.items(), key=itemgetter(1))
    return c[-1][1] - c[0][1]


if __name__ == "__main__":
    script_dir = os.path.dirname(__file__)
    file_path = os.path.join(script_dir, 'input.txt')
    input_lines = open(file_path).readlines()
    print("day 14a: ", part_1(input_lines))
    print("day 14b: ", part_2(input_lines))
