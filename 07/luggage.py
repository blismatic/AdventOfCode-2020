from __future__ import annotations


class Luggage:
    def __init__(self, style: str):
        self.style: str = style
        self.children: list[Luggage] = []
        self.unique_children: set[Luggage] = set()

    def add_children(self, luggage: Luggage, count: int) -> None:
        for _ in range(count):
            self.children.append(luggage)
            self.unique_children.add(luggage)

    def can_hold(self, style: str) -> bool:
        """Returns True if a certain style of luggage can be held inside this luggage, otherwise returns False."""
        if len(self.children) == 0:
            return False
        if style in self.unique_children:
            return True

        for child in self.children:
            return child.can_hold(style)


def main():
    """
    light red bags contain 1 bright white bag, 2 muted yellow bags.
    dark orange bags contain 3 bright white bags, 4 muted yellow bags.
    bright white bags contain 1 shiny gold bag.
    muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
    shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
    dark olive bags contain 3 faded blue bags, 4 dotted black bags.
    vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
    faded blue bags contain no other bags.
    dotted black bags contain no other bags.
    """
    light_red = Luggage("light red")
    dark_orange = Luggage("dark orange")
    bright_white = Luggage("bright white")
    muted_yellow = Luggage("muted yellow")
    shiny_gold = Luggage("shiny gold")
    dark_olive = Luggage("dark olive")
    vibrant_plum = Luggage("vibrant plum")
    faded_blue = Luggage("faded blue")
    dotted_black = Luggage("dotted black")

    light_red.add_children(bright_white, 1)
    light_red.add_children(muted_yellow, 2)

    dark_orange.add_children(bright_white, 3)
    dark_orange.add_children(muted_yellow, 4)

    bright_white.add_children(shiny_gold, 1)

    muted_yellow.add_children(shiny_gold, 2)
    muted_yellow.add_children(faded_blue, 9)

    shiny_gold.add_children(dark_olive, 1)
    shiny_gold.add_children(vibrant_plum, 2)

    dark_olive.add_children(faded_blue, 3)
    dark_olive.add_children(dotted_black, 4)

    vibrant_plum.add_children(faded_blue, 5)
    vibrant_plum.add_children(dotted_black, 6)

    all_bags = [light_red, dark_orange, bright_white, muted_yellow, shiny_gold, dark_olive, vibrant_plum, faded_blue, dotted_black]
    count = 0
    my_style = shiny_gold
    for bag in all_bags:
        if bag.can_hold(my_style):
            count += 1
    print(count)


if __name__ == "__main__":
    main()
