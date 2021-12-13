from typing import List
from collections import Counter, OrderedDict

def tick(counts: List[int]) -> List[int]:
    transforms = OrderedDict({
        8: [7],
        0: [8, 6],
        1: [0],
        2: [1],
        3: [2],
        4: [3],
        5: [4],
        7: [6],
        6: [5]
    })
    new_counts = {}
    for k in counts.keys():
        for i in transforms[k]:
            new_counts[i] = new_counts.get(i, 0) + counts[k]
    return new_counts 

def tick_n_days(start, no_of_days):
    counts = Counter(start)

    for i in range(no_of_days):
        counts = tick(counts)

    return sum(counts.values())


if __name__ == "__main__":
    start = [5,3,2,2,1,1,4,1,5,5,1,3,1,5,1,2,1,4,1,2,1,2,1,4,2,4,1,5,1,3,5,4,3,3,1,4,1,3,4,4,1,5,4,3,3,2,5,1,1,3,1,4,3,2,2,3,1,3,1,3,1,5,3,5,1,3,1,4,2,1,4,1,5,5,5,2,4,2,1,4,1,3,5,5,1,4,1,1,4,2,2,1,3,1,1,1,1,3,4,1,4,1,1,1,4,4,4,1,3,1,3,4,1,4,1,2,2,2,5,4,1,3,1,2,1,4,1,4,5,2,4,5,4,1,2,1,4,2,2,2,1,3,5,2,5,1,1,4,5,4,3,2,4,1,5,2,2,5,1,4,1,5,1,3,5,1,2,1,1,1,5,4,4,5,1,1,1,4,1,3,3,5,5,1,5,2,1,1,3,1,1,3,2,3,4,4,1,5,5,3,2,1,1,1,4,3,1,3,3,1,1,2,2,1,2,2,2,1,1,5,1,2,2,5,2,4,1,1,2,4,1,2,3,4,1,2,1,2,4,2,1,1,5,3,1,4,4,4,1,5,2,3,4,4,1,5,1,2,2,4,1,1,2,1,1,1,1,5,1,3,3,1,1,1,1,4,1,2,2,5,1,2,1,3,4,1,3,4,3,3,1,1,5,5,5,2,4,3,1,4]
    print("day 6a: ", tick_n_days(start, 80))
    print("day 6b: ", tick_n_days(start, 256))
