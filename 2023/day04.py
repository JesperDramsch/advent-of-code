from day import Day
from aocd import submit
from functools import cached_property


class Card:
    def __init__(self, data):
        self.mine, self.winning = data.split(":")[1].split(" | ")
        self._parse_numbers()

    def _parse_numbers(self):
        self.mine = set(int(x) for x in self.mine.split())
        self.winning = set(int(x) for x in self.winning.split())

    @cached_property
    def winning_score(self):
        return int(2 ** (len(set.intersection(self.mine, self.winning)) - 1))


class Pile:
    def __init__(self, data):
        self.cards = [Card(card) for card in data]

    def winning_score(self):
        return sum(card.winning_score for card in self.cards)


def main(day, part=1):
    cards = Pile(day.data)
    if part == 1:
        return cards.winning_score()
    if part == 2:
        pass


if __name__ == "__main__":
    day = Day(4)
    day.download()

    day.load()
    p1 = main(day)
    print(p1)
    submit(p1, part="a", day=4, year=2023)

    # day.load()
    # p2 = main(day, part=2)
    # print(p2)
    # submit(p2, part="b", day=4, year=2023)
