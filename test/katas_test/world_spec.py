from expects import expect
from expects.matchers.built_in import be, equal
from mamba import description, it, context

from gol.cell import AliveCell, DeadCell
from gol.point import Point
from gol.world import World

EXAMPLE_MAP = "..*.\n" \
              ".**.\n" \
              ".*.."

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
            expect(repr(World.from_string(EXAMPLE_MAP))).to(equal(EXAMPLE_MAP))

    with it("computes new state of the world on each tick"):
        world = World.from_string(EXAMPLE_MAP)
        world.tick()
        expect(repr(world)).to(equal(".**.\n"
                                     ".**.\n"
                                     ".**."))
