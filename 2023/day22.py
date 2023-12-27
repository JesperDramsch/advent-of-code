from day import Day
from aocd import submit
from collections import deque
from collections import defaultdict
from tqdm import tqdm


class Brick:
    def __init__(self, id, data):
        self.id = id
        self.x = None
        self.y = None
        self.z = None
        self._parse(data)

    def __repr__(self):
        return f"Brick({self.id}, {self.x}, {self.y}, {self.z})"

    def __hash__(self):
        return hash((self.id, *self.x, *self.y, *self.z))

    def __eq__(self, other):
        return self.id == other.id and self.x == other.x and self.y == other.y and self.z == other.z

    def _parse(self, data):
        start, end = data.split("~")

        start = start.split(",")
        end = end.split(",")

        x = int(start[0]), int(end[0])
        y = int(start[1]), int(end[1])
        z = int(start[2]), int(end[2])

        self.x = min(x), max(x)
        self.y = min(y), max(y)
        self.z = min(z), max(z)

    def lower(self, counter=1):
        self.z = self.z[0] - counter, self.z[1] - counter
        return self

    def higher(self):
        self.z = self.z[0] + 1, self.z[1] + 1
        return self

    def collision(self, other, offset=0):
        # Bottom collision
        if self.z[0] - offset <= 0 or self.z[0] - offset <= 0:
            return True
        if self.x[0] > other.x[1] and self.x[1] > other.x[1] or self.x[0] < other.x[0] and self.x[1] < other.x[0]:
            return False
        if self.y[0] > other.y[1] and self.y[1] > other.y[1] or self.y[0] < other.y[0] and self.y[1] < other.y[0]:
            return False
        if (
            self.z[0] - offset > other.z[1]
            and self.z[1] - offset > other.z[1]
            or self.z[0] - offset < other.z[0]
            and self.z[1] - offset < other.z[0]
        ):
            return False
        return True


class Tower:
    def __init__(self, bricks):
        self.bricks = deque(sorted((Brick(i, x) for i, x in enumerate(bricks)), key=lambda x: x.z[0]))
        self.graph = defaultdict(set)

    def settle(self):
        settled = deque()
        num_bricks = len(self.bricks)
        highest_z = 0
        while self.bricks:
            brick = self.bricks.popleft()
            # This speeds up the code by over 300%
            counter = max(0, brick.z[0] - highest_z - 1)
            while min(brick.z) >= 1:
                counter += 1
                if any(brick.collision(settled_brick, offset=counter) for settled_brick in settled) or not settled:
                    brick.lower(counter - 1)
                    settled.appendleft(brick)
                    break
            highest_z = max(highest_z, brick.z[1])
        assert len(settled) == num_bricks, f"Lost bricks during settling: {num_bricks - len(settled)}"
        self.bricks = deque(sorted(settled, key=lambda x: x.z[0]))

    def check_wiggle(self):
        self.single_supports = set()
        settled = set(self.bricks)
        backup = self.bricks.copy()

        while backup:
            brick = backup.pop()
            collisions = set()
            for settled_brick in settled:
                if brick == settled_brick:
                    continue
                if brick.collision(settled_brick, offset=1):
                    collisions.add(settled_brick)
            if len(collisions) == 1:
                self.single_supports.update(collisions)
        return len(settled - self.single_supports)

    def search_graph(self):
        from copy import deepcopy

        print(len(self.bricks), len(self.single_supports))
        backup = deepcopy(self.bricks)
        all_falling = 0
        for wiggly_brick in tqdm(self.single_supports):
            self.bricks = deepcopy(backup)
            self.bricks.remove(wiggly_brick)
            self.settle()
            all_falling += len(backup) - len(set(backup).intersection(set(self.bricks))) - 1
        return all_falling


def main(day, part=1):
    tower = Tower(day.data)
    tower.settle()
    wiggle = tower.check_wiggle()
    if part == 1:
        return wiggle
    if part == 2:
        return tower.search_graph()


if __name__ == "__main__":
    day = Day(22)
    day.download()

    day.load()
    p1 = main(day)
    print(p1)
    submit(p1, part="a", day=22, year=2023)

    # day.load()
    p2 = main(day, part=2)
    print(p2)
    submit(p2, part="b", day=22, year=2023)
