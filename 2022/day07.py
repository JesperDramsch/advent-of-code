from day import Day
from aocd import submit
from dataclasses import dataclass, field
from operator import ge, le


@dataclass
class Directory:
    name: str
    parent: "Directory" = None
    children: dict = field(default_factory=dict)
    files: dict = field(default_factory=dict)

    def add_child(self, child):
        self.children[child] = Directory(child, parent=self)

    def add_file(self, name: str, size: int):
        self.files[name] = File(name, size)

    def size(self):
        return sum([file.size for file in self.files.values()]) + sum(
            [child.size() for child in self.children.values()]
        )

    def print(self, indent=0):
        print(" " * indent, f"{self.name} ({self.size()})")
        for file in self.files.values():
            print(" " * indent, f"  {file.name} ({file.size})")
        for child in self.children.values():
            child.print(indent=indent + 2)


@dataclass
class File:
    name: str = ""
    size: int = 0


def parse_directory(data):
    tree = Directory("/")
    dir = tree
    for line in data:
        match line.split(" "):
            case "$", "cd", "..":
                dir = dir.parent
            case "$", "cd", "/":
                dir = tree
            case "$", "cd", target_dir:
                dir = dir.children[target_dir]
            case "$", "ls":
                pass
            case "dir", name:
                dir.add_child(name)
            case start, name:
                dir.add_file(name, int(start))
    return tree


def find_dirs(tree, size, over=False):
    small_dirs = []
    comp = ge if over else le
    for child in tree.children.values():
        if comp(child.size(), size):
            small_dirs.append(child.size())
        small_dirs += find_dirs(child, size, over)
    return small_dirs


def main(day, part=1):
    day.parse_list()
    tree = parse_directory(day.data)
    if part == 1:
        return sum(find_dirs(tree, 100000))
    if part == 2:
        space_total = 70000000
        space_needed = 30000000

        space_available = space_total - tree.size()
        free_up = space_needed - space_available

        return min(find_dirs(tree, free_up, over=True))


if __name__ == "__main__":
    day = Day(7)
    day.download()

    day.load()
    p1 = main(day)
    print(p1)
    submit(p1, part="a", day=7, year=2022)

    day.load()
    p2 = main(day, part=2)
    print(p2)
    submit(p2, part="b", day=7, year=2022)
