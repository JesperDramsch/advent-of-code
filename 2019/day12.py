from util import Day
from math import gcd
import operator


def parse_moons(data: str) -> list:
    out = []
    for el in ["x", "y", "z"]:
        out.append(int(data[1:-1].split(el + "=")[1].split(",", 1)[0].strip()))
        # Cut off the annoying <>
        # split at x=, y= and z=
        # Choose element 2 after the =
        # Split at the next comma once
        # Choose the first element and strip of white space
        # Boom number
    return list(out)


def moon_mash(io: tuple, europa: tuple, ganymede: tuple, callisto: tuple) -> list:
    return list(zip(io, europa, ganymede, callisto))


def coord_mash(x: tuple, y: tuple, z: tuple) -> list:
    return list(zip(x, y, z))


def gravity(position: tuple, velocities: tuple):
    vels = list(velocities)
    for x in range(len(position)):
        for y in range(x, len(position)):
            if position[y] > position[x]:
                vels[x] += 1
                vels[y] -= 1
            if position[y] < position[x]:
                vels[x] -= 1
                vels[y] += 1
    return tuple(vels)


def simulate(data, iterations):
    vels = [(0, 0, 0)] * 4

    coords = moon_mash(*data)
    velo = moon_mash(*vels)

    for dim in range(3):
        for i in range(iterations):
            # print(i,": ", data, vels)
            velo[dim] = gravity(coords[dim], velo[dim])
            coords[dim] = tuple(map(operator.add, coords[dim], velo[dim]))

    data = coord_mash(*coords)
    vels = coord_mash(*velo)
    return data, vels


def energy(pos, vel):
    ene = []
    for x in range(4):
        ene.append(sum(map(abs, pos[x])) * sum(map(abs, vel[x])))
    return tuple(ene)


def simulate_circular(data):
    vels = [(0, 0, 0)] * 4

    coords = moon_mash(*data)
    velo = moon_mash(*vels)

    coords_init = coords.copy()
    steps = [0, 0, 0]
    for dim in range(3):
        # for i in range(iterations):
        while True:
            # print(i,": ", data, vels)
            velo[dim] = gravity(coords[dim], velo[dim])
            coords[dim] = tuple(map(operator.add, coords[dim], velo[dim]))
            steps[dim] += 1
            if velo[dim] == (0, 0, 0, 0) and coords[dim] == coords_init[dim]:
                break

    return lcm(steps[0], steps[1], steps[2])


def lcm(x, y, z):
    gcd2 = gcd(y, z)
    gcd3 = gcd(x, gcd2)

    lcm2 = y * z // gcd2
    lcm3 = x * lcm2 // gcd(x, lcm2)

    return lcm3


if __name__ == "__main__":
    part1 = Day(12, 1)

    raw_data = """
    <x=-1, y=  0, z= 2>
    <x= 2, y=-10, z=-7>
    <x= 4, y= -8, z= 8>
    <x= 3, y=  5, z=-1>
    """.strip().split(
        "\n"
    )

    raw_data = """
    <x=-8, y=-10, z=0>
    <x=5, y=5, z=10>
    <x=2, y=-7, z=3>
    <x=9, y=-8, z=-3>
    """.strip().split(
        "\n"
    )

    part1.load(raw_data)
    part1.load(sep="\n")

    part1.apply(str.strip)
    # part1.data = [x[5:-1].split(",") for x in part1]
    part1.apply(parse_moons)
    part1.bake()

    # io, europa, ganymede, callisto = part1.data

    pos, vel = simulate(part1.data, 1000)

    energies = energy(pos, vel)

    part1.answer(sum(energies), v=1)

    print(simulate_circular(part1.data))

