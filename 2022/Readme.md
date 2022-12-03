# 2022

## Running Errorlog

### 2022-12-03
- Can't index into a set.
- `sum(map(...) for ...)` caused mixed `int` and `map` to not be summed. Sum the integers in the map first to ensure equal type.
- Encoding error loading the readme in `conftest.py` on windows. Always load text files with `encoding="utf8"` or there will be errors.
- Used the set union, when I should have used the intersection in part 2.
- Mistyped `rucksack` and `rucksacks`.
- Badges were added at the beginning of the loop, so the last badges of the group weren't added to the list, which caused a low result. There are probably clean fixes, but I just added an empty item to the data, to add an extra final loop to not repeat the code unnecessarily. 