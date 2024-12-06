from pathlib import Path
from typing import List
import numpy as np


def read_input(file_path: Path) -> List[str]:
    """Read input file

    :param Path file_path: Path to the input file
    :return str: Read string
    """

    data_lines = []
    with open(file_path, "r") as in_file:
        data_lines = in_file.readlines()
    data_lines = [list(line.replace("\n", "")) for line in data_lines]

    return np.asarray(data_lines)


def find_count_target_word(search_map: List[str], target_word: str = "XMAS") -> int:
    """Find count of a target word

    Find the total appearances of the target word in the search map
    array of strings. The target word migh appear horizontally, vertically,
    diaganoally and might be backwargs

    :param List[str] search_map: search space, assumed that length of strings is constant
    :param str target_word: Word to be searched for, defaults to "XSMAS"
    :return int: Number of word appearances
    """

    word_length = len(target_word)
    n_cols = len(search_map[0])
    n_rows = len(search_map)
    count = 0

    for i_row in range(0, n_rows):
        for j_col in range(0, n_cols):
            if search_map[i_row, j_col] != target_word[0]:
                continue

            # Look horizontally forward:
            if j_col + word_length <= n_cols:
                word = "".join(search_map[i_row, j_col : j_col + word_length])
                count += 1 if word == target_word else 0
                # look diagonally up/forwards
                if i_row + word_length <= n_rows:
                    word = "".join(
                        [
                            search_map[i_row + x, j_col + x]
                            for x in range(0, word_length)
                        ]
                    )
                    count += 1 if word == target_word else 0
                # look diagonally down/forward
                if i_row - word_length + 1 >= 0:
                    word = "".join(
                        [
                            search_map[i_row - x, j_col + x]
                            for x in range(0, word_length)
                        ]
                    )
                    count += 1 if word == target_word else 0

            # Look horizontally backwards
            if j_col - word_length + 1 >= 0:
                word = "".join(
                    [search_map[i_row, j_col - x] for x in range(0, word_length)]
                )
                count += 1 if word == target_word else 0
                # look diagonally up/backwards
                if i_row + word_length <= n_rows:
                    word = "".join(
                        [
                            search_map[i_row + x, j_col - x]
                            for x in range(0, word_length)
                        ]
                    )
                    count += 1 if word == target_word else 0
                # look diagonally down/backwards
                if i_row - word_length + 1 >= 0:
                    word = "".join(
                        [
                            search_map[i_row - x, j_col - x]
                            for x in range(0, word_length)
                        ]
                    )
                    count += 1 if word == target_word else 0
            # Look vertically downwards:
            if i_row + word_length <= n_rows:
                word = "".join(search_map[i_row : i_row + word_length, j_col])
                count += 1 if word == target_word else 0
            # Look vertically upwards
            if i_row - word_length + 1 >= 0:
                word = "".join(
                    [search_map[i_row - x, j_col] for x in range(0, word_length)]
                )
                count += 1 if word == target_word else 0

    return count


def solve_puzzle():
    input_instructions = read_input(Path(__file__).parent / "input.txt")
    solution_part_1 = find_count_target_word(input_instructions)
    print(f"Solution to puzzle 1 is {solution_part_1}")


if __name__ == "__main__":
    solve_puzzle()
