from util import Day
from aocd import submit
from itertools import combinations


def preprocess(data):
    out = []
    for row in data:
        ingredients, allergens = row[:-1].split("(contains ")
        out.append((ingredients.split(), allergens.split(", ")))
    return out


def per_allergen(data):
    out = {}

    for ingredients, allergens in data:
        for allergen in allergens:
            if out.get(allergen):
                out[allergen].append(set(ingredients))
            else:
                out[allergen] = [set(ingredients)]
    return out


def sieve(data):
    out = {}
    for allergens, all_ingredients in data.items():
        out[allergens] = [set()]
        for x in all_ingredients:
            tmp = []
            for sets in out[allergens]:
                z = x.intersection(sets)
                if z:
                    tmp.append(z)
                else:
                    tmp.append(x)
            out[allergens] = tmp

    # sort by len
    out = {k: v[0] for k, v in sorted(out.items(), key=lambda item: len(item[1][0]))}
    for a, x in combinations(out.keys(), r=2):
        b, y = out[a], out[x]
        q = b - y
        if q:
            out[a] = q
        q = y - b
        if q:
            out[x] = q
    return {k: v.pop() for k, v in out.items()}


def remove_allergens(data, allergens):
    out = []
    for alli, _ in data:
        out += [v for v in alli if v not in list(allergens.values())]
    return out


def main(day, part=1):
    day.data = preprocess(day.data)
    per = per_allergen(day.data)
    allergens = sieve(per)
    if part == 1:
        clean = remove_allergens(day.data, allergens)
        out = len(clean)
    if part == 2:
        tmp = []
        for k in sorted(allergens.keys()):
            tmp.append(allergens[k])
        out = ",".join(tmp)
    return out


if __name__ == "__main__":
    day = Day(21)
    day.download()

    day.load(typing=str)
    p1 = main(day)
    print(p1)
    submit(p1, part="a", day=21, year=2020)

    day.load(typing=str)
    p2 = main(day, part=2)
    print(p2)
    submit(p2, part="b", day=21, year=2020)
