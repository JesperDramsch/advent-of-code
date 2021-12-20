from util import Day
from aocd import submit
import numpy as np


def parse_input(data):
    data = [row.replace(".", "0").replace("#", "1") for row in data]
    key = data[0]
    image = np.array([list(map(int, row)) for row in data[2:]])
    return key, image


def process_image(image, key, step):
    if step == 0:
        padding = 0
    else:
        padding = str(image[0, 0])
    image = np.pad(image, (3, 3), "constant", constant_values=(padding, padding))

    if key[int(str(image[0, 0]) * 9, 2)] == "1":
        output_image = np.ones_like(image)
    else:
        output_image = np.zeros_like(image)
    for i in range(1, image.shape[0] - 1):
        for ii in range(1, image.shape[1] - 1):
            location = int("".join(map(str, image[i - 1 : i + 2, ii - 1 : ii + 2].flatten().tolist())), 2)
            output_image[i, ii] = key[location]
    return output_image


def main(day, part=1):
    key, image = parse_input(day.data)
    if part == 1:
        image = process_image(image, key, 0)
        image = process_image(image, key, 1)
    if part == 2:
        for i in range(50):
            image = process_image(image, key, i)
    return int(np.sum(image))


if __name__ == "__main__":
    day = Day(20)
    day.download()

    day.load(typing=str)
    p1 = main(day)
    print(p1)
    submit(p1, part="a", day=20, year=2021)

    day.load(typing=str)
    p2 = main(day, part=2)
    print(p2)
    submit(p2, part="b", day=20, year=2021)
