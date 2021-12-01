lines = [x.strip() for x in open('day1/input.txt').readlines()]
measures = [int(n) for n in lines]


def count_increasing(measures):
    count = 0
    for i, n in enumerate(measures[1:]):
        if measures[i] < measures[i+1]:
            count += 1
    return count

print("Simple count", count_increasing(measures))

def roll_up(measures):
    return [measures[i] + measures[i+1] + measures[i+2] for i in range(len(measures) - 2)]

print("Rolling count", count_increasing(roll_up(measures)))