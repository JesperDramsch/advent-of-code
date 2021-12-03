from util import Day
from aocd import submit
from collections import Counter

def power_consumption(data):
    epsilon_rate = gamma_rate = ""

    # Make zero & one counters
    zeros = Counter()
    ones = Counter()

    # Iterate through each entry
    for num in data:
        # Iterate through each digit
        for i, digit in enumerate(num):
            if digit == "0":
                zeros[i] += 1
            else:
                ones[i] += 1

    # Iterate through each digit append "0" or "1" to gamma_rate and epsilon_rate
    for i in range(len(data[0])):
        if ones[i] >= zeros[i]:
            gamma_rate += "1"
            epsilon_rate += "0"

        elif zeros[i] > ones[i]:
            gamma_rate += "0"
            epsilon_rate += "1"

    return gamma_rate, epsilon_rate


def life_support_rating(data):

    co2_scrubber_rating = ""

    o2_flag = co2_flag = False

    # Initial split of data
    gamma_rate, epsilon_rate = power_consumption(data)
    o2_data = list(filter(lambda c: c.startswith(gamma_rate[0]), data))
    co2_data = list(filter(lambda c: c.startswith(epsilon_rate[0]), data))

    # Loop through each digit in the data after the first digit
    for i in range(1, len(gamma_rate)):
        # As long as data exists and the flag is not set
        if len(o2_data) > 0 and not o2_flag:
            # Save last entry just in case
            oxygen_generator_rating = o2_data[-1]
            # Find current power consumption
            gamma_rate, _ = power_consumption(o2_data)
            # Filter data to only include max power consumption
            o2_data = list(filter(lambda c: c.startswith(gamma_rate[: i + 1]), o2_data))

        if len(co2_data) > 0 and not co2_flag:
            co2_scrubber_rating = co2_data[-1]
            _, epsilon_rate = power_consumption(co2_data)
            co2_data = list(filter(lambda c: c.startswith(co2_data[0][:i] + epsilon_rate[i]), co2_data))

        # If only one entry left, then we have found the best match
        if len(o2_data) == 1:
            oxygen_generator_rating = o2_data[0]
            o2_flag = True

        if len(co2_data) == 1:
            co2_scrubber_rating = co2_data[0]
            co2_flag = True

        # If both finished processing break
        if o2_flag and co2_flag:
            break

    return oxygen_generator_rating, co2_scrubber_rating


def main(day, part=1):
    if part == 1:
        a, b = power_consumption(day.data)
    if part == 2:
        a, b = life_support_rating(day.data)
    return int(a, 2) * int(b, 2)


if __name__ == "__main__":
    day = Day(3)
    day.download()

    day.load(typing=str)
    p1 = main(day)
    print(p1)
    submit(p1, part="a", day=3, year=2021)

    day.load(typing=str)
    p2 = main(day, part=2)
    print(p2)
    submit(p2, part="b", day=3, year=2021)
