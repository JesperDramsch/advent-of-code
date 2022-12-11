import argparse
from pathlib import Path
from functools import partial
import os


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
