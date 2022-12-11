import argparse
from pathlib import Path
from datetime import datetime


def create_dirs(number):
    filename = f"day{number:02d}"
    files = (filename + ".py", filename + ".txt", "test_" + filename + ".py")
    dirs = (".", "data", "tests")

    year = get_year()

    for d, f in zip(dirs, files):
        there = Path(d, f)
        if there.exists():
            continue
        template_there = Path("..", ".templates")
        with open(Path(template_there, "day.py"), "r") as fp:
            template_day = fp.read()
        with open(Path(template_there, "test.py"), "r") as fp:
            template_test = fp.read()
        with open(there, "w") as fp:
            if "tests" == d:
                fp.write(template_test.format(number=number, year=year))
            elif "." == d:
                fp.write(template_day.format(number=number))
            else:
                pass


def get_year():
    return Path(__file__).resolve().parent.name


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create Files")
    parser.add_argument("--day", help="Number of day", type=int, default=datetime.now().day, required=False)
    args = parser.parse_args()

    create_dirs(args.day)
