from dataclasses import dataclass


@dataclass
class Cell:
    is_alive: bool = False

    def tick(self, number_of_living_neighbors: int):
        if number_of_living_neighbors == 2:
            return self
        elif number_of_living_neighbors == 3:
            return AliveCell()

        return DeadCell()


class AliveCell(Cell):
    def __init__(self):
        super().__init__(True)


class DeadCell(Cell):
    pass
