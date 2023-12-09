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
