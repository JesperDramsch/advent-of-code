from util import Day

if __name__ == "__main__":
    part1 = Day(9, 1)
    part1.load(typing=int, sep=",")
    part1.debug = True

    in_l = len(part1)
    part1.input(1)
    part1.time().execute_opcode().time()
    part1.answer(v=1)

    #print(part1[:in_l])

    part2 = Day(9, 2)
    part2.load(typing=int, sep=",")
    part2.debug = True

    in_l = len(part2)
    part2.input(2)
    part2.time().execute_opcode().time()
    part2.answer(v=1)

    #print(part2[:in_l])
