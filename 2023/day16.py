from day import Day
from aocd import submit
from collections import defaultdict

# I apologize for this code


class LasterMaze:
    def __init__(self, data):
        self.data = data
        self.grid = [list(row) for row in data]
        self.width = len(self.grid[0])
        self.height = len(self.grid)
        self.objects = {}
        self.rows = defaultdict(dict)
        self.cols = defaultdict(dict)
        self.raypath = set()
        self.parse()

        self.mirrors = ["\\", "/"]
        self.splitters = ["|", "-"]

    def parse(self):
        for y, row in enumerate(self.grid):
            for x, col in enumerate(row):
                if col != ".":
                    self.rows[x][y] = col
                    self.cols[y][x] = col

    def fire(self, pos=(0, -1), direction=1j, visited=None):
        if visited is None:
            self.raypath = set()
            visited = set()

        # Define the searchable direction and collapse dimension
        if direction.real == 0:  # horizontal
            pos_index = True
            search = self.cols[pos[not pos_index]]
            direction_1d = int(direction.imag)
        elif direction.imag == 0:  # vertical
            pos_index = False
            search = self.rows[pos[not pos_index]]
            direction_1d = int(direction.real)

        # Get the next symbol in the direction we're going (high or low)
        closest, next_symbol = self.find_closest_symbol(search, pos[pos_index], direction_1d)

        # Dynamically update the position
        next_pos = list(pos)
        next_pos[pos_index] = closest
        next_pos = tuple(next_pos)

        # Don't add paths with 0 length
        if next_pos == pos:
            self.raypath.update(visited)
            return visited

        # If we've already visited this path, don't continue
        if (pos, next_pos) in visited:
            self.raypath.update(visited)
            return visited

        # Add the path to the visited set
        visited.add((pos, next_pos))

        # Determine new direction based on the next symbol
        for new_direction in self.next_direction(direction, next_symbol):
            visited.update(self.fire(pos=next_pos, direction=new_direction, visited=visited))
        self.raypath.update(visited)
        return visited

    def find_closest_symbol(self, search, pos, direction_1d):
        closest = None
        next_symbol = None
        for number, symbol in search.items():
            # If we're going up, we want the closest number that's higher than our current position
            if direction_1d > 0 and number > pos:
                if closest is None or (number - pos) < (closest - pos):
                    closest = number
                    next_symbol = symbol
            # If we're going down, we want the closest number that's lower than our current position
            elif direction_1d < 0 and number < pos:
                if closest is None or (pos - number) < (pos - closest):
                    closest = number
                    next_symbol = symbol
        else:
            # If we're going up and we didn't find a higher number, we want the highest number
            if direction_1d > 0 and closest is None:
                closest = self.height - 1
            # If we're going down and we didn't find a lower number, we want the lowest number
            elif direction_1d < 0 and closest is None:
                closest = 0
        return closest, next_symbol

    def next_direction(self, direction, next_symbol):
        new_direction = ()
        if next_symbol in self.mirrors:
            if next_symbol == "\\":
                if direction.real == 0:
                    new_direction = (direction * -1j,)
                elif direction.imag == 0:
                    new_direction = (direction * 1j,)
            elif next_symbol == "/":
                if direction.real == 0:
                    new_direction = (direction * 1j,)
                elif direction.imag == 0:
                    new_direction = (direction * -1j,)
        elif next_symbol in self.splitters:
            if (direction.real == 0 and next_symbol == "-") or (direction.imag == 0 and next_symbol == "|"):
                new_direction = (direction,)
            if (direction.real == 0 and next_symbol == "|") or (direction.imag == 0 and next_symbol == "-"):
                new_direction = (direction * 1j, direction * -1j)
        return new_direction

    def print(self):
        x = [[z for z in q] for q in self.data]
        for start, end in self.raypath:
            for i in range(min(start[0], end[0]), max(start[0], end[0]) + 1):
                for j in range(min(start[1], end[1]), max(start[1], end[1]) + 1):
                    x[i][j] = "#"
        print("\n".join([str(i) + " " + "".join(row) for i, row in enumerate(x)]) + "\n")

    def calc_energized(self):
        # Wanted to do this "smart" but double counted crossing lasers. Oh well.
        activated = set()
        for start, end in self.raypath:
            for i in range(min(start[0], end[0]), max(start[0], end[0]) + 1):
                for j in range(min(start[1], end[1]), max(start[1], end[1]) + 1):
                    activated.add((i, j))
        return len(activated)

    def find_max_energy(self):
        max_energy = []
        # Cover full width
        for i in range(self.width):
            if i in [0, self.width - 1]:
                # Go down the sides
                for ii in range(self.height):
                    if ii in [0, self.height - 1]:
                        # Corners
                        if (i, ii) in (
                            (0, 0),
                            (0, self.height - 1),
                            (self.width - 1, 0),
                            (self.width - 1, self.height - 1),
                        ):
                            for direction in [1, -1, 1j, -1j]:
                                self.fire(pos=(i, ii), direction=direction)
                                max_energy.append(self.calc_energized())
                    else:
                        # Sides
                        for direction in [1, -1]:
                            self.fire(pos=(i, ii), direction=direction)
                            max_energy.append(self.calc_energized())
            else:
                # Top and bottom
                for direction in [1j, -1j]:
                    self.fire(pos=(i, ii), direction=direction)
                    max_energy.append(self.calc_energized())
        return max(max_energy)


def main(day, part=1):
    maze = LasterMaze(day.data)
    maze.fire()
    if part == 1:
        maze.print()
        return maze.calc_energized() - 1
    if part == 2:
        return maze.find_max_energy()


if __name__ == "__main__":
    day = Day(16)
    day.download()

    day.load()
    #     data = r""".|...\....
    # /.-.\.....
    # .....|-...
    # ........|.
    # ..........
    # .........\
    # ..../.\\..
    # .-.-/..|..
    # .|....-|.\
    # ..//.|...."""

    #     day.load(data)
    p1 = main(day)
    print(p1)
    submit(p1, part="a", day=16, year=2023)

    # day.load()
    p2 = main(day, part=2)
    print(p2)
    submit(p2, part="b", day=16, year=2023)
