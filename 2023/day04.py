from day import Day
from aocd import submit
from functools import cached_property


class Card:
    def __init__(self, data):
        self.tickets = 1
        self.mine, self.winning = data.split(":")[1].split(" | ")
        self._parse_numbers()

    def _parse_numbers(self):
        self.mine = set(int(x) for x in self.mine.split())
        self.winning = set(int(x) for x in self.winning.split())

    @cached_property
    def num_winning_numbers(self):
        return len(set.intersection(self.mine, self.winning))

    @cached_property
    def winning_score(self):
        return int(2 ** (self.num_winning_numbers - 1))


class Pile:
    def __init__(self, data):
        self.cards = [Card(card) for card in data[::-1]]

    def winning_score(self):
        return sum(card.winning_score for card in self.cards)

    def multiplying_cards(self):
        for i in range(len(self.cards)):
            this_extra_tickets = max(0, i - self.cards[i].num_winning_numbers)
            for ii in range(this_extra_tickets, i):
                self.cards[i].tickets += self.cards[ii].tickets


def main(day, part=1):
    pile = Pile(day.data)
    if part == 1:
        return pile.winning_score()
    if part == 2:
        pile.multiplying_cards()
        return sum(card.tickets for card in pile.cards)


if __name__ == "__main__":
    day = Day(4)
    day.download()

    day.load()
    p1 = main(day)
    print(p1)
    submit(p1, part="a", day=4, year=2023)

    day.load()
    p2 = main(day, part=2)
    print(p2)
    submit(p2, part="b", day=4, year=2023)
