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


def part1(data: list[str], slope: tuple[int, int] = (3, 1)) -> int:
    """Solve and return the answer to part 1."""
    length = len(data[0])  # This refers to the length of a single row before it begins re-starting
    start_pos = {"x": 0, "y": 0}
    curr_pos = start_pos
    slope = {"x": slope[0], "y": slope[1]}

    num_trees = 0
    for row in data[:: slope["y"]]:
        if row[curr_pos["x"] % length] == "#":
            num_trees += 1
        curr_pos["x"] += slope["x"]
        curr_pos["y"] -= slope["y"]  # Assume that moving down the map decreases your y-value

    return num_trees


def part2(data: list[str]) -> int:
    """Solve and return the answer to part 2."""
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

    num_trees = [part1(data, slope=s) for s in slopes]
    result = 1
    for tree in num_trees:
        result *= tree
    return result


def solve(puzzle_input) -> tuple:
    """Solve the puzzle for the given input. Returns a tuple containing the answers to part 1 and part 2."""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    load_dotenv()
    # solutions = solve(example_input)
    puzzle_input = get_data(day=3, year=2020)
    solutions = solve(puzzle_input)

    print("\n".join(str(solution) for solution in solutions))
