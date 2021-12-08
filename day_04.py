#!/usr/bin/python3
""" Day 4: Giant Squid """
from aocd import get_data


def check_rows(input):
    for i in range(5):
        if set(range(i * 5, 5 + i * 5)) <= set(input):  # horizontal
            return True
        elif i < 5 and set(range(i, 25, 5)) <= set(input):  # vertical
            return True
    return False


def check_bingo(numbers, boards):
    marked = [list() for i in range(len(boards))]
    for number in numbers:
        for i, board in enumerate(boards):
            if number in board:
                marked[i].append(board.index(number))
                check = check_rows(marked[i])
                if check:
                    return i, number, marked[i]


def check_slowest_bingo(numbers, boards):
    marked = [list() for i in range(len(boards))]
    for number in numbers:
        for i, board in enumerate(boards):
            if number in board:
                marked[i].append(board.index(number))
                check = check_rows(marked[i])
                # Last board left?
                if check and sum([len(lst) for lst in boards]) == 25:
                    return i, number, marked[i]
                elif check:
                    boards[i].clear()


def bingo_board(input):
    boards = list()
    for row in input:
        if len(row) == 0:
            boards.append(list())
        boards[-1] += [int(i) for i in row.split()]
    return boards


def bingo(input):
    numbers = [int(n) for n in input[0].split(",")]
    boards = bingo_board(input[1:])
    winning_board, number, marked = check_bingo(numbers, boards)
    unmarked = [n for n in boards[winning_board]
                if boards[winning_board].index(n) not in marked]
    return sum(unmarked) * number


def last_bingo(input):
    numbers = [int(n) for n in input[0].split(",")]
    boards = bingo_board(input[1:])
    winning_board, number, marked = check_slowest_bingo(numbers, boards)
    unmarked = [n for n in boards[winning_board]
                if boards[winning_board].index(n) not in marked]
    return sum(unmarked) * number


def main():
    input = get_data(day=4, year=2021)
    input = input.splitlines()
    print(bingo(input))
    print(last_bingo(input))


if __name__ == "__main__":
    main()
