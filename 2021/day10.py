from util import Day
from aocd import submit
from collections import deque
from statistics import median

pairs = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">",
}


def score_syntax_error(corrupted):
    points = {
        ")": 3,
        "]": 57,
        "}": 1197,
        ">": 25137,
    }
    score = 0
    for c in corrupted:
        score += points[c]
    return score


def score_autocomplete(incomplete):
    """Median score of autocomplete."""
    # Points for each character (open to save lookup)
    points = {
        "(": 1,
        "[": 2,
        "{": 3,
        "<": 4,
    }
    scores = []
    for line in incomplete:
        score = 0
        for c in line:
            score *= 5
            score += points[c]
        scores.append(score)
    return median(scores)


def process_syntax(data):
    """Separate lines into corrupted and incomplete."""
    corrupted = deque()
    incomplete = deque()
    # Split data into lines
    for line in data:
        # Reset deque
        last = deque()
        # Split line into characters
        for char in line:
            # If character is an opener bracket, add to deque
            if char in pairs.keys():
                last.appendleft(char)
            else:
                # If character is a closer bracket, check if it matches last opener
                if char == pairs[last[0]]:
                    # If it matches, pop last opener
                    last.popleft()
                else:
                    # If it doesn't match, add to corrupted and skip line
                    corrupted.appendleft(char)
                    break
        else:
            # If line is uncorrupted, add to incomplete
            incomplete.append(last)
    return corrupted, incomplete


def main(day, part=1):
    corrupt, incomplete = process_syntax(day.data)
    if part == 1:
        return score_syntax_error(corrupt)
    if part == 2:
        return score_autocomplete(incomplete)


if __name__ == "__main__":
    day = Day(10)
    day.download()

    day.load(typing=str)
    p1 = main(day)
    print(p1)
    submit(p1, part="a", day=10, year=2021)

    day.load(typing=str)
    p2 = main(day, part=2)
    print(p2)
    submit(p2, part="b", day=10, year=2021)
