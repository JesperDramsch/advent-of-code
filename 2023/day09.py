from day import Day
from aocd import submit
from utils.parser import Parser

# from sklearn.ensemble import RandomForestRegressor as ML

from sklearn.linear_model import LinearRegression as ML
from sklearn.preprocessing import PolynomialFeatures as Prep
from sklearn.preprocessing import SplineTransformer as Prep
import numpy as np
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import (
    DotProduct,
    WhiteKernel,
    ConstantKernel,
    RBF,
    RationalQuadratic,
    Exponentiation,
)


class Sequence:
    def __init__(self, sequence):
        self._sequence = sequence
        self.data = None
        self.next_entry = []
        self.build_diff_sequences()
        self.calculate_next_entry()

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
        pass


if __name__ == "__main__":
    day = Day(9)
    day.download()

    day.load(process=False)
    #     data = """0 3 6 9 12 15
    # 1 3 6 10 15 21
    # 10 13 16 21 30 45"""

    #     day.load(data, process=False)
    p1 = main(day)
    print(p1)
    submit(p1, part="a", day=9, year=2023)

    # day.load()
    # p2 = main(day, part=2)
    # print(p2)
    # submit(p2, part="b", day=9, year=2023)
