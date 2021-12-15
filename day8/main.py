import os
from collections import Counter

def count_unique(input):
    tokens = [x[1].split(' ') for x in input]
    count = 0
    for bag in tokens:
        count += len([x for x in bag if len(x.strip()) in [2, 4, 3, 7]]) 
    return count

def sum_numbers(input):
    displays = [x[1].split(' ') for x in input]
    patterns = [x[0].split(' ') for x in input]
    sum = 0
    for i, pattern in enumerate(patterns):
        mappings = parse_pattern(pattern)
        sum += int(''.join( [str(word_to_digit(word.strip(), mappings)) for word in displays[i]]))
    return sum


def parse_pattern(pattern):
    pattern = [set(word.strip()) for word in pattern]
    c = Counter()
    for word in pattern:
        c.update(word)
        if len(word) == 2:
            one = word
        elif len(word) == 3:
            seven = word
        elif len(word) == 4:
            four = word
        elif len(word) == 7:
            eight = word
    t = (seven - one).pop()
    t_l = filter(lambda x: c[x] == 6, c).__next__()
    t_r = (set(filter(lambda x: c[x] == 8, c)) - set(t)).pop()
    m   = (four - one - set(t_l)).pop()
    b_l = filter(lambda x: c[x] == 4, c).__next__()
    b_r = filter(lambda x: c[x] == 9, c).__next__()
    b   = (set(filter(lambda x: c[x] == 7, c)) - set(m)).pop()
    return (t, t_l, t_r, m, b_l, b_r, b)

def word_to_digit(word, mappings):
    t, t_l, t_r, m, b_l, b_r, b = mappings
    one = set([t_r, b_r])
    four = one | set(t_l + m)
    seven = one | set(t)
    three = seven | set(m + b)
    eight = three | set(t_l + b_l)
    zero = eight - set(m)
    nine = eight - set(b_l)
    five = nine - set(t_r)
    six = five | set(b_l)
    two = eight - set(t_l + b_r)

    if set(word) == zero:
        return 0
    if set(word) == one: 
        return 1
    if set(word) == eight: 
        return 8
    if set(word) == seven:
        return 7
    if set(word) == three:
        return 3
    if set(word) == nine:
        return 9
    if set(word) == five:
        return 5
    if set(word) == six:
        return 6
    if set(word) == two:
        return 2
    if set(word) == four:
        return 4

if __name__ == "__main__":
    script_dir = os.path.dirname(__file__)

    input_file = "input.txt"
    input_file_path = os.path.join(script_dir, input_file)

    input = [x.split(' | ') for x in open(input_file_path).readlines()]
    uniques = count_unique(input)
    sums = sum_numbers(input)

    print("day 8a: ", uniques)
    print("day 8b: ", sums)