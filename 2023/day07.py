from day import Day
from aocd import submit
from collections import Counter

import functools


@functools.total_ordering
class Hand:
    def __init__(self, hand, bid):
        self.hand = hand
        self.bid = int(bid)
        self._matches = Counter(hand)
        self.order = "AKQJT98765432"

    @functools.cached_property
    def matches(self):
        m = self._matches.most_common(2)
        if len(m) == 1:
            return m[0][1], 0
        return m[0][1], m[1][1]

    def __eq__(self, other):
        return self.matches == other.matches and self.hand == other.hand

    def __gt__(self, other):
        if self.matches[0] == other.matches[0]:
            if self.matches[1] == other.matches[1]:
                for i in range(len(self.hand)):
                    card1, card2 = self.order.index(self.hand[i]), self.order.index(other.hand[i])
                    if card1 < card2:
                        return True
                    if card1 > card2:
                        return False
            if self.matches[1] > other.matches[1]:
                return True
            return False
        return self.matches[0] > other.matches[0]

    def __repr__(self):
        return f"{self.hand} {self.bid}"


class JokerHand(Hand):
    def __init__(self, hand, bid):
        super().__init__(hand, bid)
        self.order = "AKQT98765432J"
        self.add_jokers()

    def add_jokers(self):
        if "J" not in self._matches:
            return
        if self._matches["J"] == 5:
            return
        jokers = self._matches.pop("J")
        top = self._matches.most_common(1)[0][0]
        self._matches[top] += jokers


def main(day, part=1):
    if part == 1:
        game = [Hand(*line.split(" ")) for line in day.data]
    if part == 2:
        game = [JokerHand(*line.split(" ")) for line in day.data]

    return sum(i * hand.bid for i, hand in enumerate(sorted(game), start=1))


if __name__ == "__main__":
    day = Day(7)
    day.download()

    day.load()
    p1 = main(day)
    print(p1)
    submit(p1, part="a", day=7, year=2023)

    day.load()
    p2 = main(day, part=2)
    print(p2)
    submit(p2, part="b", day=7, year=2023)
