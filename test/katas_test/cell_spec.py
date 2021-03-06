from expects import expect, be_an, be_a
from mamba import description, it, context

from gol.cell import AliveCell, DeadCell

with description("Cell") as self:
    with context("Lifecycle"):
        with it("should die and stay dead when there is < 2 neighbors"):
            expect(AliveCell().tick(1)).to(be_a(DeadCell))
            expect(DeadCell().tick(1)).to(be_a(DeadCell))

        with it("should come to life if there is 3 neighbors"):
            expect(DeadCell().tick(3)).to(be_an(AliveCell))

        with it("should stay dead or alive when there is 2 neighbors"):
            expect(DeadCell().tick(2)).to(be_an(DeadCell))
            expect(AliveCell().tick(2)).to(be_an(AliveCell))

        with it("should die and stay dead if there is more then 3 neighbors"):
            expect(AliveCell().tick(4)).to(be_a(DeadCell))
            expect(DeadCell().tick(4)).to(be_a(DeadCell))
