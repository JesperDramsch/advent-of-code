from util import Day
from itertools import permutations


def load_all(objs, data=None):
    for obj in objs:
        obj.load(data=data, typing=int, sep=",")
        obj.apply(int)
        obj.bake()


def amp_chain(objs, phases, volt=0):
    if volt == 0:
        for k, obj in enumerate(objs):
            out = obj.input(phases[k]).input(volt).execute_opcode()
            obj.bake()
            volt = obj.diagnostic
    else:
        for obj in objs:
            out = obj.input(volt).execute_opcode(reset_pointer=False)
            volt = obj.diagnostic
            obj.bake()
    return volt, out


def feedback(amps, phases):
    volt = 0
    for k, obj in enumerate(amps):
        volt = obj.input(phases[k]).input(volt).execute_opcode()
        obj.bake()
    while True:
        for obj in amps:
            volt = obj.input(volt).execute_opcode(reset_pointer=False)
            #obj.bake()
        if volt is None:
            break
    return amps[-1].diagnostic


if __name__ == "__main__":
    amp_a = Day(7, 1)
    amp_b = Day(7, 1)
    amp_c = Day(7, 1)
    amp_d = Day(7, 1)
    amp_e = Day(7, 1)

    amps = [amp_a, amp_b, amp_c, amp_d, amp_e]
    load_all(amps, "3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0".split(","))
    print(amp_chain(amps, [4, 3, 2, 1, 0]))
    load_all(amps, "3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0".split(","))
    print(amp_chain(amps, [0, 1, 2, 3, 4]))
    load_all(amps,"3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0".split(","),)
    print(amp_chain(amps, [1, 0, 4, 3, 2]))

    load_all(amps)
    amp_e.answer(max(amp_chain(amps, num)[0] for num in permutations(range(5))), v=True)
    # 79723

    ## Part2
    amp_a = Day(7, 2)
    amp_b = Day(7, 2)
    amp_c = Day(7, 2)
    amp_d = Day(7, 2) 
    amp_e = Day(7, 2)

    amps = [amp_a, amp_b, amp_c, amp_d, amp_e]

    for amp in amps:
        amp.debug = False
        amp.concurrent = True

    load_all(amps,"3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5".split(","))
    print(amp_chain(amps, [9, 8, 7, 6, 5]))
    print(feedback(amps, [9, 8, 7, 6, 5]))
    amp_e.answer(v=True)

    amp_e.hist()

    # amp_a = Day(7, 2)
    # amp_b = Day(7, 2)
    # amp_c = Day(7, 2)
    # amp_d = Day(7, 2) 
    # amp_e = Day(7, 2)

    # amps = [amp_a, amp_b, amp_c, amp_d, amp_e]

    for amp in amps:
        amp.reset(1)
        amp.debug = False
        amp.concurrent = True
    amp_e.hist()

    load_all(amps,"3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10".split(","))
    feedback(amps, [9, 7, 8, 5, 6])
    amp_e.answer(v=True)

    # amp_a = Day(7, 2)
    # amp_b = Day(7, 2)
    # amp_c = Day(7, 2)
    # amp_d = Day(7, 2) 
    # amp_e = Day(7, 2)

    # amps = [amp_a, amp_b, amp_c, amp_d, amp_e]

    for amp in amps:
        amp.reset(1)
        amp.debug = False
        amp.concurrent = True

    load_all(amps)

    amp_e.answer(max(feedback(amps, num) for num in permutations(range(5,10))), v=True)
