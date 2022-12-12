import argparse
from pathlib import Path
from datetime import datetime


def create_dirs(number, year):
    filename = f"day{number:02d}"
    files = (filename + ".py", filename + ".txt", "test_" + filename + ".py")
    dirs = (".", "data", "tests")

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
                fp.write(template_test.format(number=number))
            elif "." == d:
                fp.write(template_day.format(number=number, year=year))
            else:
                pass

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create Files")
    parser.add_argument("--day", help="Number of day", type=int, default=datetime.now().day, required=False)
    parser.add_argument("--year", help="Number of year", type=int, default=datetime.now().year, required=False)
    args = parser.parse_args()

    create_dirs(args.day, args.year)
