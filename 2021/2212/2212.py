import typing as T
from dataclasses import dataclass


@dataclass
class cuboid:
    x: T.Tuple[int]
    y: T.Tuple[int]
    z: T.Tuple[int]
    l: int
    w: int
    h: int

    def __init__(self, xa, ya, za):
        self.x = xa
        self.y = ya
        self.z = za

        self.l = xa[1] - xa[0]
        self.w = ya[1] - ya[0]
        self.h = za[1] - za[0]

    @property
    def get_volume(self):
        return self.l * self.w * self.h


class Cuboid:
    def __init__(self, x_axis: T.List[int], y_axis: T.List[int], z_axis: T.List[int]):
        self.representation = [cuboid_coord(x_axis, y_axis, z_axis)]
        self.cube_num = self.count_cubes()

    def count_cubes(self):
        res = 0
        for c in self.representation:
            res += c.get_volume()
        return res


def cadd(c1: cuboid, c2: cuboid):
    pass

def c_overlap(c1: cuboid, c2:cuboid):
    """Return -1 if not overlap, return overlaping cuboid"""
    if :
        return -1
    else:
        x_over =
        y_over =
        z_over =
        return cuboid(x_over, y_over, z_over)






def get_input1(filename):
    with open(filename) as f:
        input = [line.strip() for line in f.readlines()]
    return input

def get_solution1(input):
    res = 0
    print("Solution to part1: ", res)

def get_solution2(input):
    res = 0
    print("Solution to part2: ", res)

if __name__ == "__main__":
    input = get_input1("input")
    get_solution1(input)
    get_solution2(input)
