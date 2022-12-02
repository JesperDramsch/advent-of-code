from util import Day
from aocd import submit

def winner(player1, player2):
    winner = {"scissors": "paper", "paper": "rock", "rock": "scissors"}
    if winner[player1] == player2:
        return winner_points("win")
    elif player1 == player2:
        return winner_points("draw")
    else:
        return winner_points("lose")

def winner_points(outcome):
    return {"win": 6, "draw": 3, "lose": 0}[outcome]
    
def selection_points(player1):
    return {"rock": 1, "paper": 2, "scissors": 3}[player1]
    
def decode_part1(data):
    player1, player2 = data.split(" ")

    code1 = {"A": "rock", "B": "paper", "C": "scissors"}
    code2 = {"X": "rock", "Y": "paper", "Z": "scissors"}

    return code2[player2], code1[player1]

def decode_part2(data):
    player1, outcome = data.split(" ")

    code1 = {"A": "rock", "B": "paper", "C": "scissors"}
    code2 = {"X": "lose", "Y": "draw", "Z": "win"}

    winner = {"scissors": "paper", "paper": "rock", "rock": "scissors"}
    if code2[outcome] == "win":
        play = winner[winner[code1[player1]]]
    elif code2[outcome] == "draw":
        play = code1[player1]
    elif code2[outcome] == "lose":
        play = winner[code1[player1]]

    return play, code2[outcome]

def main(day, part=1):
    if part == 1:
        day.data = (decode_part1(line) for line in day.data)
        return sum(winner(*line) + selection_points(line[0]) for line in day.data)
    if part == 2:
        day.data = (decode_part2(line) for line in day.data)
        return sum(winner_points(line[1]) + selection_points(line[0]) for line in day.data)

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
