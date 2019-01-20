from dataclasses import dataclass
from itertools import product


@dataclass(frozen=True)
class Point:
    x: int = 0
    y: int = 0

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def neighbors(self):
        mutations = product(range(-1, 2), repeat=2)
        return set(Point(self.x + shift[0], self.y + shift[1]) for shift in mutations) - {self}
