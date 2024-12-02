#!/usr/bin/env python3
from pathlib import Path
from typing import List

import numpy as np


def read_input(file_path: Path) -> List[List[int]]:
    """Read input file

    Read input file, a space delimited csv

    :param Path file_path: Path to the input file
    :return List[List[int]]: Read list of numbers
    """

    data_lines = []
    with open(file_path, "r") as in_file:
        data_lines = [list(map(int, x.split())) for x in in_file.readlines()]

    return data_lines


def is_safe_report(line: List[int]) -> bool:
    """Check if a line number is safe

    A line of numbers is considered safe if

        1. Numbers are monotonic increasing or decreasing.
        2. Numbers are not repeated.
        3. Maximum difference among numbers is 3
    """
    line_diff = np.asarray(line[1:]) - np.asarray(line[:-1])
    diff_signs = np.sign(line_diff)
    if max(np.abs(line_diff)) > 3:
        return False
    # All increasing/decreasing
    elif min(np.abs(line_diff)) <= 0:
        return False
    elif max(diff_signs) != min(diff_signs):
        return False
    return True


def solve_puzzle():
    """Solve day 02 puzzle"""
    lines = read_input(Path(__file__).parent / "input.txt")
    total_correct = 0
    for line in lines:
        if is_safe_report(line):
            total_correct += 1

    print(f"Solution to puzzle 1 is {total_correct}")

    # Now reports are also considered safe if removing one
    # level makes them ok
    total_correct = 0
    for line in lines:
        if is_safe_report(line):
            total_correct += 1
        else:
            for indx in range(0, len(line)):
                if is_safe_report(line[0:indx] + line[indx + 1 :]):
                    total_correct += 1
                    break
    print(f"Solution to puzzle 2 is {total_correct}")


if __name__ == "__main__":
    solve_puzzle()
