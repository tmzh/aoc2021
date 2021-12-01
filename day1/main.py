lines = [x.strip() for x in open('day1/input.txt').readlines()]
measures = [int(n) for n in lines]

count = 0

for i, n in enumerate(measures[1:]):
    if measures[i] < measures[i+1]:
        count += 1

print("Simple count", count)

rolling_measures = [measures[i] + measures[i+1] + measures[i+2] for i in range(len(measures) - 2)]
rolling_count = 0

for i, n in enumerate(rolling_measures[1:]):
    if rolling_measures[i] < rolling_measures[i+1]:
        rolling_count += 1

print("Rolling count", rolling_count)