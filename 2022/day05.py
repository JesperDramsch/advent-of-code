from day import Day
from aocd import submit
import re
from collections import deque

def parse_lines(data):
    """Parse lines into stacks and list of moves

    Parameters
    ----------
    data : list(str)
        List of strings with stacks and moves separated by empty line

    Returns
    -------
    list(deque(str)), list(tuple(int,int,int)
        Stacks in deques and moves in tuples of "repeats", start, end
    """
    stack_line = data.index("")-1

    num_stack = int(re.findall(r"\d+", data[stack_line])[-1])

    stacks = [deque() for _ in range(num_stack)]
    
    for i in range(stack_line):
        for ii in range(1, len(data[i]), 4):
            if data[i][ii] != " ":
                stacks[ii//4].appendleft(data[i][ii])
    moves = [tuple(map(int, re.findall("\d+", move))) for move in data[stack_line+2:]]
    return stacks, moves

def move_stacks(stacks, moves, cratemove=9000):
    """Move stacks according to moves

    Parameters
    ----------
    stacks : list(deque(str))
        List of deques with stacks
    moves : list(tuple(int, int, int))
        list of move tuples with number of containers, start stack and target stack
    cratemove : int, optional
        type of cratemove crane, by default 9000

    Returns
    -------
    list(deque(str))
        Final stacks after move
    """
    for i, start, end in moves:
        crane = deque()
        for ii in range(i):
            if stacks[start-1]:
                crane.append(stacks[start-1].pop())
        if cratemove == 9001:
            crane.reverse()
        stacks[end-1].extend(crane)
    return stacks

def extract_top(stacks):
    """Get top row of containers across stacks
    """
    return "".join(stack.pop() for stack in stacks)

def main(day, part=1):
    day.parse_list()
    stacks, moves = parse_lines(day.data)
    if part == 1:
        stacks = move_stacks(stacks, moves, cratemove=9000)
    if part == 2:
        stacks = move_stacks(stacks, moves, cratemove=9001)
    return extract_top(stacks)

if __name__ == "__main__":
    day = Day(5)
    day.download()

    day.load(strip=False)
    p1 = main(day)
    print(p1)
    submit(p1, part="a", day=5, year=2022)

    day.load(strip=False)
    p2 = main(day, part=2)
    print(p2)
    submit(p2, part="b", day=5, year=2022)
