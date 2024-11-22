from aocd import get_data
from dotenv import load_dotenv

from pprint import pprint

example_input = """"""


def parse(puzzle_input):
    """Parse input."""
    print(repr(puzzle_input))
    print()

    return puzzle_input.split("\n")


def part1(data):
    """Solve part 1."""
    pass


def part2(data):
    """Solve part 2."""
    pass


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    load_dotenv()
    # solutions = solve(example_input)
    puzzle_input = get_data(day=1, year=2020)
    solutions = solve(puzzle_input)

    print("\n".join(str(solution) for solution in solutions))
