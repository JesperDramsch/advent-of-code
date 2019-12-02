from util import Day

def compute(opcode: list) -> list:
    for i in range(0,len(opcode),4):
        if opcode[i] == 1:
            opcode[opcode[i+3]] = opcode[opcode[i+1]] + opcode[opcode[i+2]]
        elif opcode[i] == 2:
            opcode[opcode[i+3]] = opcode[opcode[i+1]] * opcode[opcode[i+2]]
        elif opcode[i] == 99:
            return opcode 
        else:
            break



if __name__ == "__main__":
    ## Part One
    part1 = Day(2,1)
    part1.load(int, ",")
    
    part1.data[1] = 12
    part1.data[2] = 2
    out = compute(part1.data)
    
    #out = sum(part1.apply(fuel))
    
    #print(part1.desc)
    print(part1.answer(out[0]))

    ## Part 2
    part2 = Day(2,2)
    part2.load(int, ",")

    for i in range(100):
        for j in range(100):
            data = part2.data.copy()
            data[1] = i
            data[2] = j
            out = compute(data)
            if out is None:
                continue
            elif out[0] == 19690720:
                print(i,j)
                print(part2.answer(100 * i + j))
                break

    obj_part2 = Day(2,2)
    obj_part2.load(int, ",")

    for i in range(100):
        for j in range(100):
            obj_part2.reset()
            obj_part2.data[1:3] = [i, j]
            out = obj_part2.execute_opcode()
            if out is None:
                continue
            elif out[0] == 19690720:
                print(i,j)
                print(obj_part2.answer(100 * i + j))
                break
    #out = sum(part2.apply(fuelchain))
    
    #print(part2.desc)
