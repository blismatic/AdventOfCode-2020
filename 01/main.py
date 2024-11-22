from aocd import get_data
from dotenv import load_dotenv

from pprint import pprint

example_input = """"""


def parse(puzzle_input: str):
    """Parse input."""
    result = puzzle_input.split("\n")
    result = [int(e) for e in result]

    pprint(result)
    print()
    return result


def part1(data):
    """Solve and return the answer to part 1."""
    target = 2020
    processed = set()
    for num in data:
        complement = target - num
        if complement in processed:
            return complement * num
        elif num not in processed:
            processed.add(num)

    return None


def part2(data):
    """Solve and return the answer to part 2."""
    target = 2020
    for n1 in data[:-2]:
        for n2 in data[1:-1]:
            for n3 in data[2:]:
                if n1 + n2 + n3 == target:
                    return n1 * n2 * n3

    return None


def solve(puzzle_input) -> tuple:
    """Solve the puzzle for the given input. Returns a tuple containing the answers to part 1 and part 2."""
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
