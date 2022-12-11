from day import Day
from aocd import submit


class TwoWayDict(dict):
    """Two-way dictionary"""

    def __init__(self, dictionary=None):
        if dictionary is not None:
            self.from_dict(dictionary)

    def __setitem__(self, key, value):
        # Remove any previous connections with these values
        if key in self:
            del self[key]
        if value in self:
            del self[value]
        dict.__setitem__(self, key, value)
        dict.__setitem__(self, value, key)

    def __delitem__(self, key):
        dict.__delitem__(self, self[key])
        dict.__delitem__(self, key)

    def __len__(self):
        return dict.__len__(self) // 2

    def from_dict(self, dictionary):
        for key, value in dictionary.items():
            self[key] = value


def decode(data, part=1):
    player1, player2 = data.split(" ")

    code1 = {"A": "rock", "B": "paper", "C": "scissors"}
    if part == 1:
        code2 = {"X": "rock", "Y": "paper", "Z": "scissors"}
    elif part == 2:
        code2 = {"X": "lose", "Y": "draw", "Z": "win"}

    return code1[player1], code2[player2]


def winner(player):
    return {"scissors": "paper", "paper": "rock", "rock": "scissors"}[player]


def winner_points(outcome):
    return {"win": 6, "draw": 3, "lose": 0}[outcome]


def selection_points(player):
    return {"rock": 1, "paper": 2, "scissors": 3}[player]


def game(opponent, result):
    return TwoWayDict({opponent: "draw", winner(opponent): "lose", winner(winner(opponent)): "win"})[result]


def main(day, part=1):
    day.parse_list()
    day.data = (decode(line, part=part) for line in day.data)
    if part == 1:
        return sum(selection_points(line[1]) + winner_points(game(*line)) for line in day.data)
    if part == 2:
        return sum(selection_points(game(*line)) + winner_points(line[1]) for line in day.data)


if __name__ == "__main__":
    day = Day(2)
    day.download()

    day.load()
    
    p1 = main(day)
    print(p1)
    submit(p1, part="a", day=2, year=2022)

    day.load()

    p2 = main(day, part=2)
    print(p2)
    submit(p2, part="b", day=2, year=2022)
