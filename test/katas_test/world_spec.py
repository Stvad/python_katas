from expects import expect
from expects.matchers.built_in import be, equal
from mamba import description, it, context

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

    with context("serialization"):
        with it("should be able to load world from string"):
            expect(World.from_string(".*.").data).to(equal([[d, a, d]]))

        with it("should be able to handle multiline strings"):
            expect(World.from_string(".\n*").data).to(equal([[d], [a]]))

        with it("should be able to do round-trip"):
            world_map = "..*.\n.**.\n.*.."
            expect(repr(World.from_string(world_map))).to(equal(world_map))
