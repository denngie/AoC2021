#!/usr/bin/python3
""" Day 1: Sonar Sweep """
from aocd import get_data


def depth_compare(input):
    increases = len([i for i in range(1, len(input))
                    if input[i] > input[i-1]])
    return increases


def sliding_depth_compare(input):
    increases = len([i for i in range(3, len(input))
                    if sum(input[i-2:i+1]) > sum(input[i-3:i])])
    return increases


def main():
    input = [int(n) for n in get_data(day=1, year=2021).splitlines()]
    print(depth_compare(input))
    print(sliding_depth_compare(input))


if __name__ == "__main__":
    main()
