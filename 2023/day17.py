from day import Day
from aocd import submit

from heapq import heappush, heappop


class Mountain:
    def __init__(self, data):
        self._data = data
        self.grid = {}
        self.start = 0
        self.end = None
        # val, counter, pos, direction
        self.heap = [(0, 0, 0, 1), (0, 0, 0, 1j)]
        self.parse()

    def parse(self):
        for i, line in enumerate(self._data):
            for ii, val in enumerate(line):
                self.grid[i + ii * 1j] = int(val)
        else:
            self.end = i + ii * 1j

    def traverse(self, min, max):
        # Solution based on 4HbQ, because I couldn't figure it out myself
        # Dummy value because heap doesn't like comparing complex numbers
        dummy = 0
        visited = set()
        while self.heap:
            # Get the next position
            val, _, pos, direction = heappop(self.heap)

            # Finished!
            if pos == self.end:
                return val

            # Skip if we've already been here
            if (pos, direction) in visited:
                continue
            visited.add((pos, direction))

            # Add the next two directions to the heap
            for next_direction in 1j / direction, -1j / direction:
                if pos + next_direction * min not in self.grid:
                    continue
                cost = sum(self.grid[pos + next_direction * i] for i in range(1, min))
                dummy += 1
                # Step through new direction
                for steps in range(min, max + 1):
                    new_pos = pos + next_direction * steps
                    # Add valid steps
                    if new_pos in self.grid:
                        cost += self.grid[new_pos]
                        heappush(self.heap, (val + cost, dummy, new_pos, next_direction))


def main(day, part=1):
    mountain = Mountain(day.data)
    if part == 1:
        return mountain.traverse(1, 3)
    if part == 2:
        return mountain.traverse(4, 10)


if __name__ == "__main__":
    day = Day(17)
    day.download()

    day.load()
    p1 = main(day)
    print(p1)
    submit(p1, part="a", day=17, year=2023)

    p2 = main(day, part=2)
    print(p2)
    submit(p2, part="b", day=17, year=2023)
