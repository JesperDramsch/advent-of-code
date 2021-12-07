from util import Day
from aocd import submit


def linear_fuel_cost(nums, target):
    return sum(abs(n - target) for n in nums)


def incremental_fuel_cost(nums, target):
    return sum(abs(n - target) * (abs(n - target) + 1) // 2 for n in nums)

def move_crab(crabs, fuel_cost=linear_fuel_cost):
    middle = int(sum(crabs) / len(crabs))

    visited = {}

    # Max number of steps is all integers in the range of the data
    for i in range(max(crabs) - min(crabs) + 1):

        cost = fuel_cost(crabs, middle)
        visited[middle] = cost

        lower, upper = visited.get(middle - 1), visited.get(middle + 1)

        if lower is None and upper is None:
            middle -= 1
        elif lower is None and upper < cost:
            middle += 1
        elif lower is None and upper > cost:
            middle -= 1
        elif upper is None and lower > cost:
            middle += 1
        elif upper is None and lower < cost:
            middle -= 1
        elif lower > cost < upper:
            print("Solved after {i} iterations".format(i=i))
            return int(middle)
        else:
            middle = int(sum(crabs) / len(crabs)) + 10


def main(day, part=1):
    if part == 1:
        lowest = move_crab(day.data)
        fuel = linear_fuel_cost(day.data, lowest)
    if part == 2:
        lowest = move_crab(day.data, fuel_cost=incremental_fuel_cost)
        fuel = incremental_fuel_cost(day.data, lowest)
    return fuel


if __name__ == "__main__":
    day = Day(7)
    day.download()

    day.load(sep=",", typing=int)
    p1 = main(day)
    print(p1)
    submit(p1, part="a", day=7, year=2021)

    day.load(sep=",", typing=int)
    p2 = main(day, part=2)
    print(p2)
    submit(p2, part="b", day=7, year=2021)
