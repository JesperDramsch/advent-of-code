from day import Day
from aocd import submit
import re


def parse_data(data):
    output = {}
    for line in data:
        game_id_re = re.compile(r"Game (\d+): .*")
        round_data_re = re.compile(r"(\d+) (\w+)")

        game_id_match = game_id_re.match(line)
        game_id = int(game_id_match.group(1))

        capture = dict(red=0, green=0, blue=0)
        round_data = round_data_re.findall(line)
        for num, color in round_data:
            capture[color] = max(capture.get(color, 0), int(num))
        output[game_id] = capture
    return output


def inspect_data(game_data):
    # only 12 red cubes, 13 green cubes, and 14 blue cubes?
    maximum = dict(red=12, green=13, blue=14)
    valid_ids = set()
    for game_id, colors in game_data.items():
        if all(game_data[game_id][color] <= maximum[color] for color in colors.keys()):
            valid_ids.add(game_id)
    return valid_ids


def find_minimum(game_data):
    output = {}
    for game_id, colors in game_data.items():
        minimum = dict(red=0, green=0, blue=0)
        for color, maximum in colors.items():
            minimum[color] = max(minimum[color], maximum)
        output[game_id] = minimum
    return output


def calculate_power(scores):
    output = []
    for score in scores.values():
        output.append(score["red"] * score["green"] * score["blue"])
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
