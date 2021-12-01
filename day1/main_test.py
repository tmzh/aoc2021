from day1.main import count_increasing, roll_up


def test_day1():
    test_input = """199
200
208
210
200
207
240
269
260
263"""
    measures = [int(x.strip()) for x in test_input.splitlines()]
    assert count_increasing(measures) == 7
    assert count_increasing(roll_up(measures)) == 5
