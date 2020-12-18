from util import Day
from aocd import submit


def eval_parens(expression, evaluate):
    while "(" in expression:
        for k in expression.split("("):
            if ")" in k:
                innter = k.split(")")[0]
                expression = expression.replace("(" + innter + ")", str(evaluate(innter)))
    return expression


def eval_left(expression):
    expression = expression.split()
    while ("*" in expression) or ("+" in expression):
        expression = [str(eval("".join(expression[:3])))] + expression[3:]
    return int(expression[0])


def eval_precedence(expression):
    expression = expression.split()
    while "+" in expression:
        plus = expression.index("+")
        expression[plus] = str(eval("".join(expression[plus - 1 : plus + 2])))
        expression.pop(plus + 1)
        expression.pop(plus - 1)
    return eval("".join(expression))


def main(day, part=1):
    if part == 1:
        evaluate = eval_left
    if part == 2:
        evaluate = eval_precedence
    day.apply(eval_parens, evaluate=evaluate)
    day.apply(evaluate)
    return sum(day.data)


if __name__ == "__main__":
    day = Day(18)
    day.download()

    day.load(typing=str)
    p1 = main(day)
    print(p1)
    submit(p1, part="a", day=18, year=2020)

    day.load(typing=str)
    p2 = main(day, part=2)
    print(p2)
    submit(p2, part="b", day=18, year=2020)
