import os
import math
from collections import Counter

script_dir = os.path.dirname(__file__)
input_file = "input.txt"
input_file_path = os.path.join(script_dir, input_file)

readings = [x.strip() for x in open(input_file_path).readlines()]


def arr_to_binary(arr):
    num = 0
    for i, n in enumerate(arr):
        num += n * math.pow(2, len(arr) - i - 1)
    return num


def get_gamma_readings(readings):
    no_of_1s = sum(int(r[0]) for r in readings)
    res = int(no_of_1s >= len(readings) // 2)
    if len(readings[0]) == 1:
        return [res]
    return [res, *get_gamma_readings([r[1:] for r in readings])]


def get_readings_filtered(readings, index, type):
    no_of_1s = sum(int(r[index]) for r in readings)
    res = int(no_of_1s >= len(readings) / 2)
    if type == "epsilon":
        res = (res + 1) % 2
    readings = [r for r in readings if int(r[index]) == res]
    if not readings:
        return []
    elif len(readings) == 1:
        return [int(r) for r in readings[0]]
    else:
        return get_readings_filtered(readings, index + 1, type)


def get_power_consumption(readings):
    gamma = get_gamma_readings(readings)
    epsilon = [(r + 1) % 2 for r in gamma]
    return arr_to_binary(gamma) * arr_to_binary(epsilon)


def get_power_consumption2(readings):
    gamma = get_readings_filtered(readings, 0, "gamma")
    epsilon = get_readings_filtered(readings, 0, "epsilon")
    return arr_to_binary(gamma) * arr_to_binary(epsilon)

if __name__ == "__main__":
    print("day 3a", get_power_consumption(readings))
    print("day 3b", get_power_consumption2(readings))
