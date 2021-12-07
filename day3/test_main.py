from main import get_power_consumption, get_power_consumption2

def test_get_rate():
    input = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010"""
    readings = input.splitlines()
    assert get_power_consumption(readings) == 198
    assert get_power_consumption2(readings) == 230

if __name__ == "__main__":
    test_get_rate()