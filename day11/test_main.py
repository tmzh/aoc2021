from main import grid_to_dict, tick

sample_input = """5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526""".splitlines()


def test_flashing():
    state1 = [[int(x.strip()) for x in r] for r in """11111
19991
19191
19991
11111""".splitlines()]
    state2 = [[int(x.strip()) for x in r] for r in """34543
40004
50005
40004
34543""".splitlines()]
    state3 = [[int(x.strip()) for x in r] for r in """45654
51115
61116
51115
45654""".splitlines()]
    assert grid_to_dict(state2), 9 == tick(state1, 0)
    assert grid_to_dict(state3), 9 == tick(state2, 9)