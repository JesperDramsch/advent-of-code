from day import Day
from aocd import submit
import re


def parse_data(data):
    output = {}
    for line in data:
        game_id_re = re.compile(r"Game (\d+): (.*)")
        round_data_re = re.compile(r"(\d+) (\w+)")

        game_id_match = game_id_re.match(line)
        game_id = int(game_id_match.group(1))
        game_data = game_id_match.group(2)

        capture = []
        for game in game_data.split("; "):
            round_data = round_data_re.findall(game)
            round_data = {color: int(num) for num, color in round_data}
            capture.append(round_data)
        output[game_id] = capture
    return output


def inspect_data(game_data):
    # only 12 red cubes, 13 green cubes, and 14 blue cubes?
    maximum = dict(red=12, green=13, blue=14)
    valid_ids = set(game_data.keys())
    for game_id, rounds in game_data.items():
        for round in rounds:
            if any(round[color] > maximum[color] for color in round):
                valid_ids.remove(game_id)
                break
    return valid_ids


def find_minimum(game_data):
    output = {}
    for game_id, rounds in game_data.items():
        minimum = dict(red=0, green=0, blue=0)
        for round in rounds:
            for color in round:
                minimum[color] = max(minimum[color], round[color])
        output[game_id] = minimum
    return output


def calculate_power(scores):
    output = []
    for score in scores.values():
        output.append(score.get("red", 0) * score.get("green", 0) * score.get("blue", 0))
    return output


def main(day, part=1):
    data = parse_data(day.data)
    if part == 1:
        valid_ids = inspect_data(data)
        return sum(valid_ids)
    if part == 2:
        minimal = find_minimum(data)
        return sum(calculate_power(minimal))


if __name__ == "__main__":
    day = Day(2)
    day.download()

    day.load(typing=str)

    p1 = main(day)
    print(p1)
    submit(p1, part="a", day=2, year=2023)

    day.load(typing=str)

    day.load(typing=str)
    p2 = main(day, part=2)
    print(p2)
    submit(p2, part="b", day=2, year=2023)
