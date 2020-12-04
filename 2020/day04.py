from util import Day
import re


def preprocess(data):
    out = []
    for dat in data.replace("\n\n", "\t").replace("\n", " ").strip().split("\t"):
        # dat = dat.split(" ")
        out.append(dict(x.split(":") for x in dat.split(" ")))
    return out


def validate_keys(row):
    dict_keys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]  # , "cid"
    return None not in [row.get(k) for k in dict_keys]


def validate(row):
    return validate_keys(row) and all(
        [
            1920 <= int(row.get("byr", 0)) <= 2002,
            2010 <= int(row.get("iyr", 0)) <= 2020,
            2020 <= int(row.get("eyr", 0)) <= 2030,
            ((row.get("hgt", "")[-2:] in "cm") and (150 <= int(row.get("hgt", 0)[:-2]) <= 193))
            or ((row.get("hgt", "")[-2:] in "in") and (59 <= int(row.get("hgt", 0)[:-2]) <= 76)),
            bool(re.match("#[0-9a-f]{6}", row.get("hcl", ""))),
            row.get("ecl") in "amb blu brn gry grn hzl oth".split(),
            bool(re.match("^\d{9}$", row.get("pid", ""))),
        ]
    )


def main(day, part=1):
    day.data = preprocess(day.data)
    if part == 1:
        day.apply(validate_keys)
    if part == 2:
        day.apply(validate)
    return sum(day.data)


if __name__ == "__main__":
    day = Day(4)

    day.load(typing=str, process=False)
    print(main(day))

    day.load(typing=str, process=False)
    print(main(day, part=2))
