from typing import Any
from day import Day
from aocd import submit
from functools import cached_property
from utils.parser import Parser
from itertools import combinations


class Page:
    def __init__(self, page_data):
        self.src = page_data[0].split("-to-")[0]
        self.dest = page_data[0].split("-to-")[1].split(" ")[0]
        self._data = page_data[1:]
        self.build_map()

    def build_map(self):
        self._map = {}
        for line in self._data:
            target, source, rng = map(int, line.split())
            self._map[source, source + rng] = (target, target + rng)

    def __repr__(self):
        return f"{self.src} to {self.dest}"

    def __getitem__(self, __key: Any) -> Any:
        for (source_low, source_high), (target_low, _) in self._map.items():
            if source_low <= __key < source_high:
                return target_low + (__key - source_low)
        return __key


class Almanach(dict):
    def __init__(self, data):
        parser = Parser(data)
        parser.parse_list_of_lists(sep="\n\n", sep2="\n")
        self._data = parser.data
        self.build_pages()

    @cached_property
    def seeds(self):
        return list(map(int, self._data[0][0].split(" ")[1:]))

    @cached_property
    def ranges(self):
        return sorted((seed, seed + rng) for seed, rng in zip(self.seeds[::2], self.seeds[1::2]))

    def build_pages(self):
        for page in self._data[1:]:
            page = Page(page)
            self[page.src] = page

    def seed_location(self, seed):
        page = "seed"
        key = seed
        while page != "location":
            key = self[page][key]
            page = self[page].dest
        return key

    def propagate_range(self):
        page = "seed"
        this_range = self.ranges
        print(page, this_range[:3], sum(rng[1] - rng[0] for rng in this_range))
        # Propagate until we're at the location page
        while page != "location":
            next_range = set()
            # For each range, find the overlapping and non-overlapping parts
            for range in this_range:
                new_src_ranges = self.find_segments(range, self[page]._map.keys())

                # Add the overlapping and non-overlapping parts to the next range
                for src_range in new_src_ranges:
                    if src_range is not None:
                        # Shift the end around, since we're using half-open ranges
                        next_range.add((self[page][src_range[0]], self[page][src_range[1] - 1] + 1))

            this_range = sorted(next_range)
            page = self[page].dest
            print(page, this_range[:3], sum(rng[1] - rng[0] for rng in this_range))
        return this_range

    def find_segments(self, original_range, list_of_ranges):
        result = []
        start, end = original_range

        # Check for overlap for all "mapped sections"
        for rng_start, rng_end in list_of_ranges:
            # Check that the range is within the range to check
            if rng_start < end and rng_end > start:
                overlap_start = max(start, rng_start)
                overlap_end = min(end, rng_end)
                result.append((overlap_start, overlap_end))
        result = sorted(result)

        # Add non-overlapping segment if any
        non_result = []
        if result:
            # Add the first non-overlapping segment from the start to the first overlap
            non_overlap_start = start
            non_overlap_end = result[0][0]
            if non_overlap_start < non_overlap_end:
                non_result.append((non_overlap_start, non_overlap_end))

            # Add the non-overlapping segments between the overlaps
            for i in range(len(result) - 1):
                non_overlap_start = result[i][1]
                non_overlap_end = result[i + 1][0]
                if non_overlap_start < non_overlap_end:
                    non_result.append((non_overlap_start, non_overlap_end))

            # Add the last non-overlapping segment from the last overlap to the end
            non_overlap_start = result[-1][1]
            non_overlap_end = end
            if non_overlap_start < non_overlap_end:
                non_result.append((non_overlap_start, non_overlap_end))
        else:
            # If there's no overlap, just return the original range
            result.append(original_range)
        # Merge results
        result.extend(non_result)
        return sorted(set(result))


def main(day, part=1):
    almanach = Almanach(day.data)
    if part == 1:
        return min(almanach.seed_location(seed) for seed in almanach.seeds)
    if part == 2:
        return almanach.propagate_range()[0][0]


if __name__ == "__main__":
    day = Day(5)
    day.download()

    day.load(process=False)
    p1 = main(day)
    print(p1)
    submit(p1, part="a", day=5, year=2023)

    p2 = main(day, part=2)
    print(p2)
    submit(p2, part="b", day=5, year=2023)
