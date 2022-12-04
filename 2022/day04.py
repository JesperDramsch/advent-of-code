from util import Day
from aocd import submit
import re

def parse(line: str):
    """Parse numbers out of line of pattern 0-1,2-3

    Parameters
    ----------
    line : str
        line with string and numbers to parse

    Returns
    -------
    tuple(tuple(int, int), tuple(int, int))
        parsed numbers
    """
    m = re.match(r"(\d+)-(\d+),(\d+)-(\d+)", line).groups()
    a = int(m[0]), int(m[1])
    b = int(m[2]), int(m[3])
    return a, b

def contained(a, b, full=True) -> bool:
    """Check if a is contained in b or b is contained in a

    Parameters
    ----------
    a : tuple(int, int)
        tuple of two numbers with start and end
    b : tuple(int, int)
        tuple of two numbers with start and end
    full : bool, optional
        Check partial overlap (False) or full containment, by default True

    Returns
    -------
    bool
        Whether it's contained or not
    """

    a_contained = b[0] <= a[0] <= b[1], b[0] <= a[1] <= b[1]
    b_contained = a[0] <= b[0] <= a[1], a[0] <= b[1] <= a[1]
    if full:
        return (a_contained[0] and a_contained[1]) or (b_contained[0] and b_contained[1])
    else:
        return a_contained[0] or a_contained[1] or b_contained[0] or b_contained[1]
        
def main(day, part=1):
    day.data = (parse(line) for line in day.data)
    if part == 1:
        return sum(int(contained(*pairing)) for pairing in day.data)
    if part == 2:
        return sum(int(contained(*pairing, False)) for pairing in day.data)

if __name__ == "__main__":
    day = Day(4)
    day.download()

    day.load(typing=str)
    p1 = main(day)
    print(p1)
    submit(p1, part="a", day=4, year=2022)

    day.load(typing=str)
    p2 = main(day, part=2)
    print(p2)
    submit(p2, part="b", day=4, year=2022)
