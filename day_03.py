#!/usr/bin/python3
""" Day 3: Binary Diagnostic """
from aocd import get_data


def calculate_power(input):
    gamma, epsilon = "", ""

    for i in range(12):
        temp = list(input[i::13])
        gamma += max(temp, key=temp.count)
        epsilon += min(temp, key=temp.count)
    return int(gamma, 2) * int(epsilon, 2)


def calculate_oxy_co2(oxyin, co2in):
    oxygen, co2 = "", ""

    for i in range(12):
        temp = list(oxyin[i::13])
        zeros = temp.count("0")
        ones = temp.count("1")
        if ones >= zeros:
            keep = "1"
        else:
            keep = "0"
        oxyin = [n for n in oxyin.splitlines() if n[i] == keep]
        if len(oxyin) == 1:
            oxygen = oxyin[0]
            break
        oxyin = "\n".join(oxyin)
    for i in range(12):
        temp = list(co2in[i::13])
        zeros = temp.count("0")
        ones = temp.count("1")
        if ones >= zeros:
            keep = "0"
        else:
            keep = "1"
        co2in = [n for n in co2in.splitlines() if n[i] == keep]
        if len(co2in) == 1:
            co2 = co2in[0]
            break
        co2in = "\n".join(co2in)
    return int(oxygen, 2) * int(co2, 2)


def main():
    input = get_data(day=3, year=2021)
    print(calculate_power(input))
    print(calculate_oxy_co2(input, input))


if __name__ == "__main__":
    main()
