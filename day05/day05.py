from pathlib import Path
from typing import Tuple, List
import math


def read_input(file_path: Path) -> Tuple[List[Tuple[int, int]], List[List[int]]]:
    """Read input file for the puzzle

    The input file consists in two parts separated by
    a line break. First part are the ordering rules,
    second part are the updtes

    :param Path file_path: Path to the input file
    :return str: Read string
    """

    rules = []
    updates = []
    with open(file_path, "r") as in_file:
        lines = in_file.readlines()

    for line in lines:
        if "|" in line:
            values = line.split("|")
            rules.append((int(values[0]), int(values[1])))
        elif "," in line:
            updates.append([int(x) for x in line.split(",")])
    return rules, updates


def update_is_correct(update: List[int], rules: List[Tuple[int, int]]) -> bool:
    """Check if an update is correct according to the rules

    An update is correct if all the appearances are properly ordered
    according to the specified rules

    :param List[int] update: Update to check
    :param List[Tuple[int, int]] rules: Rules to enforce
    :return bool: true if the update follows the rules
    """

    for update_entry in update:
        for rule in rules:
            if update_entry in rule:
                try:
                    # If the second part of rule appears before the first
                    # it is not properly ordered
                    if update.index(rule[0]) > update.index(rule[1]):
                        return False
                except ValueError:
                    pass
    return True


def correct_update(update: List[int], rules: List[Tuple[int, int]]) -> List[int]:
    """Check if an update is correct according to the rules

    An update is correct if all the appearances are properly ordered
    according to the specified rules

    :param List[int] update: Update to check
    :param List[Tuple[int, int]] rules: Rules to enforce
    :return List[int]: corrected order of updates
    """
    while not update_is_correct(update=update, rules=rules):
        for rule in rules:
            if rule[0] in update and rule[1] in update:
                if update.index(rule[0]) > update.index(rule[1]):
                    index_1 = update.index(rule[0])
                    index_2 = update.index(rule[1])
                    update[index_2] = rule[0]
                    update[index_1] = rule[1]
    return update


def get_total_sum_middle_correct_updates(
    updates: List[List[int]], rules: List[Tuple[int, int]]
) -> int:
    """Get solution to part 1

    Compute the sum of the middle values of all the correct updates
    according to the given set of rules

    :param List[List[int]] updates: List of updates
    :param List[Tuple[int, int]] rules: List of rules
    :return int: Sum of middle values
    """
    total_sum = 0
    for update in updates:
        if update_is_correct(update=update, rules=rules):
            total_sum += update[math.floor(len(update) / 2)]
    return total_sum


def get_total_sum_middle_corrected_updates(
    updates: List[List[int]], rules: List[Tuple[int, int]]
) -> int:
    """Get solution to part 2

    Compute the sum of the middle values of all the incorrect updates
    according to the given set of rules after correcting them

    :param List[List[int]] updates: List of updates
    :param List[Tuple[int, int]] rules: List of rules
    :return int: Sum of middle values
    """

    total_sum = 0
    for update in updates:
        if not update_is_correct(update=update, rules=rules):
            corrected_update = correct_update(update=update, rules=rules)
            total_sum += corrected_update[math.floor(len(update) / 2)]
    return total_sum


def solve_puzzle():
    rules, updates = read_input(Path(__file__).parent / "input.txt")
    solution_part_1 = get_total_sum_middle_correct_updates(updates, rules)
    print(f"Solution to puzzle 1 is {solution_part_1}")
    solution_part_2 = get_total_sum_middle_corrected_updates(updates, rules)
    print(f"Solution to puzzle 2 is {solution_part_2}")


if __name__ == "__main__":
    solve_puzzle()
