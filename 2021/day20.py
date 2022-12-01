from util import Day
from aocd import submit
import numpy as np


def parse_input(data):
    data = [row.replace(".", "0").replace("#", "1") for row in data]
    key = data[0]
    image = np.array([list(map(int, row)) for row in data[2:]])
    return key, image


def process_image(image, key, step):
    # Establish padding number
    if step == 0:
        padding = 0
    else:
        padding = str(image[0, 0])
    
    # Find size of padding and reduce to a total padding of 3
    q, w, e, r = 3, 3, 3, 3
    for i in range(3):
        if not np.all(image[i, :] == image[0, 0]):
            break
        q -= 1
    for i in range(-1,-4,-1):
        if not np.all(image[i, :] == image[0, 0]):
            break
        w -= 1
    for i in range(3):
        if not np.all(image[:, i] == image[0, 0]):
            break
        e -= 1
    for i in range(-1,-4,-1):
        if not np.all(image[:, i] == image[0, 0]):
            break
        r -= 1

    image = np.pad(image, ((q,w), (e,r)), "constant", constant_values=(padding, padding))
    # Define the background of new image based on key
    if key[int(str(image[0, 0]) * 9, 2)] == "1":
        output_image = np.ones_like(image)
    else:
        output_image = np.zeros_like(image)
    # Iterate over image and determine if a pixel should be turned on or off
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
