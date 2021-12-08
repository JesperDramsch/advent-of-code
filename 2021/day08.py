from util import Day
from aocd import submit


def parse_input(data):
    # Sort all strings to make dictionary look-up easier
    # Sort observations by length, so indexing is possible
    observation = (tuple("".join(sorted(y)) for y in sorted(x[:58].split(" "), key=len)) for x in data)
    # Do not sort outputs by length as order matters
    output = (tuple("".join(sorted(y)) for y in x[61:].split(" ")) for x in data)
    return observation, output


def easy_count(data):
    count = 0
    for row in data:
        count += sum(1 for element in row if len(element) in (2, 3, 4, 7))
    return count


def is_in(cipher, word):
    """Check if a cipher is in a word with arbitrary sorting"""
    return all(letter in word for letter in cipher)


def decrypt_cipher(observation):
    all_ciphers = []
    for i, row in enumerate(observation):
        cipher = {1: row[0], 7: row[1], 4: row[2], 8: row[9]}

        # 6-element digits
        for i in range(6, 9):
            # Check if the 4 is in the 6-element cipher. Must be a 9
            if is_in(cipher[4], row[i]):
                cipher[9] = row[i]
            # Otherwise check if the 1 is in the 6-element cipher. Must be a 0
            elif is_in(cipher[1], row[i]):
                cipher[0] = row[i]
            # Otherwise it's a 6
            else:
                cipher[6] = row[i]

        # 5-element digits
        for i in range(3, 6):
            # Check if the 1 is in the 5-element cipher. Must be a 3
            if is_in(cipher[1], row[i]):
                cipher[3] = row[i]
            else:
                # Now we have to count similarity
                same = 0
                for letter in row[i]:
                    same += letter in cipher[9]
                # If 5 elements fit, it's a 5
                if same == 5:
                    cipher[5] = row[i]
                # If only 4 fit, it's a 2
                elif same == 4:
                    cipher[2] = row[i]

        # Invert the mapping to "cipher": "value"
        all_ciphers.append({key: str(value) for value, key in cipher.items()})
    return all_ciphers


def decipher_digits(output, ciphers):
    nums = 0
    # Combine ciphers and outputs to obtain secret number
    for row, cipher in zip(output, ciphers):
        nums += int("".join([cipher[digit] for digit in row]))
    return nums


def main(day, part=1):
    day.data = parse_input(day.data)
    if part == 1:
        return easy_count(day.data[1])
    if part == 2:
        ciphers = decrypt_cipher(day.data[0])
        return decipher_digits(day.data[1], ciphers)


if __name__ == "__main__":
    day = Day(8)
    day.download()

    day.load(typing=str)
    p1 = main(day)
    print(p1)
    submit(p1, part="a", day=8, year=2021)

    day.load(typing=str)
    p2 = main(day, part=2)
    print(p2)
    submit(p2, part="b", day=8, year=2021)
