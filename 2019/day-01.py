import util

def fuel(module: int):
    return module // 3 - 2

def fuelchain(module: int):
    out = [fuel(module)]
    while(out[-1] > 0):
        out.append(fuel(out[-1]))
    return out[:-1]

if __name__ == "__main__":
    out1 = 0
    out2 = 0

    data = util.load_aoc("01")

    ## Part One
    for el in data:
        out1 += fuel(int(el))
    
    print("Output for Problem 1:", out1)

    ## Part 2
    for el in data:
        out2 += sum(fuelchain(int(el)))

    print("Output for Problem 2:", out2)