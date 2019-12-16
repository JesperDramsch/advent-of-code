import time
import sys, os
from util import Day

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


class Arcade(Day):
    def __init__(self, day, part):
        super().__init__(day, part)
        self.concurrent = True
        self.score = 0
        
        
    def paint(self):
        self.canvas = {}
        self.ball_x = 0
        self.paddle_x = 0

        while True:
            x = self.execute_opcode(reset_pointer=False)
            y = self.execute_opcode(reset_pointer=False)
            z = self.execute_opcode(reset_pointer=False)

            if z == 4:
                self.ball_x = x
                self.input(-1 if self.ball_x < self.paddle_x else 1 if self.ball_x > self.paddle_x else 0)
            if z == 3:
                self.paddle_x = x

            if isinstance(z, Day):
                break
            if x == -1 and y == 0:
                #print("Score: ", z)
                self.score = z
                self.visualize()
            else:
                self.canvas[(x, y)] = z
                if len(self.canvas.keys()) > 910:
                    self.visualize()
        return self
    def visualize(self):

        print("Score: ", self.score)
        #x, y = zip(*self.canvas.keys())
        #painting = {0: " ", 1: "░", 2: "▒", 3: "▉", 4: "◓"}
        #for j in range(min(y)-2, max(y)+1):
        #    for i in range(min(x), max(x)+1):
        # for j in range(0, 25):
        #     for i in range(0, 45):
        #         sys.stdout.write(painting[self.canvas.get((i, j), 0)])
        #     sys.stdout.write("\n")
        return self


if __name__ == "__main__":
    # part1 = Day(13, 1)

    # part1.load(typing=int, sep=",")

    # part1.concurrent = True

    # canvas = paint(part1)

    # print(sum([int(x == 2) for x in canvas.values()]))

    part2 = Arcade(13, 2)

    part2.load(typing=int, sep=",")

    part2.data[0] = 2
    part2.bake()
    part2.mem_load()
    
    part2.paint()
    #part2.visualize()

    print(part2.score)

    # x, y = zip(*self.path.keys())

    # 0 is an empty tile. No game object appears in this tile.
    # 1 is a wall tile. Walls are indestructible barriers.
    # 2 is a block tile. Blocks can be broken by the ball.
    # 3 is a horizontal paddle tile. The paddle is indestructible.
    # 4 is a ball tile. The ball moves diagonally and bounces off objects.

    fig = plt.figure()


    def f(x, y):
        return np.sin(x) + np.cos(y)

    x = np.linspace(0, 2 * np.pi, 120)
    y = np.linspace(0, 2 * np.pi, 100).reshape(-1, 1)
    # ims is a list of lists, each row is a list of artists to draw in the
    # current frame; here we are just animating one artist, the image, in
    # each frame
    ims = []
    for i in range(60):
        x += np.pi / 15.
        y += np.pi / 20.
        im = plt.imshow(f(x, y), animated=True)
        ims.append([im])

    ani = animation.ArtistAnimation(fig, ims, interval=50, blit=True,
                                    repeat_delay=1000)

    # ani.save('dynamic_images.mp4')

    plt.show()