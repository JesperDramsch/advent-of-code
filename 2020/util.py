import argparse
from pathlib import Path
from functools import partial


class Day:
    def __init__(self, day: int):

        self.day = day
        self.data = []

        self.debug = False

    def load(self, data: list = None, typing: type = int, sep: str = "\n", path: str = None) -> list:
        """Loads Data for Problem
        File _must_ be named dayXX.txt
        Returns data and makes it available as attribte "data"

        Args:
            data (list, optional):Load computed data not from file. Defaults to None.
            typing (type, optional): Type of data in list . Defaults to int.
            sep (str, optional): Separator in input data. Defaults to "\n".
            path (str, optional): Path to data file. Defaults to None.

        Returns:
            list:  Data for Problem
        """

        if path is None:
            path = f"data/day{self.day:02d}.txt"
        if data is not None:
            self.data = data
        else:
            with open(path) as f:
                data = f.read().strip().split(sep)
            self.data = list(map(typing, data))
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


def create_dirs(number):
    filename = f"day{number:02d}"
    files = [x for x in (filename+".py", filename +
                         ".txt", "test_"+filename+".py")]
    dirs = [".", "desc", "tests"]

    for d, f in zip(dirs, files):
        with open(Path(d, f), 'w') as fp:
            pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Create Files')
    parser.add_argument('day', help='Number of day', type=int)
    args = parser.parse_args()

    create_dirs(args.day)
