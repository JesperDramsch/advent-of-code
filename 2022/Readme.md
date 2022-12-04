# 2022

## Running Errorlog

### 2022-12-03
- Can't index into a set.
- `sum(map(...) for ...)` caused mixed `int` and `map` to not be summed. Sum the integers in the map first to ensure equal type.
- Encoding error loading the readme in `conftest.py` on windows. Always load text files with `encoding="utf8"` or there will be errors.
- Used the set union, when I should have used the intersection in part 2.
- Mistyped `rucksack` and `rucksacks`.
- Badges were added at the beginning of the loop, so the last badges of the group weren't added to the list, which caused a low result. There are probably clean fixes, but I just added an empty item to the data, to add an extra final loop to not repeat the code unnecessarily. 

### 2022-12-04
- `ValueError: invalid literal for int() with base 10: '-'` forgot that numbers can be more than 1 digit
- `TypeError: int() argument must be a string, a bytes-like object or a real number, not 'tuple'` misremembered the call of regex groups as `regex.groups(0)`, when the `.groups()` just returns the tuple of matches.
- Wrong result on example, because I checked for partial containment not full. Changed `or` to `and` and it passes. // My hello part 2
- ` TypeError: contained() missing 1 required positional argument: 'b'` when rewriting the parser and the contained function, I forgot to adjust the function call in `main()`