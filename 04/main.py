from aocd import get_data
from dotenv import load_dotenv

from pprint import pprint
from dataclasses import dataclass
import re

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

    def is_valid_part1(self) -> bool:
        return all([self.byr, self.iyr, self.eyr, self.hgt, self.hcl, self.ecl, self.pid])

    def byr_valid(self) -> bool:
        if self.byr is None:
            return False
        return 1920 <= int(self.byr) <= 2002

    def iyr_valid(self) -> bool:
        if self.iyr is None:
            return False
        return 2010 <= int(self.iyr) <= 2020

    def eyr_valid(self) -> bool:
        if self.eyr is None:
            return False
        return 2020 <= int(self.eyr) <= 2030

    def hgt_valid(self) -> bool:
        if self.hgt is None:
            return False
        if self.hgt[-2:] == "cm":
            return 150 <= int(self.hgt[:-2]) <= 193
        elif self.hgt[-2:] == "in":
            return 59 <= int(self.hgt[:-2]) <= 76
        else:
            return False

    def hcl_valid(self) -> bool:
        if self.hcl is None:
            return False
        pattern = r"^#[0-9a-f]{6}$"
        return bool(re.match(pattern, self.hcl))

    def ecl_valid(self) -> bool:
        if self.ecl is None:
            return False
        return self.ecl in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

    def pid_valid(self) -> bool:
        if self.pid is None:
            return False
        return bool(re.match(r"^[0-9]{9}$", self.pid))

    def is_valid_part2(self) -> bool:
        return all(
            [
                self.is_valid_part1(),
                self.byr_valid(),
                self.iyr_valid(),
                self.eyr_valid(),
                self.hgt_valid(),
                self.hcl_valid(),
                self.ecl_valid(),
                self.pid_valid(),
            ]
        )


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
        if passport.is_valid_part1():
            count += 1
    return count


def part2(data: list[Passport]):
    """Solve and return the answer to part 2."""
    count = 0
    for passport in data:
        if passport.is_valid_part2():
            count += 1
    return count


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
