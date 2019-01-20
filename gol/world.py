from copy import deepcopy
from dataclasses import dataclass, field
from typing import List, Dict, Type

from functional import seq

from gol.cell import Cell, AliveCell, DeadCell
from gol.point import Point

representations: Dict[str, Type] = {'*': AliveCell, '.': DeadCell}
reversed_representations = {v: k for k, v in representations.items()}


@dataclass
class World:
    data: List[List[Cell]] = field(default_factory=lambda: [[]])

    def count_living_neighbors_for(self, coordinate: Point):
        return seq(coordinate.neighbors()).count(lambda c: self.is_alive(c))

    def is_alive(self, coordinate: Point):
        return self.is_coordinate_within_world(coordinate) and self.data[coordinate.y][coordinate.x].is_alive

    def is_coordinate_within_world(self, coordinate):
        return self.data and \
               coordinate.y in range(len(self.data)) and \
               coordinate.x in range(len(self.data[0]))

    def tick(self):
        new_data = deepcopy(self.data)

        for i in range(len(self.data)):
            for j in range(len(self.data[0])):
                new_data[i][j] = self.data[i][j].tick(self.count_living_neighbors_for(Point(j, i)))

        self.data = new_data

    def __repr__(self):
        return '\n'.join([World.serialize_line(line) for line in self.data])

    @staticmethod
    def from_string(world_string: str):
        return World([World.deserialize_line(line) for line in world_string.split()])

    @staticmethod
    def deserialize_line(line):
        return [representations[c]() for c in line]

    @staticmethod
    def serialize_line(line):
        return ''.join([reversed_representations[type(cell)] for cell in line])
