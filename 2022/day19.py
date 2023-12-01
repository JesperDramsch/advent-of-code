from day import Day
from aocd import submit
from collections import Counter, deque
import re
# Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 4 ore. Each obsidian robot costs 4 ore and 12 clay. Each geode robot costs 4 ore and 19 obsidian.


class Blueprint:
    def __init__(self, data):
        self.data = data
        self.number = None
        self.robots = Counter({"ore": {}, "clay": {}, "obsidian": {}, "geode": {}})
        self.parse()

    def __str__(self):
        return f"Blueprint {self.number}: robot {self.robots['ore']}, clay robot - {self.robots['clay']}, obsidian robot - {self.robots['obsidian']}, geode robot - {self.robots['geode']}"

    def __repr__(self):
        return self.__str__()

    def parse(self):
        self.number = re.search(r'Blueprint (\d+):', self.data).group(1)
        self.robots['ore'] = self.extract_cost(re.search(r'Each ore robot costs ([\d a-z]+).', self.data).group(1))
        self.robots['clay'] = self.extract_cost(re.search(r'Each clay robot costs ([\d a-z]+).', self.data).group(1))
        self.robots['obsidian'] = self.extract_cost(re.search(r'Each obsidian robot costs ([\d a-z]+).', self.data).group(1))
        self.robots['geode'] = self.extract_cost(re.search(r'Each geode robot costs ([\d a-z]+).', self.data).group(1))

    def extract_cost(self, costs):
        parsed_cost = Counter()
        for cost in costs.split(' and '):
            match cost.split(' '):
                case [num, 'ore']:
                    parsed_cost['ore'] = int(num)
                case [num, 'clay']:
                    parsed_cost['clay'] = int(num)
                case [num, 'obsidian']:
                    parsed_cost['obsidian'] = int(num)
        return parsed_cost

class Factory:
    def __init__(self, blueprint, minute=24):
        self.blueprint = blueprint
        self.resources = Counter({"ore": 0, "clay": 0, "obsidian": 0, "geode": 0})
        self.minutes = minute
        self.robots = Counter({"ore": 1, "clay": 0, "obsidian": 0, "geode": 0})

    def __str__(self):
        return f"Factory: {self.blueprint.number}\n\tStorage: {self.resources}\n\tRobots: {self.robots+Counter()}\n"

    def __repr__(self):
        return self.__str__()

    def mine(self):
        for resource in self.resources.keys():
            self.resources[resource] += self.robots[resource]
    
    def build(self, robot=None):
        if robot is None:
            robot = []  
        else:
            self.resources = self.resources - self.blueprint.robots[robot]
            robot = [robot]

        self.built_robots = Counter(robot)

    def deploy(self):
        self.robots = self.robots + self.built_robots
        self.built_robots = Counter()

    def available_to_build(self):
        return [name for name, robot in self.blueprint.robots.items() if self.resources >= robot]

    def run(self, robot=None):
        self.build(robot)
        self.mine()
        self.deploy()
        self.minutes -= 1

    def find_max_geodes(self):
        while self.minutes > 0:
            self.run()
        return self.resources["geode"]

    def quality(self):
        return self.resources["geode"] * self.number


def main(day, part=1):
    day.parse_list()
    day.apply(Blueprint)
    day.apply(Factory)
    if part == 1:
        day.data[1].run()
        day.data[1].run()
        day.data[1].run()
        day.data[1].run()
        day.data[1].run()
        day.data[1].run()
        return day.data
    if part == 2:
        pass

if __name__ == "__main__":
    day = Day(19)
    day.download()

    day.load()
    data = """Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 2 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 2 ore and 7 obsidian.
Blueprint 2: Each ore robot costs 2 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 8 clay. Each geode robot costs 3 ore and 12 obsidian."""

    day.load(data)
    p1 = main(day)
    print(p1)
    # submit(p1, part="a", day=19, year=2022)

    # day.load()
    # p2 = main(day, part=2)
    # print(p2)
    # submit(p2, part="b", day=19, year=2022)
