from util import Day
from aocd import submit
from math import prod


def hex_to_bin(hex_str):
    return bin(int(hex_str, 16))[2:].zfill(len(hex_str) * 4)


def literal_packet(message):
    flag = False
    out = []
    for i in range(6, len(message), 5):
        if message[i] == "0":
            flag = not flag
        out.append(message[i + 1 : i + 5])
        if flag:
            break
    return "".join(out), i + 5


def decode(message):
    version = int(message[:3], 2)
    type_id = int(message[3:6], 2)
    # Type ID 4 is literal package
    if type_id == 4:
        out, length = literal_packet(message)
        value = [out]
    # Any other number is operator package
    else:
        value = []
        length_type = int(message[6])
        if length_type == 1:
            # Number of Sub packets
            subpackets = int(message[7 : 7 + 11], 2)
            length = 7 + 11
            for i in range(subpackets):
                if length + 6 > len(message):
                    print(
                        message, i,
                    )
                v, val, o = decode(message[length:])
                version += v
                value.append(val)
                length += o

        elif length_type == 0:
            # Total Length of Sub packet
            length = 7 + 15 + int(message[7 : 7 + 15], 2)
            offset = 7 + 15
            while offset + 6 <= length:
                v, val, o = decode(message[offset:length])
                version += v
                value.append(val)
                offset += o
    func = [
        sum,
        prod,
        min,
        max,
        lambda x: int(x[0], 2),
        lambda x: x[0] > x[1],
        lambda x: x[0] < x[1],
        lambda x: x[0] == x[1],
    ][type_id]
    return version, func(value), length


def main(day, part=1):
    day.data = hex_to_bin(day.data[0])
    x = decode(day.data)
    if part == 1:
        return x[0]
    if part == 2:
        return x[1]


if __name__ == "__main__":
    day = Day(16)
    day.download()

    day.load(typing=str)
    p1 = main(day)
    print(p1)
    submit(p1, part="a", day=16, year=2021)

    day.load(typing=str)
    p2 = main(day, part=2)
    print(p2)
    submit(p2, part="b", day=16, year=2021)
