from util import Day

def fuel(module: int) -> int:
    return module // 3 - 2

def fuelchain(module: int) -> int:
    out = [fuel(module)]
    while(out[-1] > 0):
        out.append(fuel(out[-1]))
    return sum(out[:-1])

if __name__ == "__main__":
    ## Part One
    part1 = Day(1,1)
    part1.load(int)
    
    out = sum(part1.apply(fuel))
    
    print(part1.answer(out))

    ## Part 2
    part2 = Day(1,2)
    part2.load(int)

    out = sum(part2.apply(fuelchain))
    
    print(part2.answer(out))
