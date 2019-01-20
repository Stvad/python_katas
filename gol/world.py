# todo desirealization?
from dataclasses import dataclass, field
from typing import List

from functional import seq

from gol.cell import Cell
from gol.point import Point


@dataclass
class World:
    data: List[List[Cell]] = field(default_factory=list)

    def count_living_neighbors_for(self, coordinate: Point):
        return seq(coordinate.neighbors()).count(lambda c: self.is_alive(c))

    def is_alive(self, coordinate: Point):
        return self.is_coordinate_within_world(coordinate) and self.data[coordinate.y][coordinate.x].is_alive

    def is_coordinate_within_world(self, coordinate):
        return self.data and \
               coordinate.y in range(len(self.data)) and \
               coordinate.x in range(len(self.data[0]))
