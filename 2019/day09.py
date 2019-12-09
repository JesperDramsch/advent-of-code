from util import Day

if __name__ == "__main__":
    part1 = Day(9, 1)
    part1.load(typing=int, sep=",")
    part1.debug = True

    in_l = len(part1)
    part1.input(1)
    part1.execute_opcode()
    part1.answer(v=1)

    #print(part1[:in_l])
