from pathlib import Path
from typing import Tuple
import numpy as np
from numpy.typing import NDArray


def read_input(file_path: Path) -> NDArray:
    """Read input file

    :param Path file_path: Path to the input file
    :return str: Read string
    """

    data_lines = []
    with open(file_path, "r") as in_file:
        data_lines = in_file.readlines()
    data_lines = [list(line.replace("\n", "")) for line in data_lines]

    return np.asarray(data_lines)


class GuardPath:

    DIRECTION_MAP = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}

    def __init__(self, input_map: NDArray):

        self.input_map = input_map
        self.n_rows = input_map.shape[0]
        self.n_cols = input_map.shape[1]

    def find_start_point(self) -> Tuple[int, int]:
        """Find the initial position of the guard

        Find the initial position of the guard in
        the search map

        :return Tuple[int, int]: Indexes of the initial
            position
        """
        for i_row in range(0, self.n_rows):
            for j_col in range(0, self.n_cols):
                if self.input_map[i_row, j_col] in self.DIRECTION_MAP.keys():
                    return i_row, j_col
        raise ValueError("Guard not present in input map!")

    def is_end(self, i_row: int, j_col: int) -> bool:
        """Check if we reached the end of the map

        Check if the next moves reaches the end of the map

        :param int i_row: Next move row
        :param int j_col: Next move col
        :return bool: True if reached the end
        """

        return i_row >= self.n_rows or j_col >= self.n_cols or i_row < 0 or j_col < 0

    def get_next_direction(self, current_direction: str):
        """Get the next direction

        Get the next direction, considering that it always turns
        righst.

        :param str current_direction: Current direction
        """
        directions = list(self.DIRECTION_MAP.keys())
        next_direction = (directions.index(current_direction) + 1) % len(directions)
        return directions[next_direction]

    def count_route(self) -> int:
        """Count the number of positions

        Count the total number of visited
        positions taken during the guard route

        :return int: Number of visited positions
        """
        i_row, j_col = self.find_start_point()
        current_direction = self.input_map[i_row, j_col]
        step_row, step_col = self.DIRECTION_MAP[current_direction]
        position_paths = set()
        position_paths.add((i_row, j_col))
        while not self.is_end(i_row=i_row + step_row, j_col=j_col + step_col):
            if self.input_map[i_row + step_row, j_col + step_col] != "#":
                # I can take a step
                i_row += step_row
                j_col += step_col
                position_paths.add((i_row, j_col))
            else:
                # I need to turn
                current_direction = self.get_next_direction(
                    current_direction=current_direction
                )
                step_row, step_col = self.DIRECTION_MAP[current_direction]
        return len(position_paths)


def solve_puzzle():
    input_map = read_input(Path(__file__).parent / "input.txt")
    guard = GuardPath(input_map=input_map)
    solution_part_1 = guard.count_route()
    print(f"Solution to puzzle 1 is {solution_part_1}")


if __name__ == "__main__":
    solve_puzzle()
