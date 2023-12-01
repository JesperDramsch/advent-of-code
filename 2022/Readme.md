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

### 2022-12-08
- `if cell > max_height[ii]: TypeError: '>' not supported between instances of 'str' and 'int'` forgot to change the variable name in function
- Tried to do some fancy indexing in a row, but realised I'm not checking the list forward and backward. Will just have to do indexing normally without enumerate to keep the code tidy.
- Forgot to remove print statements before the big input. What a wall of text!
- `visible = check_visibility(flip(grid), flip(visible)) NameError: name 'flip' is not defined` Removed `flip()` thinking it wasn't needed, as I don't need to flip anymore.
- `data = """30373 IndentationError: unexpected indent` accidentally hit tab
- My logic in part 2 seems faulty. Something isn't increasing numbers how I expected it to. May be the `enumerate(range(...))`. Have to investigate.
- `UnboundLocalError: cannot access local variable 'i' where it is not associated with a value` forgot to remove an `i`
- Found the error, I was starting ON the tree of the tree house so all viewing distances were seen as `0`... Off-by-one errors. The bane of my coding existence.
- `out.append(i+1) UnboundLocalError: cannot access local variable 'i' where it is not associated with a value` tried quick and dirty. Didn't work.

### 2022-12-09
- `day.data = parse(data) NameError: name 'data' is not defined` oops. Forgot `day.`.
- `tail = head.real - (diff.real / abs(diff.real)) + (head.imag - (diff.imag / abs(diff.imag))) * 1j ZeroDivisionError: float division by zero` didn't think about zeros...
- `print(f"{head.real:d} + {head.imag:d}j, \t {tail.real:d} + {tail.imag:d}j,\t {direction.real:d} + {direction.imag:d}j,\t {steps},\t {visited}") ValueError: Unknown format code 'd' for object of type 'float'` confused type conversion and formatting
- Conceptual error that I did not adjust the diagonal movement correctly.
- `visited = set(0) TypeError: 'int' object is not iterable` Can't start the set with just a zero
- `tail = rope[i+1] IndexError: list index out of range` gotta stop one before the end with pairs
- Made the error of using a for loop that returns items on a list that is changing... Didn't throw an error but gave the wrong result.

### 2022-12-10
- `cycle += 1 UnboundLocalError: cannot access local variable 'cycle' where it is not associated with a value` forgot to start cycles
- `check = checks.values()[0] TypeError: 'dict_values' object is not subscriptable` thought that would be a list or something.
- `check = checks[20] KeyError: 20` oh my. Good thing I caught that, I set up my `range()` wrong.
- `if cycles < check <= cycles+inc: TypeError: '<' not supported between instances of 'int' and 'NoneType'` Time to debug what I messed up here! I clearly don't understand the `match` statement well enough yet. Ok, since I split on an empty space the "noop" line still is a list, so the case has to also look into a list like this: `case "noop",:`. Good to know.
- `if cycles < check <= cycles+inc: TypeError: '<' not supported between instances of 'int' and 'NoneType'` ah. Messed up my logic about using `checks`. It should be the keys I'm working with and I also caught that I need to increment it.
- `return sum(cyclce*X for cycle, X in checks.items()) NameError: name 'cyclce' is not defined. Did you mean: 'cycle'?` haha, those typos will get me every time.
- `return inc, add UnboundLocalError: cannot access local variable 'add' where it is not associated with a value` you'd think I'd learn this by now.
- `return plot_crt(draw_crt(instructions)) NameError: name 'instructions' is not defined` argh. wrong name!
- Bit of an understanding error about the CRT. I thought it was continuous indexing, but in fact it is for every line individually. Easy fix!

### 2022-12-11
- `self.number = int(data[0].split(" ")[1]) NameError: name 'data' is not defined` forgot to rename the variable
- ` self.number = int(text[0].split(" ")[1]) ValueError: invalid literal for int() with base 10: '0:'` Overlooked the ":"
- `def main(day, part=1): IndentationError: expected an indented block after function definition on line 35` started writing the `turn()` method, but didn't add `pass` before working on something different.
- ` from collection import deque ModuleNotFoundError: No module named 'collection'` I can never remember the right name. It's `collections`
- `item //= 3 TypeError: unsupported operand type(s) for //=: 'NoneType' and 'int'` looks like I messed something up with the items. Forgot the "new =" in the split of the operation. Also caught that I'm now saving the modified self-operation here.
- `operation = self.operation.replace("old", "{old}").format(old=item) ValueError: Exceeds the limit (4300) for integer string conversion; use sys.set_int_max_str_digits() to increase the limit` well that's new. Apparently Python cannot convert long ints anymore.
- `if sum(remaidners) == 0: NameError: name 'remaidners' is not defined. Did you mean: 'remainders'?` Speelink is hart
- `item = [sum(item) // 3] TypeError: 'NoneType' object is not iterable` tried to return an `item.append(...)`, which is `None`.
- `return [i * int(right) for i in item]TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'` maybe my idea for calculating the modulo arithmetics actually doesn't work out?
- `item.append((op, right)) AttributeError: 'int' object has no attribute 'append'` 
- ` self.items = deque(deque(self.starting_items)) AttributeError: 'Monkey' object has no attribute 'starting_items'` oops. it's just `starting_items`

### 2022-12-12
- `wrong answer: 23` well... the hill climbing seemed easy. Now to find what I did wrong.
-  `if 0 < x < len(data) and row - 1 <= data[x-1][y] <= row + 1: TypeError: unsupported operand type(s) for -: 'list' and 'int'` didn't think about where the actual value is...
- `day.data[E[1]][E[0]] = ord("z") IndexError: list index out of range` switched rows and columns and forgot this one.
- `import scipy as sp ModuleNotFoundError: No module named 'scipy'` for once it's not my error! The big data seems to need scipy for networkx.
- ` raise nx.NetworkXNoPath(f"No path between {source} and {target}.") networkx.exception.NetworkXNoPath: No path between S and E.` Oh no... Ah. I need a directed graph.
- `raise nx.NetworkXNoPath(f"No path between {source} and {target}.") networkx.exception.NetworkXNoPath: No path between (0, 10) and (20, 120).` haha, yeah of course there are basins without connection to the peak.
- ` except networkx.exception.NetworkXNoPath: NameError: name 'networkx' is not defined` ah just copied the exception but imported `networkx as nx`

### 2022-12-13
- `def main(day, part=1): IndentationError: expected an indented block after function definition on line 4` Good ol' suddenly working on a different idea and forgetting a `pass`
- `indices = [i, compare(outcome) for i, outcome in enumerate(day.data)] SyntaxError: did you forget parentheses around the comprehension target?` Yes I did.
-  `indices = [(i, compare(outcome)) for i, outcome in enumerate(day.data)] TypeError: compare() missing 1 required positional argument: 'right'` Whoops. `*outcome`
- `raise ValueError(msg + f': {node!r}') ValueError: malformed node or string: [4, 3, 4, [2]]` forgot to escape the string evaluation in a recursive function.
- `if value in {u"", b"", None, b"None", u"None"}: TypeError: unhashable type: 'list'` forgot to actually do the math.
- `return sum(i[0] for i in indices if i[1]]) SyntaxError: closing parenthesis ']' does not match opening parenthesis '('` Hello autocomplete...
- `wrong answer: 662` oh no. Off by one!
- `return sorted(day.data, cmp=compare) TypeError: 'cmp' is an invalid keyword argument for sort()` It helps reading the documentation for Python 3 instead of 2...
- `return sorted([item for sublist in day.data for item in sublist], key=compare) TypeError: compare() missing 1 required positional argument: 'right'` ok... this time actually read the full paragraph and import `cmp_to_key()` from `functools` *facepalm*

### 2022-12-14
- Not an error, but I did get a wrong intermittent result, when I forgot to change `min` to `max` in `range(min(b,y), max(b,y) + 1):`
- `if not grid and start in grid: TypeError: argument of type 'bool' is not iterable` want to make it work with the existing function, but messed up one return.
- Wrong answer for example part 2, but that was just a off-by-one error in the floor.

### 2022-12-15
- `day.data = (complex(a, b), complex(c, d) for a, b, c, d in day.data) SyntaxError: invalid syntax` oops. Those tuple parantheses. One day I will learn.
- `return block(8+7j, 9) NameError: name 'block' is not defined. Did you mean: 'clock'?` yes I did..
- `blocked = set(sensor) TypeError: 'complex' object is not iterable` One day I'll learn.
- `blocked = set.union(clock(sensor, manhattan(sensor, beacon)) for sensor, beacon in day.data) TypeError: descriptor 'union' for 'set' objects doesn't apply to a 'generator' object` hm... 
- `for i in range(distance+1): TypeError: 'float' object cannot be interpreted as an integer` ah the distance measure should return an int.
- ` a, b = merge(a, b) ValueError: too many values to unpack (expected 2)` Didn't tuple the tuple.
- `return blocked[y] KeyError: 2000000` hehe, still on the easy stuff not the big problem.

### 2022-12-16
- `for tunnel in tunnels[valve]: TypeError: string indices must be integers, not 'str'` replaced the wrong variable. That was silly.
- `self.name: str NameError: name 'self' is not defined` tried to write dataclasses from memory
- `v.neighbours[v2.name] = find_shortest_path(valves, v.name, v2.name) TypeError: 'NoneType' object does not support item assignment` Gotta initialize those values.
- `if min(minutes) <= 0: UnboundLocalError: cannot access local variable 'minutes' where it is not associated with a value` forgot to rename the variable
- `all_minutes = (new_minutes,) + all_minutes[not eleflop] TypeError: can only concatenate tuple (not "int") to tuple` forgot I changed  to index instead of slice

It's December 24th when I finally solved this with heavy help from the solutions thread. I lost my mind on this and out of frustration I stopped adding errors here, especially when I got unconcentrated over the weekend. Sorry.

### 2022-12-17
- `new_pieces.append(i+ii*1j) NameError: name 'new_pieces' is not defined. Did you mean: 'new_piece'?` oops. Yes I did. The new Python errors are really good actually.
- `IndentationError: expected an indented block after function definition on line 52` started working on a different part and forgot the `pass`
- `return "\n".join("".join(row) for row in self.board) TypeError: can only join an iterable` argh. Yeah makes sense. I don't actually have rows.
- `for i, v in self.pieces.items(): AttributeError: 'list' object has no attribute 'items'` wrong variable
- `def _right(self): SyntaxError: invalid syntax` closing brackets. Weird autocomplete quirks...
- `if i + direction in self.board or i + direction < 0 or i + direction > self.width: TypeError: '<' not supported between instances of 'complex' and 'int'` argh, yeah makes sense.
- `for i in range(self.height): TypeError: 'float' object cannot be interpreted as an integer` oops, yeah the `max()` function returned a float
- `self.check_tetris(piece) TypeError: Tetris.check_tetris() takes 1 positional argument but 2 were given` forgot to provide the `piece` to the function
- `signature = tuple(k-(self.height+23) for k, v in self.board.items() if k >= self.height - 23)TypeError: '>=' not supported between instances of 'complex' and 'int'` I will never not fall for this.
- `self.height += height_offset - h_end UnboundLocalError: cannot access local variable 'height_offset' where it is not associated with a value` didn't initialize...

### 2022-12-18
- Made a logic error, where I thought a single dimension has to be offset by one to be a neighbour. No idea how I had that error in my mind.
- `cube = nx.grid_graph(dim=(range(min_x-2, max_x+2), range(min_y-2, max_y+2), range(min_z-2, max_z+2)) SyntaxError: '(' was never closed` just autocomplete things.
- `KeyError: (-2, -2, -2)` oops. wrong minimum

### 2022-12-19
- `self.robot_cost = {ore: None, clay: None, obsidian: None, geode: None} NameError: name 'ore' is not defined. Did you mean: 'ord'?` forgot to make the keys strings
- `self.robot_cost["ore"] = extract_cost(re.search(r'Each ore robot costs ([\d a-z]+).', self.data).group(1)) NameError: name 'extract_cost' is not defined` method not function. my bad
- `def Factory: SyntaxError: expected '('` that should've been a class
- `self.ore += self.robots['ore']AttributeError: 'Factory' object has no attribute 'ore'` worked on changing the resources to a Counter