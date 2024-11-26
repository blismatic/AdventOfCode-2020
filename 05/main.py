from aocd import get_data
from dotenv import load_dotenv

from pprint import pprint

example_input = """"""


def parse(puzzle_input: str):
    """Parse input."""
    result = puzzle_input.split("\n")

    pprint(result[:3])
    print()
    return result


def get_seat_id(boarding_pass: str) -> int:
    boarding_pass = list(reversed(list(boarding_pass)))  # e.g. 'FFB' -> ['B', 'F', 'F']
    result = 0
    for pos, letter in enumerate(boarding_pass):
        if letter == "R" or letter == "B":
            result += 2**pos
    return result


def part1(data: list[str]):
    """Solve and return the answer to part 1."""
    highest_seat_id = -1
    for boarding_pass in data:
        seat_id = get_seat_id(boarding_pass)
        if seat_id > highest_seat_id:
            highest_seat_id = seat_id
    return highest_seat_id


def part2(data):
    """Solve and return the answer to part 2."""
    pass


def solve(puzzle_input) -> tuple:
    """Solve the puzzle for the given input. Returns a tuple containing the answers to part 1 and part 2."""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    load_dotenv()
    # solutions = solve(example_input)
    puzzle_input = get_data(day=5, year=2020)
    solutions = solve(puzzle_input)

    print("\n".join(str(solution) for solution in solutions))
