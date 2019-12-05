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
        99: Exit

        Returns:
            list -- Opcode after execution
        """

        def __opmode(position: int, mode: int) -> int:
            if int(mode) == 0:
                return self.data[position]
            elif int(mode) == 1:
                return position
        
        def __instructor(code: int):
            mode = f"{code:05d}"
            return int(mode[3:]), mode[2], mode[1], mode[0]

        loop = 0
        while loop < len(self.data) or self.data[loop] != 99:
            instruct, A, B, C = __instructor(self.data[loop])
            if instruct == 1:
                self.data[__opmode(loop+3, C)] = self.data[__opmode(loop+1, A)] + self.data[__opmode(loop+2, B)]
                inc = 4
            elif instruct == 2:
                self.data[__opmode(loop+3, C)] = self.data[__opmode(loop+1, A)] * self.data[__opmode(loop+2, B)]
                inc = 4
            elif instruct == 3:
                self.data[__opmode(loop+1, C)] = int(input("Please provide input: "))
                inc = 2
            elif instruct == 4:
                self.diagnostic = self.data[__opmode(loop+1, C)]
                print(self.diagnostic)
                inc = 2
            elif instruct == 99:
                return self.data 
            else:
                break
            loop += inc
    
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
