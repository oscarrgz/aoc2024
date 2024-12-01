#!/usr/bin/env python3
from pathlib import Path
from typing import List, Tuple

import pandas as pd


def read_input_list(path_to_file) -> Tuple[List[int], List[int]]:
    """Read input file

    Parse input file, having two integers per linte separated by spaces

    :param _type_ path_to_file: Path to the input file
    :return Tuple[List[int], List[int]]: Read list of numbers
    """

    list_1 = []
    list_2 = []
    with open(path_to_file, "r") as in_file:
        lines = in_file.readlines()

    for line in lines:
        values = line.split()
        list_1.append(int(values[0]))
        list_2.append(int(values[1]))
    return list_1, list_2


def compute_list_distances(list_1: List[int], list_2: List[int]) -> int:
    """Compute the difference between two lists

    Computes the difference between two lists by comparing its values
    piecewise, pairing up the smalles number in each list

    :param List[int] list_1: Input list 1
    :param List[int] list_2: Input list 2
    :return int: Distance score
    """

    total_distance = 0
    for value_1, value_2 in zip(sorted(list_1), sorted(list_2)):
        total_distance += abs(value_1 - value_2)
    return total_distance


def compute_similarity_score(list_1: List[int], list_2: List[int]) -> int:
    """Compute the similarity score accross list

    Computes the total sum of the list values from 1 multiplied by their
    frequency in list 2.

    :param List[int] list_1: Input list 1
    :param List[int] list_2: Input list 2
    :return int: Similarity score
    """

    similarity_score = 0
    df_2 = pd.DataFrame(list_2, columns=["ids"])
    similarity_score = sum([l * df_2[df_2.ids == l].count() for l in list_1])
    return similarity_score.values[0]


def solve_puzzle():
    """Solve part 1 of puzzle"""

    list_1, list_2 = read_input_list(Path(__file__).parent / "input.txt")

    total_distance = compute_list_distances(list_1=list_1, list_2=list_2)

    # Solution to puzzle 1
    print(f"Total list difference is {total_distance}")
    # Solution to puzzle 2
    similarity = compute_similarity_score(list_1=list_1, list_2=list_2)
    print(f"List similarity is {similarity}")


if __name__ == "__main__":
    solve_puzzle()
