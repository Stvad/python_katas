from expects import expect, equal
from expects.matchers.built_in import not_, contain
from mamba import description, it

from gol.point import Point

with description("Point"):
    with it("neighbors should not include the point"):
        point = Point()
        expect(point.neighbors()).to(not_(contain(point)))

    with it("addition should perform by coordinate addition"):
        expect(Point() + Point(-1, 1)).to(equal(Point(-1, 1)))
