from util import Day

class Robot(Day):
    def __init__(self, day, part):
        super().__init__(day, part)
        self.concurrent = True
        self.location = (0,0)
        self.path = {self.location: 0}
        self.direction = 0
        self.painted = set()

    def parse_direction(self):
        dir_dict = {0: (0,  1), # Up
                    1: (1,  0), # Right
                    2: (0, -1), # Down
                    3: (-1, 0)} # Left
        return dir_dict[self.direction]

    def turn(self, direction):
        # left  0 right 1 
        if direction == 0:
            self.turn_left()
        elif direction == 1:
            self.turn_right()
        return self

    def turn_right(self, turns=1):
        self.direction = (self.direction + turns) % 4
        return self.walk()

    def turn_left(self, turns=1):
        self.direction = (self.direction - turns ) % 4
        return self.walk()
    
    def walk(self):
        step_x, step_y = self.parse_direction()
        self.location = self.location[0] + step_x, self.location[1] + step_y
        self.path[self.location] = self.path.get(self.location, 0)
        return self

    def vision(self):
        self.input(self.path[self.location])
        return self
    
    def paint(self, color):
        self.path[self.location] = color
        self.painted.add(self.location)
        # black 0 white 1
        return self
    
    def run(self):
        while True:
            # First See
            self.vision()
            # Then think and pause
            out = self.execute_opcode(reset_pointer=False)
            if isinstance(out, Robot):
                break
            # Then paint
            self.paint(out)
            # Then think and pause
            out = self.execute_opcode(reset_pointer=False)
            # Then turn
            self.turn(out)
        return self
    
    def visualize(self):
        x, y = zip(*part2.path.keys())
        painting = {0: ".", 1: "#"}
        for j in range(max(y)+1, min(y)-2, -1):
            for i in range(min(x), max(x)+1):
                print(painting[part2.path.get((i,j), 0)], end=" ")
            print()


if __name__ == "__main__":
    part1 = Robot(11, 1)
    part1.load(typing=int, sep=",")

    part1.run()
    print("Caution Wet Paint: ", len(part1.painted))


    part2 = Robot(11, 2)
    part2.load(typing=int, sep=",")

    part2.path[(0,0)] = 1 # Set robot to initial white location

    part2.run().visualize()
