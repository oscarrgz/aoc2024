from pathlib import Path
import re


def read_input(file_path: Path) -> str:
    """Read input file

    :param Path file_path: Path to the input file
    :return str: Read string
    """

    data_lines = []
    with open(file_path, "r") as in_file:
        data_lines = in_file.read()

    return data_lines


def solve_part_1(input_string: str) -> int:
    """Solve the part 1 of the puzzle

    Find the correct memory instructions and
    multiply its result

    :param str input_string: _description_
    :return int: Result of multiplying correct instructions
    """

    regex = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")

    correct_instructions = regex.findall(input_string)

    return sum([int(x) * int(y) for x, y in correct_instructions])


def keep_only_enabled_instructions(input_string: str) -> int:
    """Remove disabled instructions

    Parse the input string to remove the disabled instructions.
    All instructions that are between don't() and do() statements
    are disabled

    :param str input_string: _description_
    :return str: Cleaned up string
    """
    regex = re.compile(r"(?:don't\(\).*?)+do\(\)", re.DOTALL)

    return regex.sub("", input_string)


def solve_puzzle():
    """Solve puzzle for day 03"""

    input_instructions = read_input(Path(__file__).parent / "input.txt")
    solution_part_1 = solve_part_1(input_instructions)
    print(f"Solution to puzzle 1 is {solution_part_1}")

    cleanded_instructions = keep_only_enabled_instructions(input_instructions)
    solution_part_2 = solve_part_1(cleanded_instructions)
    print(f"Solution to puzzle 2 is {solution_part_2}")


if __name__ == "__main__":
    solve_puzzle()
