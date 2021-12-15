from main import count_unique, parse_pattern, word_to_digit, sum_numbers


sample_input = """be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce"""

tokens = [x.split(' | ') for x in sample_input.splitlines()]

def test_count_unique():
    uniques = count_unique(tokens)
    assert uniques == 26

def test_sum_numbers():
    assert sum_numbers(tokens) == 61229

def test_parse_words():
    words = 'acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab'.split()
    assert ('d', 'e', 'a', 'f', 'g', 'b', 'c') == parse_pattern(words)

def test_word_to_digit():
    mappings = ('d', 'e', 'a', 'f', 'g', 'b', 'c')
    patterns = [
        ['acedgfb', 8],
        ['cdfbe', 5],
        ['gcdfa', 2],
        ['fbcad', 3],
        ['dab', 7],
        ['cefabd', 9],
        ['cdfgeb', 6],
        ['eafb', 4],
        ['cagedb', 0],
        ['ab', 1]]
    for word, digit in patterns:
        assert word_to_digit(word, mappings) == digit