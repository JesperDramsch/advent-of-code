import sys

sys.path.insert(0, ".")
from util import Day
from day08 import *
import numpy as np


def test_given_1():
    part1 = Day(8, 1)
    part1.load(["123456789012"])

    part1.data = shaper(part1.data, 3, 2)
    part1.bake()
    assert part1.data.shape == (2, 2, 3)

    layer_i = min_layer(part1.data)
    assert layer_i == 0

    part1.answer(hash(part1.data, layer_i), v=1)
    assert part1.result == 1


def test_part_1():
    part1 = Day(8, 1)
    part1.load(typing=str, sep=",")

    part1.data = shaper(part1.data, 25, 6)
    part1.bake()

    layer_i = min_layer(part1.data)

    part1.answer(hash(part1.data, layer_i), v=1)
    assert part1.result == 2520

    # Part 2

    # plt.imshow(np.take_along_axis(part1.data, np.expand_dims(np.argmax(part1.data < 2, axis=0), 0), 0).squeeze())
    # plt.show()


def test_given_2():
    part1 = Day(8, 1)
    part1.load(["0222112222120000"])

    part1.data = shaper(part1.data, 2, 2)
    part1.bake()

    np.testing.assert_array_equal(sif_decode(part1.data), np.array([[0, 1], [1, 0]]))
