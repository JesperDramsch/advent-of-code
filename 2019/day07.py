from util import Day
from itertools import permutations


def load_all(objs, data=None):
    """Load data into all provided objects
    
    Arguments:
        objs {Day class} -- Day class containing OpCode iterator
    
    Keyword Arguments:
        data {list} -- Data to load, None loads input file (default: {None})
    """
    for obj in objs:
        obj.load(data=data, typing=int, sep=",")
        obj.apply(int)
        obj.bake()


def amp_chain(objs, phases, volt=0):
    """Chain objects of Day class

    Problem statement asks for several OpCode instances to be chained together
    
        O-------O  O-------O  O-------O  O-------O  O-------O
    0 ->| Amp A |->| Amp B |->| Amp C |->| Amp D |->| Amp E |-> (to thrusters)
        O-------O  O-------O  O-------O  O-------O  O-------O

    Arguments:
        objs {Day.class} -- OpCode iterator class
        phases {list(int)} -- Phase setting to change amplifier seed
    
    Keyword Arguments:
        volt {int} -- Start voltage for first run of Amp chain (default: {0})
    
    Returns:
        {int}, {int} -- Returns output of last amp and the state value
    """
    if volt == 0:
        for k, obj in enumerate(objs):
            out = obj.input(phases[k]).input(volt).execute_opcode()
            obj.bake()
            volt = obj.diagnostic
    else:
        for obj in objs:
            out = obj.input(volt).execute_opcode(reset_pointer=False)
            obj.bake()
            volt = obj.diagnostic
    return volt, out


def feedback(amps, phases, volt=0):
    """Feedback loop of amp chain

    Reruns chain of amplifiers until "halt" is reached in last amplifier
    Feeds last output to input of next run
    Phases are provided once at first input and not changed after

          O-------O  O-------O  O-------O  O-------O  O-------O
    0 -+->| Amp A |->| Amp B |->| Amp C |->| Amp D |->| Amp E |-.
       |  O-------O  O-------O  O-------O  O-------O  O-------O |
       |                                                        |
       '--------------------------------------------------------+
                                                                |
                                                                v
                                                        (to thrusters)

    Arguments:
        amps {Day.class} -- Amplifiers in Feedback loop of amp chain
        phases {list(int)} -- Phase settings to seed operation of amp chain

    Keyword Arguments:
        volt {int} -- Input voltage to amplifier at first amp for first iteration (default: {0})

    Returns:
        int -- Output voltage after feedback loop
    """
    while True:
        volt, out = amp_chain(amps, phases, volt)
        if isinstance(out, Day):
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
        amp.reset(1) # Reset all amps to state after loading and int conversion
        amp.debug = False
        amp.concurrent = True

    load_all(amps)

    amp_e.answer(max(feedback(amps, num) for num in permutations(range(5,10))), v=True)
