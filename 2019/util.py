class Day:
    def __init__(self, day: int, part: int):
        from problems import description
        self.day  = day
        self.part = part
        self.desc = description(day, part)
    
    def load(self, typing=str) -> list:
        with open(f"day{self.day:02d}.txt") as f:
            data = f.read().splitlines()
        self.data = list(map(typing, data))
        return self.data

    def apply(self, func) -> list:
        return list(map(func, self.data))

    def answer(self, num) -> str:
        return f"The Solution on Day {self.day} for Part {self.part} is: {num}"

if __name__ == "__main__":
    day = Day(1,1)

    print("Data is:", day.data(int))
    print("Day is:", day.day)
    print("Part is:", day.part)
    print("Description is:", day.desc)
