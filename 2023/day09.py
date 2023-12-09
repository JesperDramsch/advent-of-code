from day import Day
from aocd import submit
from utils.parser import Parser


class Sequence:
    def __init__(self, sequence):
        self._sequence = sequence
        self.data = None
        self.next_entry = []
        self.prev_entry = []
        self.build_diff_sequences()
        self.calculate_next_entry()
        self.calculate_prev_entry()

    def diff(self, sequence):
        return [sequence[i + 1] - sequence[i] for i in range(len(sequence) - 1)]

    def build_diff_sequences(self):
        diff_sequences = []
        sequence = self._sequence
        while any(s != 0 for s in sequence):
            diff_sequences.append(sequence)
            sequence = self.diff(sequence)
        self.data = diff_sequences

    def calculate_next_entry(self):
        next_val = 0
        for sequence in self.data[::-1]:
            next_val = sequence[-1] + next_val
            self.next_entry.append(next_val)

    def calculate_prev_entry(self):
        prev_val = 0
        for sequence in self.data[::-1]:
            prev_val = sequence[0] - prev_val
            self.prev_entry.append(prev_val)

    def sum(self):
        return sum(self.next_entry)

    def __repr__(self) -> str:
        return f"{self.data}"


def main(day, part=1):
    sequences = Parser(day.data)
    sequences.parse_list_of_lists(sep2=" ", sep="\n", typing=int)
    sequences = [Sequence(sequence) for sequence in sequences.data]
    if part == 1:
        return sum(sequence.next_entry[-1] for sequence in sequences)
    if part == 2:
        return sum(sequence.prev_entry[-1] for sequence in sequences)


if __name__ == "__main__":
    day = Day(9)
    day.download()

    day.load(process=False)
    p1 = main(day)
    print(p1)
    submit(p1, part="a", day=9, year=2023)

    p2 = main(day, part=2)
    print(p2)
    submit(p2, part="b", day=9, year=2023)
