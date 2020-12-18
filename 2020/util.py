import argparse
from pathlib import Path
from functools import partial


class Day:
    def __init__(self, day: int):

        self.day = day
        self.data = []

        self.debug = False

    def load(
        self, data: list = None, typing: type = int, sep: str = "\n", path: str = None, process: bool = True
    ) -> list:
        """Loads Data for Problem
        File _must_ be named dayXX.txt
        Returns data and makes it available as attribte "data"

        Args:
            data (list, optional):Load computed data not from file. Defaults to None.
            typing (type, optional): Type of data in list . Defaults to int.
            sep (str, optional): Separator in input data. Defaults to "\n".
            path (str, optional): Path to data file. Defaults to None.
            process (bool, optional): [description]. Defaults t

        Returns:
            list:  Data for Problem
        """
        if path is None:
            path = f"data/day{self.day:02d}.txt"
        if data is not None:
            self.data = data
        else:
            with open(path) as f:
                self.data = f.read()

        if process:
            self.data = list(map(typing, self.data.strip().split(sep)))

        return self

    def apply(self, func, *args, **kwargs) -> list:
        """Apply a function to every element.
        Changes the original data.

        Args:
            func (function): Function to apply to every element in input

        Returns:
            list: Function applied to every element in input
        """

        mapfunc = partial(func, *args, **kwargs)
        self.data = list(map(mapfunc, self.data))
        return self

    def download(self):
        from aocd import get_data

        loc = Path("data", f"day{self.day:02d}.txt")
        with open(loc, "w") as fp:
            fp.write(get_data(day=self.day))


def create_dirs(number):
    filename = f"day{number:02d}"
    files = (filename + ".py", filename + ".txt", filename + ".txt", "test_" + filename + ".py")
    dirs = (".", "desc", "data", "tests")

    for d, f in zip(dirs, files):
        there = Path(d, f)
        if there.exists():
            continue
        with open(there, "w") as fp:
            if "tests" == d:
                fp.write(
                    f'import sys\nimport pytest\n\nsys.path.insert(0, ".")\nfrom util import Day\nfrom day{number:02d} import *\n\n@pytest.fixture(scope="function")\ndef example():\n    day = Day({number})\n    data = """"""\n\n    day.load(data, typing=str)\n    return day\n\n@pytest.fixture(scope="function")\ndef day():\n    day = Day({number})\n    day.load(typing=str)\n    return day\n\ndef test_example(example):\n    assert main(example, part=1) == False\n\ndef test_example_p2(example):\n    assert main(example, part=2) == False\n\ndef test_part1(day):\n    assert main(day, part=1) == False\n\ndef test_part2(day):\n    assert main(day, part=2) == False\n'
                )
            elif "." == d:
                fp.write(
                    f'from util import Day\nfrom aocd import submit\n\ndef main(day, part=1):\n    if part == 1:\n        pass\n    if part == 2:\n        pass\n\nif __name__ == "__main__":\n    day = Day({number})\n    day.download()\n\n    day.load(typing=str)\n    p1 = main(day)\n    print(p1)\n    # submit(p1, part="a", day={number}, year=2020)\n\n    # day.load(typing=str)\n    # p2 = main(day, part=2)\n    # print(p2)\n    # submit(p2, part="b", day={number}, year=2020)\n'
                )
            else:
                pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create Files")
    parser.add_argument("day", help="Number of day", type=int)
    args = parser.parse_args()

    create_dirs(args.day)
