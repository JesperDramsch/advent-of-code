from util import Day
from itertools import groupby


def check_password(password: str, limit_groups=False) -> bool:
    """Password Checker
    
    Arguments:
        password {str} -- 6 string password
    
    Keyword Arguments:
        limit_groups {bool} -- Only conut real doubles (no groups) (default: {False})
    
    Returns:
        bool -- Valid password
    """
    password = password.strip()  # because always

    six = len(password) == 6
    # doub = not sorted(set(password)) == sorted(password) # Part 1 worked
    for _, g in groupby(password):
        lg = len(list(g))  # This here killed me. g is empty after one run.
        if lg >= 2 and not limit_groups:
            doub = True
            break
        elif lg == 2 and limit_groups:
            doub = True
            break
    else:
        doub = False

    sort = "".join(sorted(password)) == password
    return six and doub and sort


if __name__ == "__main__":
    # Part 1
    part1 = Day(4, 1)

    part1.load(typing=int, sep="-")
    part1.load(list(range(part1.data[0], part1.data[1] + 1)))

    part1.apply(str)

    part1.apply(check_password)

    print(part1.answer(part1.sum()))

    # Part 2
    part2 = Day(4, 2)

    part2.load(typing=int, sep="-")
    part2.load(list(range(part2.data[0], part2.data[1] + 1)))

    part2.apply(str)

    part2.apply(check_password, limit_groups=True)

    print(part2.answer(part2.sum()))

