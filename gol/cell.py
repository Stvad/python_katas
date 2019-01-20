class Cell:
    def tick(self, number_of_living_neighbors: int):
        if number_of_living_neighbors == 2:
            return self
        elif number_of_living_neighbors == 3:
            return AliveCell()

        return DeadCell()


class AliveCell(Cell):
    pass


class DeadCell(Cell):
    pass
