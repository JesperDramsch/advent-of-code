from functools import partial

class Day:
    def __init__(self, day: int, part: int):
        from problems import description
        self.day  = day
        self.part = part
        self.desc = description(day, part)
    
    def load(self, data=None, typing=str, sep="\n") -> list:
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
        if data:
            self.data = data
        else:
            with open(f"data/day{self.day:02d}.txt") as f:
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
        99: Exit

        Returns:
            list -- Opcode after execution
        """
        for i in range(0,len(self.data),4):
            if self.data[i] == 1:
                self.data[self.data[i+3]] = self.data[self.data[i+1]] + self.data[self.data[i+2]]
            elif self.data[i] == 2:
                self.data[self.data[i+3]] = self.data[self.data[i+1]] * self.data[self.data[i+2]]
            elif self.data[i] == 99:
                return self.data 
            else:
                break
    
    def sum(self) -> float:
        return sum(self.data)

    def answer(self, num) -> str:
        self.result = num
        return f"The Solution on Day {self.day} for Part {self.part} is: {num}"

if __name__ == "__main__":
    day = Day(1,1)

    print("Day is:", day.day)
    print("Part is:", day.part)
    print("Description is:", day.desc)
