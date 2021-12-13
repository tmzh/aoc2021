from main import tick
from collections import Counter
from operator import itemgetter


def test_tick():
    start = [3,4,3,1,2]
    counts = Counter(start)
    no_of_ticks = 18
    print(sorted(counts.items()))
    for _ in range(no_of_ticks):
        counts = tick(counts)
        print(sorted(counts.items()))
    assert sum(counts.values()) == 26