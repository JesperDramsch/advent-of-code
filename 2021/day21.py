from util import Day
from aocd import submit

def parse_player(data):
    player1 = int(data[0].split(":")[1].strip())
    player2 = int(data[1].split(":")[1].strip())
    return player1, player2

def new_position(position, dice_roll):
    x = position + dice_roll
    while x > 10:
        x -= 10
    return x

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
            player1_pos = new_position(player1_pos, dice_roll)
            player1_score += player1_pos
        else:
            player2_pos = new_position(player2_pos, dice_roll)
            player2_score += player2_pos
        p1_turn = not p1_turn
    return turns * player1_score if p1_turn else turns * player2_score


def main(day, part=1):
    player1, player2 = parse_player(day.data)
    if part == 1:
        return deterministic_dice_pawn(player1, player2)
    if part == 2:
        pass

if __name__ == "__main__":
    day = Day(21)
    day.download()

    day.load(typing=str)
    p1 = main(day)
    print(p1)
    submit(p1, part="a", day=21, year=2021)

    # day.load(typing=str)
    # p2 = main(day, part=2)
    # print(p2)
    # submit(p2, part="b", day=21, year=2021)
