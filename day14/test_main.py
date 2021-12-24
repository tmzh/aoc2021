import unittest

from main import parse_input, insert_n_times_using_count

sample_input = """NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C""".splitlines()


class MyTestCase(unittest.TestCase):
    def test_count_insertion(self):
        template, rules = parse_input(sample_input)
        self.assertEqual({'B': 1749, 'C': 298, 'H': 161, 'N': 865}, insert_n_times_using_count(template, rules, 10))


if __name__ == '__main__':
    unittest.main()