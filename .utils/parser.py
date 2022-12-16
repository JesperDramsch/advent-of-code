from typing import Union, Iterable, Tuple, List, Dict, Any, Callable, Optional
import re
class Parser:
    def __init__(self, data: str):
        self.data = data

    def parse_list(self, sep: str = "\n", typing: Union[Iterable[type], type] = str) -> list:
        """Parse into list of type

        Parameters
        ----------
        sep : str, optional
            Separator in input data, by default "\n"
        typing : type, optional
            Type of data in list, by default int
        """
        self.data = self.split(self.data, sep=sep)
        self.data = self.apply_type(self.data, typing=typing)


    def parse_list_of_lists(self, sep: str = "\n\n", sep2: str = "\n", typing: Union[Iterable[type], type] = str) -> list:
        """Parse into list of lists of type

        Parameters
        ----------
        sep : str, optional
            Separator of groups, by default "\n\n"
        sep2 : str, optional
            Separator inside of groups, by default "\n"
        typing : type, optional
            type of items in groups, by default str
        """
        self.parse_list(sep = sep, typing = str)
        self.data = [self.apply_type(self.split(line, sep2), typing=typing) for line in self.data]

    def parse_regex(self, regex: str, typing: Union[Iterable[type], type] = str) -> list:
        """Parse data using regex

        Parameters
        ----------
        regex : str
            Regex to use
        typing : type, optional
            Type of data in list, by default str
        """
        self.data = re.findall(regex, self.data)
        self.data = self.apply_type(self.data, typing=typing)

    @staticmethod
    def split(data, sep: str = "\n") -> list:
        """Split data into list even if sep is empty"""
        if sep:
            return data.split(sep)
        else:
            return [x for x in data]


    @staticmethod
    def apply_type(data, typing: Union[Iterable[type], type] = str) -> list:
        """Apply a type to every element in iterable.

        Args:
            data (Iterable): Iterable with data to apply type to
            typing (type): Type to apply to every element in iterable

        Returns:
            Iterable: Type applied to every element in input
        """
        # Extract and apply same type to iterable
        iter_typing = type(data)
        if type(typing) == type:
            try:
                changed = iter_typing(typing(x) for x in data)
            except TypeError:
                iteriter_typing = type(data[0])
                changed = iter_typing(iteriter_typing(typing(x) for x in y) for y in data)
        else:
            if len(typing) != len(data):
                print(typing, data)
                raise IndexError("Length of typing and data not equal")
            changed = (types(x) for types, x in zip(typing, data))
        return iter_typing(changed)


class ParserMap:
    def __init__(self, n: str = None, ne: str = None, e: str = None, se: str = None, s: str = None, sw: str = None, w: str = None, nw: str = None):

        directions = {
            "n": 1 + 0j,
            "ne": 1 + 1j,
            "e": 1j,
            "se": -1 + 1j,
            "s": -1,
            "sw": -1 - 1j,
            "w": -1j,
            "nw": 1 - 1j,
        }

        self.cardinals = {}

        if n is not None:
            self.cardinals[n] = directions["n"]
        elif ne is not None:
            self.cardinals[ne] = directions["ne"]
        elif e is not None:
            self.cardinals[e] = directions["e"]
        elif se is not None:
            self.cardinals[se] = directions["se"]
        elif s is not None:
            self.cardinals[s] = directions["s"]
        elif sw is not None:
            self.cardinals[sw] = directions["sw"]
        elif w is not None:
            self.cardinals[w] = directions["w"]
        elif nw is not None:
            self.cardinals[nw] = directions["nw"]
        else:
            raise IndexError


    def parse_xy(self, coords: list) -> list:
        def parse(data):
            for line in self.data:
                direction, steps = line.split()
                yield self.cardinals[direction], int(steps)
