from functools import partial

class Day:
    def __init__(self, day: int, part: int):
        from problems import description
        self.day  = day
        self.part = part
        self.desc = description(day, part)
    
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
        self.raw_data = self.data.copy()
        return self.data
    
    def reset(self):
        """Reset Data to original
        """
        self.data = self.raw_data.copy()
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
        mapfunc = partial(func, *args,**kwargs)
        self.data = list(map(mapfunc, self.data))
        return self.data
    
    def execute_opcode(self) -> list:
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

        def __opmode(position: int, mode: int, get = False) -> int:
            if int(mode) == 0:
                position = self.data[position]
            if get:
                return self.data[position]
            else:
                return position
        
        def __instructor(code: int):
            mode = f"{code:05d}"
            return int(mode[3:]), mode[2], mode[1], mode[0]

        pointer = 0
        while pointer < len(self.data):
            instruct, A, B, C = __instructor(self.data[pointer])
            inc = 0
            if instruct == 1:
                # Multiply
                self.data[__opmode(pointer+3, C)] = __opmode(pointer+1, A, get=True) + __opmode(pointer+2, B, get=True)
                inc = 4
            elif instruct == 2:
                # Add
                self.data[__opmode(pointer+3, C)] = __opmode(pointer+1, A, get=True) * __opmode(pointer+2, B, get=True)
                inc = 4
            elif instruct == 3:
                # Input
                self.data[__opmode(pointer+1, C)] = int(input("Please provide input: "))
                inc = 2
            elif instruct == 4:
                # Output
                self.diagnostic = __opmode(pointer+1, A, get=True)
                print(self.diagnostic)
                inc = 2
            elif instruct == 5:
                # Jump If True
                # Jump If False
                if __opmode(pointer+1, A, get=True) != 0: 
                    pointer = __opmode(pointer+2, B, get=True)
                else:
                    inc = 3
            elif instruct == 6:
                # Jump If True
                # Jump If False
                if __opmode(pointer+1, A, get=True) == 0: 
                    pointer = __opmode(pointer+2, B, get=True)
                else:
                    inc = 3
            elif instruct == 7:
                # Less Than
                self.data[__opmode(pointer+3, 0)] = int(__opmode(pointer+1, A, get=True) < __opmode(pointer+2, B, get=True))
                inc = 4
                pass
            elif instruct == 8:
                # Equals
                self.data[__opmode(pointer+3, 0)]  = int(__opmode(pointer+1, A, get=True) == __opmode(pointer+2, B, get=True))
                inc = 4
                pass
            elif instruct == 99:
                return self.data 
            else:
                raise RuntimeError(f'ERR {instruct}: \n Data Dump: {self.data[pointer], pointer}')
                break
            pointer += inc
    
    def answer(self, num=None, v=False) -> str:
        if not num == None:
            self.result = num
        s = f"The Solution on Day {self.day} for Part {self.part} is: {self.result}"
        if v:
            print(s)
        return s

if __name__ == "__main__":
    day = Day(1,1)

    print("Day is:", day.day)
    print("Part is:", day.part)
    print("Description is:", day.desc)
