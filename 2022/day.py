import argparse
from pathlib import Path
from functools import partial
import os, sys

from utils.parser import Parser

class Day(Parser):
    def __init__(self, day: int):

        self.day = day
        self.data = []

        self.debug = False

    def load(
        self, data: list = None, path: str = None, strip: bool = True) -> list:
        """Loads Data for Problem
        File _must_ be named dayXX.txt
        Returns data and makes it available as attribute "data"

        Args:
            data (list, optional):Load computed data not from file. Defaults to None.
            path (str, optional): Path to data file. Defaults to None.
            strip (bool, optional): Strip data. Defaults to True.

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

        if strip:
            self.data = self.data.strip()

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
        try:
            self.data = list(map(mapfunc, self.data))
        except TypeError:
            self.data = [list(map(mapfunc, x)) for x in self.data]
        return self

    def download(self):
        from aocd import get_data

        loc = Path("data", f"day{self.day:02d}.txt")
        with open(loc, "w") as fp:
            fp.write(get_data(day=self.day))
