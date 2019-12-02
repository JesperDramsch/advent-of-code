from util import Day

def fuel(weight: int) -> int:
    """Calculate Fuel Requirements
    
    Arguments:
        weight {int} -- Weight of Input
    
    Returns:
        int -- Fuel Requirements
    """
    return weight // 3 - 2

def fuelchain(module: int) -> int:
    """Recursive Fuel calculation
    To understand recursion, one first has to understand recursion.
    
    Arguments:
        module {int} -- Weight of Module
    
    Returns:
        int -- Total Fuel Requirements with "wishing really hard"
    """
    out = [fuel(module)]
    while(out[-1] > 0):
        out.append(fuel(out[-1]))
    return sum(out[:-1]) # Skip last one

if __name__ == "__main__":
    ## Part One
    part1 = Day(1,1)
    part1.load(int)
    
    out = sum(part1.apply(fuel))
    
    print(part1.desc)
    print(part1.answer(out))

    ## Part 2
    part2 = Day(1,2)
    part2.load(int)

    out = sum(part2.apply(fuelchain))
    
    print(part2.desc)
    print(part2.answer(out))
