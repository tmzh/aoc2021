import os
from enum import Enum

parse_input = lambda lines: '{0:08b}'.format(int(lines[0], 16))
parse_bits = lambda data: int(data, 2)


def parse_literal(data):
    val = ''
    while data[0] != '0':
        val += data[1:5]
        data = data[5:]
    val += data[1:5]
    return parse_bits(val)


def parse_packet(data):
    packet, remaining = None, None
    return packet, remaining


class PacketType(Enum):
    LITERAL = 1
    OPERATOR = 2


class Packet(object):
    def __init__(self, bits: str):
        self.bits = bits
        self.length_of_sub_packets = None
        self.no_of_sub_packets = None

    @property
    def version(self):
        version = parse_bits(self.bits[:3])
        return version

    @property
    def type(self):
        packet_type_id = parse_bits(self.bits[3:6])
        if packet_type_id == 4:
            return PacketType.LITERAL
        else:
            return PacketType.OPERATOR

    @property
    def value(self):
        if self.type == PacketType.LITERAL:
            return parse_literal(self.bits[6:])

    def sub_packets(self):
        if self.type == PacketType.OPERATOR:
            if self.bits[6] == 0:
                self.length_of_sub_packets = self.bits[7:22]
            elif self.bits[6] == 1:
                self.no_of_sub_packets = self.bits[7:18]
        else:
            return None


if __name__ == "__main__":
    script_dir = os.path.dirname(__file__)
    input_file_path = os.path.join(script_dir, 'input.txt')
