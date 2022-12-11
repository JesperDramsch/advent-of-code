from day import Day
from aocd import submit

from collections import deque

class Monkey:
    def __init__(self, text, part=1):
        self.number = int(text[0].split(" ")[1][:-1])
        
        for line in text[1:]:
            if "Starting items" in line:
                starting_items = deque(int(x) for x in line.split(": ")[1].split(", "))
            elif "Operation" in line:
                self.operation = line.split(": ")[1]
            elif "If true" in line:
                self.if_true = int(line.split(" ")[-1])
            elif "If false" in line:
                self.if_false = int(line.split(" ")[-1])
            elif "Test: divisible by" in line:
                self.test_value = int(line.split(" ")[-1])
            else:
                pass
        
        self.items = starting_items
        self.inspect_counter = 0
        self.part = part
        self.max_mod = None

    def __repr__(self):
        return f"Monkey {self.number}: {self.items}"

    def __str__(self):
        return f"Monkey {self.number}: {self.items}"

    def __eq__(self, other):
        return self.number == other.number

    def worry(self, item):
        operation = self.operation.replace("old", "{old}").format(old=item)
        match operation.split(" "):
            case _, "=", left, "*", right:
                return int(left) * int(right)
            case _, "=", left, "+", right:
                return int(left) + int(right)

    def turn(self):
        throw_items = []
        while self.items:
            self.inspect_counter += 1
            # Inspect item
            item = self.items.popleft()

            ## Operation
            item = self.worry(item)

            if self.part == 1:
                ## Relief
                item //= 3
            item %= self.max_mod

            # Test item
            if item % self.test_value == 0:
                # If true
                throw_items.append((self.if_true, item))

            else:
                # If false
                throw_items.append((self.if_false, item))
        return throw_items


def single_round(day):
    for i in range(len(day.data)):
        throw_items = day.data[i].turn()
        for monkey, item in throw_items:
            day.data[monkey].items.append(item)
    return day

def monkey_business(day):
    counts = sorted(x.inspect_counter for x in day.data)[-2:]
    return counts[1] * counts[0]


def main(day, part=1):
    day.parse_list_of_lists()
    day.apply(Monkey, part=part)
    max_mod = 1
    for monkey in day.data:
        max_mod *= monkey.test_value
    for i in range(len(day.data)):
        day.data[i].max_mod = max_mod
    rounds = 20 if part == 1 else 10_000
    for _ in range(rounds):
        day = single_round(day)
    return monkey_business(day)

if __name__ == "__main__":
    day = Day(11)
    day.download()


    day.load()
    p1 = main(day)
    print(p1)
    submit(p1, part="a", day=11, year=2022)

    day.load()
    p2 = main(day, part=2)
    print(p2)
    submit(p2, part="b", day=11, year=2022)
