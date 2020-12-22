from util import Day
from aocd import submit
from collections import deque
from itertools import islice


def preprocess(data):
    out = []
    for q in data.split("\n\n"):
        q = q.split("\n")[1:]
        out.append(deque(map(int, q)))
    return tuple(out)


def cömbät(player1, player2):
    while player1 and player2:
        c1 = player1.popleft()
        c2 = player2.popleft()
        if c1 > c2:
            player1.append(c1)
            player1.append(c2)
        else:
            player2.append(c2)
            player2.append(c1)
    return player1, player2


def recürsive_cömbät(player1, player2):
    # print("\nGame time!")
    deck_tracker_p1 = set()
    deck_tracker_p2 = set()
    while player1 and player2:
        # print("Round", i := i + 1)
        q1 = False
        q2 = False

        # print("Player 1: ", player1)
        # print("Player 2: ", player2)

        if tuple(player1) in deck_tracker_p1 and tuple(player2) in deck_tracker_p2:
            # Player 1 wins by recursion default
            return player1, None
        deck_tracker_p1.add(tuple(player1))
        deck_tracker_p2.add(tuple(player2))

        card1 = player1.popleft()
        card2 = player2.popleft()

        if card1 <= len(player1) and card2 <= len(player2):
            # Recürsive Cömbät!
            # print("Recürsiön")
            q1, q2 = recürsive_cömbät(deque(islice(player1, 0, card1)), deque(islice(player2, 0, card2)))
            if q2 is None:
                q1 = True
        else:
            q1 = card1 > card2
            q2 = card1 < card2

        if q1:
            player1.append(card1)
            player1.append(card2)
        elif q2:
            player2.append(card2)
            player2.append(card1)
    return player1, player2


def score(deck):
    return sum([(i + 1) * v for i, v in enumerate(reversed(deck))])


def main(day, part=1):
    day.data = preprocess(day.data)
    if part == 1:
        game = cömbät(*day.data)
    if part == 2:
        game = recürsive_cömbät(*day.data)
        print(game)
    out = score(game[game[0] == deque()])
    return out


if __name__ == "__main__":
    day = Day(22)
    day.download()

    data = """Player 1:
9
2
6
3
1

Player 2:
5
8
4
7
10"""

#     data = """Player 1:
# 43
# 19

# Player 2:
# 2
# 29
# 14"""

    day.load(process=False)
    p1 = main(day)
    print(p1)
    submit(p1, part="a", day=22, year=2020)

    day.load(process=False)
    p2 = main(day, part=2)
    print(p2)
    submit(p2, part="b", day=22, year=2020)
