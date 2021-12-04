from util import Day
from aocd import submit
import numpy as np


def parse_input(input_str):
    # First line is the draw sequence
    draw_sequence = input_str.pop(0).split(",")
    draw_sequence = [int(x) for x in draw_sequence]

    # Open array for boards (empty space still present) [boards x 5 x 5]
    boards = np.zeros(((len(input_str) + 1) // 6, 5, 5), dtype=int)

    # Iterate through boards, ignore empty strings
    for i, line in enumerate(filter(len, input_str)):
        # Slice up lines into 5x5 arrays
        line = [int(line[ii : ii + 3]) for ii in range(0, len(line), 3)]
        boards[i // 5, i % 5, :] = line

    return draw_sequence, boards


def check_bingo(boards):
    # Check columns
    cols = np.where(np.sum(boards, axis=1) == -5)
    # Check rows
    rows = np.where(np.sum(boards, axis=2) == -5)

    if cols[0].size > 0:
        return cols[0]
    if rows[0].size > 0:
        return rows[0]


def find_winning_board(draw_sequence, boards, position=1):
    winner_sequence = []
    # Iterate through draw sequence
    for draw in draw_sequence:
        # Mark the board
        boards[boards == draw] = -1

        # Check if there is a winner
        winner = check_bingo(boards)

        # If there is a winner
        if winner is not None:
            # Add the winner to the winner sequence
            # Sometimes multiple columns and rows win at the same time, so dedupe those
            winner_sequence.extend(set(winner))

            # If we are at the end of the sequence, return the winner
            if len(winner_sequence) == position:
                winning_board = boards[winner_sequence[-1], ...]
                return draw, winning_board

            # Reset the winning boards
            for i in winner:
                boards[i, ...] = -999


def main(day, part=1):
    draw_sequence, boards = parse_input(day.data)
    if part == 1:
        # Find the first winning board
        draw, board = find_winning_board(draw_sequence, boards)
    if part == 2:
        # Find the last winning board
        draw, board = find_winning_board(draw_sequence, boards, boards.shape[0])

    # Set marks to zero for sum
    board[board == -1] = 0
    return np.sum(board) * draw


if __name__ == "__main__":
    day = Day(4)
    day.download()

    day.load(typing=str)
    p1 = main(day)
    print(p1)
    submit(p1, part="a", day=4, year=2021)

    day.load(typing=str)
    p2 = main(day, part=2)
    print(p2)
    submit(p2, part="b", day=4, year=2021)
