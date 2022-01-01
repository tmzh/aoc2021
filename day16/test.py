import unittest

from main import parse_input, parse_bits, parse_literal, Packet

sample_input = "8A004A801A8002F478".splitlines()


class Test(unittest.TestCase):
    def test_parse_input(self):
        self.assertEqual("100010100000000001001010100000000001"
                         "101010000000000000101111010001111000",
                         parse_input("8A004A801A8002F478".splitlines()))

    def test_parse_bits(self):
        parsed = parse_bits('1010')
        self.assertEqual(10, parsed)

    def test_parse_literal(self):
        data = '101111111000101000'
        self.assertEqual(2021, parse_literal(data))


class TestLiteralPacket(unittest.TestCase):
    def test_literal_packet(self):
        packet = Packet('110100101111111000101000')
        self.assertEqual(2021, packet.value)


if __name__ == "__main__":
    unittest.main()
