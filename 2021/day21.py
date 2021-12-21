from util import Day
from aocd import submit
from itertools import product
from functools import lru_cache


def parse_player(data):
    player1 = int(data[0].split(":")[1].strip()) - 1
    player2 = int(data[1].split(":")[1].strip()) - 1
    return player1, player2


def deterministic_dice_pawn(player1_pos, player2_pos):
    i = 0
    turns = 0
    p1_turn = True
    player1_score, player2_score = 0, 0
    while player1_score < 1000 and player2_score < 1000:
        dice_roll = 0
        for _ in range(3):
            turns += 1
            i += 1
            if i > 100:
                i = 1
            dice_roll += i
        if p1_turn:
            player1_pos = (player1_pos + dice_roll) % 10
            player1_score += player1_pos + 1
        else:
            player2_pos = (player2_pos + dice_roll) % 10
            player2_score += player2_pos + 1
        p1_turn = not p1_turn
    return turns * player1_score if p1_turn else turns * player2_score

@lru_cache(maxsize=None)
def dirac_dice_pawn(player1_pos, player2_pos, player1_score=0, player2_score=0):

    if player1_score >= 21:
        return 1, 0
    if player2_score >= 21:
        return 0, 1

    player1_wins, player2_wins = 0, 0
    for dice_roll in product([1, 2, 3], repeat=3):
        player_pos_new = (player1_pos + sum(dice_roll)) % 10
        player_score_new = player1_score + player_pos_new + 1
        
        player2_win, player1_win = dirac_dice_pawn(player2_pos, player_pos_new, player2_score, player_score_new)
        player1_wins, player2_wins = player1_wins + player1_win, player2_wins + player2_win
    return player1_wins, player2_wins


def main(day, part=1):
    player1, player2 = parse_player(day.data)
    if part == 1:
        return deterministic_dice_pawn(player1, player2)
    if part == 2:
        return max(dirac_dice_pawn(player1, player2))


if __name__ == "__main__":
    day = Day(21)
    day.download()

    day.load(typing=str)
    p1 = main(day)
    print(p1)
    submit(p1, part="a", day=21, year=2021)

    day.load(typing=str)
    p2 = main(day, part=2)
    print(p2)
    submit(p2, part="b", day=21, year=2021)
