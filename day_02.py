#!/usr/bin/python3
""" Day 2: Dive! """
from aocd import get_data


def calculate_position(input):
    pos, depth = 0, 0
    for command in input:
        direction, units = command.split()
        units = int(units)
        if direction == "forward":
            pos += units
        elif direction == "down":
            depth += units
        elif direction == "up":
            depth -= units
    return pos * depth


def calculate_position_with_aim(input):
    pos, depth, aim = 0, 0, 0
    for command in input:
        direction, units = command.split()
        units = int(units)
        if direction == "forward":
            pos += units
            depth += units * aim
        elif direction == "down":
            aim += units
        elif direction == "up":
            aim -= units
    return pos * depth


def main():
    input = get_data(day=2, year=2021)
    input = input.splitlines()
    print(calculate_position(input))
    print(calculate_position_with_aim(input))


if __name__ == "__main__":
    main()
