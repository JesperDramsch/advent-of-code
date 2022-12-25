from day import Day
from aocd import submit
from collections import deque


class Tetris:
    def __init__(self, directions):
        self.directions = deque(directions)
        self.width = 7
        self.height = 0
        self.floor = 0
        self.start = 3 + 2j

        self.board = {}
        self._parse_pieces()

        self.seen = dict()
        self.circular = ()

    def _parse_pieces(self):
        raw_pieces = """####

.#.
###
.#.

..#
..#
###

#
#
#
#

##
##""".split(
            "\n\n"
        )
        self.pieces = deque()

        for piece in raw_pieces:
            new_piece = []
            for i, line in enumerate(piece.split("\n")[::-1]):
                for ii, char in enumerate(line):
                    if char == "#":
                        new_piece.append(i + ii * 1j)
            self.pieces.append(tuple(new_piece))

    def __str__(self):
        board = [["+"] + ["-"] * self.width + ["+"]]
        for i in range(self.height):
            board.append(["|"] + ["."] * self.width + ["|"])
        for k, v in self.board.items():
            board[int(k.real)][int(k.imag) + 1] = v
        return "\n".join("".join(row) for row in board[::-1])

    def __repr__(self):
        return str(self)

    def next_piece(self):
        piece = self.pieces.popleft()
        self.pieces.append(piece)
        return {i + self.start + self.height + 1: "#" for i in piece}

    def next_direction(self):
        direction = self.directions.popleft()
        self.directions.append(direction)
        return direction

    def _check_move(self, piece, direction):
        for i in piece.keys():
            new = i + direction
            if new.imag < 0 or new.imag >= self.width or new.real <= self.floor or new in self.board:
                return False
        return True

    def check_tetris(self, piece):
        min_height = int(min([p.real - 1 for p in self.board.keys()]))
        for i in range(self.height, min_height, -1):
            if all([i + ii * 1j in self.board for ii in range(self.width)]):
                self.board = {k: v for k, v in self.board.items() if k.real > i}
                self.floor = i
                break

    def check_circular(self):
        if self.height < 55:
            return
        signature = tuple(k - (self.height + 55) for k, v in self.board.items() if k.real >= self.height - 55)
        piece = tuple(self.pieces)
        directions = tuple(self.directions)
        if (signature, piece, directions) in self.seen:
            self.circular = self.seen[(signature, piece, directions)], (self.turn_counter, self.height)
        self.seen[(signature, piece, directions)] = (self.turn_counter, self.height)

    def _down(self, piece):
        if self._check_move(piece, -1):
            return {i - 1: piece[i] for i in piece.keys()}

    def _left(self, piece):
        if self._check_move(piece, -1j):
            return {i - 1j: piece[i] for i in piece.keys()}

    def _right(self, piece):
        if self._check_move(piece, 1j):
            return {i + 1j: piece[i] for i in piece.keys()}

    def turn(self):
        piece = self.next_piece()
        while True:
            direction = self.next_direction()
            if direction == "<":
                new_piece = self._left(piece)
            elif direction == ">":
                new_piece = self._right(piece)
            if new_piece is not None:
                piece = new_piece
            new_piece = self._down(piece)
            if new_piece is not None:
                piece = new_piece
            else:
                self.board |= piece
                self.height = int(max([self.height] + [p.real for p in piece.keys()]))
                self.check_circular()
                self.check_tetris(piece)
                break

    def game(self, turns):
        self.turn_counter = 0
        height_offset = 0
        while self.turn_counter < turns:
            self.turn()

            if self.circular:
                (i_start, h_start), (i_end, h_end) = self.circular
                cycles = (turns - i_start) // (i_end - i_start)
                height_offset = h_start + cycles * (h_end - h_start) - h_end
                self.turn_counter = i_start + cycles * (i_end - i_start)
                self.circular, self.seen = (), {}
            self.turn_counter += 1
        else:
            self.height += height_offset


def main(day, part=1):
    day.parse_list(sep="")
    board = Tetris(day.data)
    if part == 1:
        turns = 2022
    if part == 2:
        turns = 1_000_000_000_000
    board.game(turns)
    return board.height


if __name__ == "__main__":
    day = Day(17)
    day.download()

    day.load()
    p1 = main(day)
    print(p1)
    submit(p1, part="a", day=17, year=2022)

    day.load()

    p2 = main(day, part=2)
    print(p2)
    submit(p2, part="b", day=17, year=2022)
