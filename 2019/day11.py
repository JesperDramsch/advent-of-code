from util import Robot

if __name__ == "__main__":
    part1 = Robot(11, 1)
    part1.load(typing=int, sep=",")

    part1.time().run().time()
    print("Caution Wet Paint: ", len(part1.painted))

    part2 = Robot(11, 2)
    part2.load(typing=int, sep=",")

    part2.path[(0,0)] = 1 # Set robot to initial white location

    part2.time().run().visualize().time()
