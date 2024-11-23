from aocd import get_data
from dotenv import load_dotenv

from pprint import pprint
from collections import Counter

example_input = """"""


def parse(puzzle_input: str):
    """Parse input."""
    result = puzzle_input.split("\n")
    temp = [line.split(" ") for line in result]
    result = []
    for row in temp:
        char_range = row[0].split("-")
        _min = int(char_range[0])
        _max = int(char_range[1])

        result.append({"_min": _min, "_max": _max, "letter": row[1][0], "password": row[2]})

    pprint(result[:4])
    print()
    return result


def part1(data: list[dict]):
    """Solve and return the answer to part 1."""

    def is_valid(row: dict) -> int:
        c = Counter(row["password"])
        num_letters = c[row["letter"]]
        if row["_min"] <= num_letters <= row["_max"]:
            return 1
        else:
            return 0

    num_valid_passwords = sum([is_valid(row) for row in data])
    return num_valid_passwords


def part2(data):
    """Solve and return the answer to part 2."""

    def is_valid(row: dict) -> int:
        pos_1 = row["_min"] - 1  # Toboggan Corporate Policies use 1 based indexing, but we want 0 based.
        pos_2 = row["_max"] - 1
        letter = row["letter"]
        password = row["password"]

        if (password[pos_1] == letter and password[pos_2] != letter) or (password[pos_1] != letter and password[pos_2] == letter):
            return 1
        else:
            return 0

    num_valid_passwords = sum([is_valid(row) for row in data])
    return num_valid_passwords


def solve(puzzle_input) -> tuple:
    """Solve the puzzle for the given input. Returns a tuple containing the answers to part 1 and part 2."""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    load_dotenv()
    # solutions = solve(example_input)
    puzzle_input = get_data(day=2, year=2020)
    solutions = solve(puzzle_input)

    print("\n".join(str(solution) for solution in solutions))
