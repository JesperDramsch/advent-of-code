from functools import partial


class Day:
    def __init__(self, day: int, part: int):
        from problems import description

        self.day = day
        self.part = part
        self.desc = description(day, part)
        self.task = self.desc.strip().split("\n")[-1].strip()

        self.pointer = 0
        self.debug = False
        self.concurrent = False
        self.op_input = []

    def load(self, data=None, typing=str, sep="\n", path="") -> list:
        """Loads Data for Problem
        File _must_ be named dayXX.txt
        Returns data and makes it available as attribte "data"

        Keyword Arguments:
            data {[list]} -- Load computed data not from file (default: {None})
            typing {[type]} -- Type of data in list (default: {str})
            sep {[str]} -- Separator in input data (default: {"\n"})
        
        Returns:
            list -- Data for Problem
        """
        if path == "":
            path = f"data/day{self.day:02d}.txt"
        if data:
            self.data = data
        else:
            with open(path) as f:
                data = f.read().split(sep)
            if "" in data:
                data.remove("")
            self.data = list(map(typing, data))
        self.raw_data = [self.data.copy()]
        return self

    def bake(self):
        """Finalize processed data as resettable
        """
        self.raw_data.append(self.data.copy())
        return self

    def input(self, data):
        """Input data to queue
        """
        self.op_input.append(data)
        return self

    def reset(self, step=None):
        """Reset Opcode class

        Resets data, and pointer.
        Flushes input queue.
        
        Can restore specific data from history

        Keyword Arguments:
            step {[int]} -- restoration point (default: {Last})
        """
        if step is None:
            step = len(self.raw_data) - 1
        self.data = self.raw_data[step].copy()
        self.raw_data = [x.copy() for x in self.raw_data[: step + 1]]
        self.op_input = []
        self.pointer = 0
        return self

    def hist(self):
        """Produce data history
        """
        l = len(self.raw_data)
        ends = ("y", "ies")
        print(f"{l} histor{ends[l != 1]} saved")
        print("=" * 15)
        for hist in self.raw_data:
            s = f"{hist}"
            print(s[:70] + " . . ." * (70 < len(s)))

    def summary(self):
        """Produce Task Summary
        """
        s = f"The problem for Day {self.day} and part {self.part}:\n{self.task}"
        if hasattr(self, "result"):
            print(s)
            self.answer(v=True)
        else:
            print(s)

    def sum(self) -> float:
        return sum(self.data)

    def apply(self, func, *args, **kwargs) -> list:
        """Apply a function to every element.
        Changes the original data.

        Arguments:
            func {function} -- Function to apply to every element in input
        
        Returns:
            list -- Function applied to every element in input
        """
        mapfunc = partial(func, *args, **kwargs)
        self.data = list(map(mapfunc, self.data))
        return self.data

    def execute_opcode(self, three_in=None, reset_pointer=True) -> list:
        """Execute OpCode operation
        
        1:  Add
        2:  Multiply
        3:  Input
        4:  Output
        5:  Jump If True
        6:  Jump If False
        7:  Less Than
        8:  Equals
        99: Exit

        Returns:
            list -- Opcode after execution
        """

        def __opmode(pointer: int, mode: tuple, offset: int, get=False) -> int:
            if int(mode[offset - 1]) == 0:
                position = self.data[pointer + offset]
            else:
                position = pointer + offset
            if get:
                return self.data[position]
            else:
                return position

        def __instructor(code: int):
            mode = f"{code:05d}"
            return int(mode[3:]), (mode[2], mode[1], mode[0])

        inc = {
            1: 4,
            2: 4,
            3: 2,
            4: 2,
            5: 3,
            6: 3,
            7: 4,
            8: 4,
        }

        if three_in is not None:
            self.input(three_in)

        if reset_pointer is True:
            self.pointer = 0
        while self.pointer < len(self.data):
            instruct, param = __instructor(self.data[self.pointer])
            if self.debug is True:
                print(instruct, end="")
            if instruct == 1:
                # Multiply
                self.data[__opmode(self.pointer, param, offset=3)] = __opmode(
                    self.pointer, param, offset=1, get=True
                ) + __opmode(self.pointer, param, offset=2, get=True)
                self.pointer += inc[instruct]
            elif instruct == 2:
                # Add
                self.data[__opmode(self.pointer, param, offset=3)] = __opmode(
                    self.pointer, param, offset=1, get=True
                ) * __opmode(self.pointer, param, offset=2, get=True)
                self.pointer += inc[instruct]
            elif instruct == 3:
                # Input
                if not getattr(self, "op_input"):
                    self.data[__opmode(self.pointer, param, offset=1)] = int(
                        input("Please provide input: ")
                    )
                elif type(self.op_input) == list:
                    self.data[__opmode(self.pointer, param, offset=1)] = int(self.op_input.pop(0))
                self.pointer += inc[instruct]
            elif instruct == 4:
                # Output
                self.diagnostic = __opmode(self.pointer, param, offset=1, get=True)
                self.result = self.diagnostic  # Save as result
                self.pointer += inc[instruct]
                if self.concurrent is True:
                    return self.diagnostic
            elif instruct == 5:
                # Jump If True
                if __opmode(self.pointer, param, offset=1, get=True) != 0:
                    self.pointer = __opmode(self.pointer, param, offset=2, get=True)
                else:
                    self.pointer += inc[instruct]
            elif instruct == 6:
                # Jump If False
                if __opmode(self.pointer, param, offset=1, get=True) == 0:
                    self.pointer = __opmode(self.pointer, param, offset=2, get=True)
                else:
                    self.pointer += inc[instruct]
            elif instruct == 7:
                # Less Than
                self.data[__opmode(self.pointer, param, offset=3)] = int(
                    __opmode(self.pointer, param, offset=1, get=True)
                    < __opmode(self.pointer, param, offset=2, get=True)
                )
                self.pointer += inc[instruct]
            elif instruct == 8:
                # Equals
                self.data[__opmode(self.pointer, param, offset=3)] = int(
                    __opmode(self.pointer, param, offset=1, get=True)
                    == __opmode(self.pointer, param, offset=2, get=True)
                )
                self.pointer += inc[instruct]
            elif instruct == 99:
                self.op_input = []  # Flush inputs
                return None
            else:
                raise RuntimeError(
                    f"ERR {instruct}: \n Data Dump: {self.data[self.pointer]} Index:{self.pointer}"
                )
                break

    def answer(self, num=None, v=False) -> str:
        """Produce answer string
        
        Saves number in result attribute and returns a nice string

        Keyword Arguments:
            num {int} -- Input result (default: {None})
            v {bool} -- Verbesity (default: {False})
        
        Returns:
            str -- Answer string
        """
        if num is not None:
            self.result = num
        s = f"The Solution on Day {self.day} for Part {self.part} is: {self.result}"
        if v:
            print(s)
        return s


if __name__ == "__main__":
    day = Day(1, 1)

    print("Day is:", day.day)
    print("Part is:", day.part)
    print("Description is:", day.desc)
