# 🎄 Advent of Code 2023 🎄

## Runtime Error Log

### 2023-12-01

-   `ValueError: invalid literal for int() with base 10: 'eightqrssm9httwogqshfxninepnfrppfzhsc'` getting used to the Day.py again, needs to be `.load(typing=str)`
-   `IndexError: list index out of range` made a logic error filtering the data. Though I could check if it's an int, when iterating through a list of strings
-   `SyntaxError: expression cannot contain assignment, perhaps you meant "=="?` thought keywords in `dict()` had to be strings...
-   `SyntaxError: '(' was never closed` ayo
-   `TypeError: 'list' object is not callable` assigned the same name to the function as the variable... It's too early!
-   `aocd.exceptions.AocdError: cowardly refusing to re-submit answer_a (54159) for part b` Forgot to adjust the parts
-   Submitted wrong answer
-   Thought I can just "replace" the values but this cuts into valid earlier values if they're
-   Forgot to escape string in the f-string

### 2023-12-02

-   `TypeError: expected string or bytes-like object, got 'list'` forgot that I wanted to map the function to each line individually
-   `TypeError: 'str' object does not support item assignment` double assignment of variable 👀
-   Forgot to remove the test data call
-   Mixed up my datatypes `KeyError: 0`, thought it was a list

### 2023-12-03

-   Forgot to add `self` to method
-   Had an `enumerate` instead of looking at the `match_group.span()`, which I caught in the example (not technically an error but good I checked)
-   Forgot to comment out new code while refactoring
-   `TypeError: Engine.add_symbol_neighbours() missing 1 required positional argument: 'symbol'` forgot to remove arg from signature
-   `AttributeError: 'complex' object has no attribute 'location'` should've used dict iteration but used simple for loop...
-   Dict iteration again in another method...
-   `AttributeError: 'Symbol' object has no attribute 'value'`, symbol not part...
-   `KeyError: (1+9j)` oops. Changed keys to ID but didn't update the assignment

### 2023-12-04

-   `ValueError: invalid literal for int() with base 10: 'Card'` forgot to get rid of the "Card ###":
-   `TypeError: unsupported operand type(s) for -: 'set' and 'int'` put the -1 inside the length
-   Not technically an error, but I didn't have parentheses around the exponent, so got the wrong result on the test data
-   `TypeError: unsupported operand type(s) for +=: 'NoneType' and 'int'` initialized extra_tickets as None, could just use 0
-   Would only be fair to note that I was hunting a bunch of off-by-one errors, but they never actually resulted in errors or bad submissions.

### 2023-12-05

-   Messed up the import of the Parser
-   `AttributeError: 'list' object has no attribute 'split'` indexed the wrong one...
-   `ValueError: invalid literal for int() with base 10: 'seeds:'` forgot it has a name
-   `TypeError: 'str' object cannot be interpreted as an integer` forgot to `int()` the range
-   `MemoryError` didn't look at the input. Building a dense dictionary is a bad idea...
-   `TypeError: '<=' not supported between instances of 'int' and 'tuple'` messed up somewhere?
-   `TypeError: '<=' not supported between instances of 'int' and 'range'` trying to figure out how to do the ranges... this will probably not work anyways...
-   Ok, honestly, we knew this wouldn't work, just going through the ranges. We need to find the overlaps of ranges.
-   `TypeError: list.append() takes exactly one argument (2 given)` forgot to make them tuples again

### 2023-12-06

-   `TypeError: object of type 'generator' has no len()` should've just used a list
-   `TypeError: sequence item 0: expected str instance, int found` thought I could be lazy
-   `TypeError: can only concatenate str (not "int") to str` so many types. So little time

### 2023-12-07

-   `TypeError: unsupported operand type(s) for *: 'int' and 'Hand'` wanted to access the bid attribute of the hand, but got sloppy
-   `KeyError: 'J'` forgot that there are hands without Jokers...
-   `IndexError: list index out of range` got a hand full of jokers...

### 2023-12-08

-   `AttributeError: 'list' object has no attribute 'split'`
-   Accidentally re-ran A for part B

### 2023-12-09

-   `sequences = Parser(day.data).parse_list_of_lists(sep2=" ", sep="\n" typing=int)` forgot a comma
-   `NameError: name 'sequence' is not defined. Did you mean: 'Sequence'?` changes to `self.data` and didn't update
-   `wrong answer: That's not the right answer; your answer is too high` Huh, genuinely thought I had it...
-   `SyntaxError: can't use starred expression here` figuring out how to zip the enumerate
-   `ValueError: Expected 2D array, got scalar array instead:` playing around with scikit-learn
-   Scikit-learn didn't work but it was fun trying.
-   My big error was thinking I could just use `sum(sequence) == 0` and of course I couldn't -.-'

### 2023-12-10

-   `TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'` didn't return value from "self.method"
-   `AttributeError: 'PipeSystem' object has no attribute 'set_all_neighbours'.` Refactor incomplete...
-   Had an error where I used every Neighbour that could connect to "this" pipe, without filtering for "this" pipe to connect to the other
-   `RecursionError: maximum recursion depth exceeded while calling a Python object` computer go brrrr
-   Made a mistake, where the "start symbol" wasn't counted as a "vertical bar", so got the wrong answer.

### 2023-12-11

-   `KeyError: 7` tried to remove from set twice

### 2023-12-12

-   `AttributeError: 'dict' object has no attribute 'check_valid'` wrong object
-   `TypeError: 'int' object is not iterable` forgot the range again...
-   Didn't read the instructions for part 2 correctly. I was missing the extra `?` -.-'
-   Have to switch to dynamic programming to work with pointers instead
-   Somehow `@cache` was memoizing the wrong info and writing my own state_dict gave the correct info?

### 2023-12-13

-   Forgot to reset the tolerance in the loop for checking midpoints

### 2023-12-14

-   `TypeError: 'float' object cannot be interpreted as an integer` even remembered it first, but then forgot to "int" the value
-   Got my logic wrong, where I needed to use `or` instead of `and`
-   Had to sort my list depending on the tilt direction, which stumped me a bit

### 2023-12-15

-   Wrong regex `AttributeError: 'NoneType' object has no attribute 'groups'`

### 2023-12-16

-   `SyntaxError: expected '('` used `def` meant `class`
-   `TypeError: '>' not supported between instances of 'complex' and 'int'` wrong variable
-   `TypeError: 'NoneType' object is not iterable`
-   `UnboundLocalError: cannot access local variable 'new_direction' where it is not associated with a value` indents
-   Wrong answer. I was stupid about "cleaning up the connections"
-   I double counted crossing beams... So just using a set and optimising later
-   `TypeError: '>' not supported between instances of 'set' and 'int'` wrong append
-   Also had to use raw strings, because of backslashes.

Didn't need to optimise...

### 2023-12-17

-   `AttributeError: 'list' object has no attribute 'splitlines'` damnit Copilot!
-   `TypeError: '<' not supported between instances of 'complex' and 'int'` heap doesn't like comparing my nice coordinates.
-   I wanted to do something else today, so I looked at what 4HbQ did and it was mindblowing. I need to learn about priority queues more.

### 2023-12-18

-   `IndexError: list index out of range` hmmm...
-   `ValueError: invalid literal for int() with base 16: '#088ba'` no hashtags!

### 2023-12-19

-   `AttributeError: 'list' object has no attribute 'split'` forget to turn off processing
-   `TypeError: cannot unpack non-iterable Parser object` forgot to access the data
-   `TypeError: int() argument must be a string, a bytes-like object or a real number, not 'tuple'` findall returned a list not the tuples
-   `ValueError: not enough values to unpack (expected 4, got 3)` forgot to drop the last value for the splits

Absolute ugly brute force. Best not to run this...

### 2023-12-20

-   `ValueError: not enough values to unpack (expected 2, got 1)` yikes
-   Tried running it for a while, but it took a while, so I looked at the graph, found a bunch of conjunctions and figured out how to reverse engineer the low pulse coinciding and hope for some periodicity in the conjunctions two before, where it's four conjunctions that have to come together. Then just LCM, good ol' AoC periodicity!

### 2023-12-21

-   Can't do mod on complex, I figured but wanted to test anyways.
-   Part two, I started check the input and there's a weird diamond shape in the input...
-   Checked the solutions, because I have no clue how to solve this.

### 2023-12-22

-   Didn't account for "self-collision" in my check, but caught it.
-   Got two wrong answers, probably from moving the bricks around.
-   Assumed the bricks were sorted like in the example...
-   First time, I gave a bunch of wrong answers... Simulating the move now, then moving.
-   Thought I had to find the maximum number of bricks that would fall... Not the sum...

### 2023-12-23

-   Forgot an enumerate
-   Had to figure out how to search all paths possible...
-   Using networkx, but turns out it doesn't have an easy way to find the "longest path", all set to the shortest one.
-   Mixed up the check `has_nodes` and `has_edges`, which gave an error. I should sleep probably...
-   Takes a bit to run part 2
