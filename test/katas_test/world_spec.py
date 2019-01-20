from expects import expect
from expects.matchers.built_in import be
from mamba import description, it

from gol.cell import AliveCell, DeadCell
from gol.point import Point
from gol.world import World

a = AliveCell()
d = DeadCell()

with description("World") as self:
    with it("should consider the cells out of bounds as dead"):
        expect(World([[a]]).count_living_neighbors_for(Point())).to(be(0))

    with it("should return an appropriate number of neighbors for cell in the middle"):
        expect(World([[a, d, d]]).count_living_neighbors_for(Point(0, 1))).to(be(1))
