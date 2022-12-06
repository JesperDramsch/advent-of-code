from util import Day
from aocd import submit


def winner(player):
    return {"scissors": "paper", "paper": "rock", "rock": "scissors"}[player]


def winner_points(outcome):
    return {"win": 6, "draw": 3, "lose": 0}[outcome]


def selection_points(player):
    return {"rock": 1, "paper": 2, "scissors": 3}[player]


def decode(data, part=1):
    player1, player2 = data.split(" ")

    code1 = {"A": "rock", "B": "paper", "C": "scissors"}
    if part == 1:
        code2 = {"X": "rock", "Y": "paper", "Z": "scissors"}
    elif part == 2:
        code2 = {"X": "lose", "Y": "draw", "Z": "win"}

    return code1[player1], code2[player2]


def faceoff(player1, player2):
    if winner(player2) == player1:
        return winner_points("win")
    elif player1 == player2:
        return winner_points("draw")
    else:
        return winner_points("lose")


def strategic_play(player, outcome):
    if outcome == "win":
        play = winner(winner(player))
    elif outcome == "draw":
        play = player
    elif outcome == "lose":
        play = winner(player)
    return play


def main(day, part=1):
    day.data = (decode(line, part=part) for line in day.data)
    if part == 1:
        return sum(faceoff(*line) + selection_points(line[1]) for line in day.data)
    if part == 2:
        return sum(selection_points(strategic_play(*line)) + winner_points(line[1]) for line in day.data)


if __name__ == "__main__":
    day = Day(2)
    day.download()

    day.load(typing=str)

    p1 = main(day)
    print(p1)
    submit(p1, part="a", day=2, year=2022)

    day.load(typing=str)

    p2 = main(day, part=2)
    print(p2)
    submit(p2, part="b", day=2, year=2022)
