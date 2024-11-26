from aocd import get_data
from dotenv import load_dotenv

from pprint import pprint

example_input = """"""


def parse(puzzle_input: str):
    """Parse input."""
    result = puzzle_input.split("\n\n")
    result = [group_answers.split("\n") for group_answers in result]

    pprint(result[:3])
    print()
    return result


def unique_answers(group: list[str]) -> int:
    """Returns the number of answers that anyone in a group answered yes to."""
    answers = set()
    for person in group:
        answers.update(person)
    return len(answers)


def similar_answers(group: list[str]) -> int:
    """Returns the number of answers that everyone in a group answered yes to."""
    answers = set(group[0])
    for person in group[1:]:
        answers = answers.intersection(person)
    return len(answers)


def part1(data: list[list[str]]):
    """Solve and return the answer to part 1."""
    result = 0
    for group in data:
        result += unique_answers(group)
    return result


def part2(data):
    """Solve and return the answer to part 2."""
    result = 0
    for group in data:
        result += similar_answers(group)
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
    puzzle_input = get_data(day=6, year=2020)
    solutions = solve(puzzle_input)

    print("\n".join(str(solution) for solution in solutions))
