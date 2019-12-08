from util import Day

import numpy as np
import matplotlib.pyplot as plt


def shaper(data, wide, tall):
    return np.array([int(x) for x in data[0]]).reshape(-1, tall, wide)


def min_layer(data, axis=0):
    return np.argmax([np.count_nonzero(data[i, :, :]) for i in range(data.shape[0])])


def hash(data, layer):
    return np.sum(data[layer, :, :] == 1) * np.sum(data[layer, :, :] == 2)


def sif_decode(data):
    return np.take_along_axis(data, np.expand_dims(np.argmax(data < 2, axis=0), 0), 0).squeeze()


if __name__ == "__main__":
    # Part 1
    part1 = Day(8, 1)
    part1.load(typing=str)

    part1.data = shaper(part1.data, 25, 6)
    part1.bake()

    layer_i = min_layer(part1.data)
    part1.answer(hash(part1.data, layer_i), v=1)

    # Part 2

    plt.imshow(sif_decode(part1.data))
    plt.show()
