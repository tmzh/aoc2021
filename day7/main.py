import numpy as np

input = np.loadtxt('input.txt', dtype=int, delimiter=',')

def cost(distance):
    return distance*(distance+1)/2

print("day 7a", np.sum(np.abs(input - np.floor(np.median(input)))))
print("day 7b", min(sum(cost(abs(input - np.floor(np.mean(input))))),
          sum(cost(abs(input - np.ceil(np.mean(input)))))))