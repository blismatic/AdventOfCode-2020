from aocd import get_data
from dotenv import load_dotenv

from pprint import pprint
from dataclasses import dataclass

example_input = """"""


@dataclass
class Passport:
    byr: str = None
    iyr: str = None
    eyr: str = None
    hgt: str = None
    hcl: str = None
    ecl: str = None
    pid: str = None
    cid: str = None

    def is_valid(self) -> bool:
        return all([self.byr, self.iyr, self.eyr, self.hgt, self.hcl, self.ecl, self.pid])


def parse(puzzle_input: str):
    """Parse input."""
    result = puzzle_input.split("\n\n")
    result = [passport.replace("\n", " ") for passport in result]
    result = [dict(passport.split(":") for passport in passport.split()) for passport in result]
    result = [Passport(**item) for item in result]

    pprint(result[1])
    print()
    return result


def part1(data: list[Passport]):
    """Solve and return the answer to part 1."""
    count = 0
    for passport in data:
        if passport.is_valid():
            count += 1
    return count


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
    puzzle_input = get_data(day=4, year=2020)
    solutions = solve(puzzle_input)

    print("\n".join(str(solution) for solution in solutions))
