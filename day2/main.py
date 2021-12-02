lines = [x.strip() for x in open('day2/input.txt').readlines()]
commands = [x.split() for x in lines]

def move(direction, step):
    if direction == 'forward':
        return (step, 0)
    elif direction == 'down':
        return (0, step)
    elif direction == 'up':
        return (0, -step)
    else:
        pass

def move_and_aim(commands):
    pos = depth =  aim = 0
    for direction, step in commands:
        step = int(step)
        if direction == 'forward':
            pos += step
            depth += aim*step
        elif direction == 'down':
            aim += step
        elif direction == 'up':
            aim -= step
        else:
            pass
    return pos * depth


start = [0, 0]
for direction, step in commands:
    delta_pos, delta_depth = move(direction, int(step))
    start[0] += delta_pos
    start[1] += delta_depth

print("day 2a", start[0] * start[1])
print("day 2b", move_and_aim(commands))