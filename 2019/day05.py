from util import Day


if __name__ == "__main__":
    # Part 1
    part1 = Day(5,1)
    part1.load(typing=int, sep=",")

    out = part1.execute_opcode()

    part1.answer(part1.diagnostic, v=1)

    
    # Part 1
    part2 = Day(5,2)
    part2.load(typing=int, sep=",")

    out = part2.execute_opcode()

    part2.answer(part2.diagnostic, v=1)