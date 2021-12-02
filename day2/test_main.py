from main import move, move_and_aim

def test_move():
    commands = [x.split() for x in """forward 5
down 5
forward 8
up 3
down 8
forward 2""".splitlines()]
    start = [0, 0]
    for direction, step in commands:
        delta_pos, delta_depth = move(direction, int(step))
        start[0] += delta_pos
        start[1] += delta_depth
    assert start[0] * start[1] == 150 


def test_move_and_aim():
    commands = [x.split() for x in """forward 5
down 5
forward 8
up 3
down 8
forward 2""".splitlines()]
    assert move_and_aim(commands) == 900