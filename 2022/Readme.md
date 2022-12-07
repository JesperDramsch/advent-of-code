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

### 2022-12-06
- Got an empty list, but caught that early, because I didn't want to mess up with this new data. There are no splits and it's a singular string, so I figured my standard loader might not love it.
- Put the data `mjqjpqmgbljsphdztnvjfqwrcgsmlb` as the solution to the test example. That was a simple enough brain fart.
- `day.data = [i, set(day.data[x-i] for i in range(4)) for x in range(3, len(day.data))] SyntaxError: invalid syntax`, forgot parantheses
- `IndexError: list index out of range` messing up the index shifting in the stream
- Off-by-one error, because the puzzle expects 1-indexed numbers.
- Didn't change the variable name from `day.data` to `data` when refactoring into a function for part 2.

### 2022-12-07
- `elif "ls" in line: SyntaxError: invalid syntax` forgot a closing bracket
- `dir = dir.children[dir.children.index(line.split(" ")[1])] ValueError: 'cd' is not in list` forgot that commands have 2 spaces
- `ValueError: '/' is not in list` follow up to error before where I don't return to root properly, I'll split the command as a result
- `ValueError: 'cwdpn' is not in list` – no idea what that even means, I made a logic error somewhere. Gotta go debug!
- `dir.add_file(line.split(" ")) TypeError: Directory.add_file() missing 1 required positional argument: 'name'` gotta broadcast the tuple!
- `start, name = line.split(" ")[1] ValueError: too many values to unpack (expected 2)` - oops, I should maybe be a bit more careful
- `AttributeError: 'str' object has no attribute 'size'` changed to a dictionary representation and didn't adjust the size calculation
- `TypeError: unsupported operand type(s) for +: 'int' and 'str'` didn't convert the sizes to an integer in the File class
- `ValueError: invalid literal for int() with base 10: 'grgj'` another very nice mistake parsing. Gotta take it slower. The sizes are first in the files.
- `AttributeError: 'NoneType' object has no attribute 'print'` forgot to return the tree from the `parse_directory()` function
- Used `if` instead of `elif`, which caused an unexpected output on the `$ cd ..` command
- Part 2: `wrong answer: 1186199` too high. So I made some logic error.