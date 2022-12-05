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

### 2022-12-05
- `AttributeError: 'NoneType' object has no attribute 'group'` messed up the regex and called `.group` when it was supposed to be `.groups()`
- `IndexError: string index out of range` somehow messed up the indices. Different lines have different length, so I define `ii` dynamically instead.
- `for i, start, end in moves: ValueError: too many values to unpack (expected 3)` mixed up stacks and moves when returning the parser function...
- `stacks[end-1].append(stacks[start-1].pop()) IndexError: pop from an empty deque` didn't consider that stacks would be empty, gotta escape that.
- Messed up the moving, so the example doesn't pass: `AssertionError: assert 'ZMN' == 'CMZ'`
- Somehow messed up the parsing of the stacks. My standard parser strips the string, which doesn't work here. 
- `day.data = day.data.split("\n") AttributeError: 'list' object has no attribute 'split'` simply don't need to split if I have the parser set up right
- Forget to delete debug print statements. Not an error but I definitely had my screen full of deques.
- somehow got a None on the crane `deque()`. Let's investigate: `stacks[end-1].extend(crane.reverse()) TypeError: 'NoneType' object is not iterable` – ah yes, the `deque().reverse()` is in-place.
- Mixed up the example and full data test results, so they failed, when the code worked.