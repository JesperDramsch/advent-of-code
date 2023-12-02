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
