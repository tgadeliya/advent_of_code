import typing as T
import copy

class CaveWithOctopuses:
    def __init__(self, inp):
        self.inp: T.List[T.List[int]] = copy.deepcopy(inp)
        self.n_steps = 0
        self.n_flashes = 0

    def get_actual_flashes(self):
        """Return num_flashes, steps_performed"""
        return self.n_flashes, self.n_steps

    def simulate_flashes_on_step(self):
        # coords of flash
        coords_to_flash = self.get_flash_coords()
        flashed = []

        while len(coords_to_flash) > 0:
            for x, y in coords_to_flash:
                self.perform_flash(x, y)
            flashed.extend(coords_to_flash)
            coords_to_flash = [x for x in self.get_flash_coords() if x not in flashed]

        for x,y in flashed:
            self.inp[x][y] = 0

    def simulate_steps(self, n_steps):
        for i in range(n_steps):
            self.increase_by_one()
            self.simulate_flashes_on_step()
            self.n_steps += 1

    def increase_by_one(self):
        for i in range(len(self.inp)):
            for j in range(len(self.inp[0])):
                self.inp[i][j] += 1

    def get_flash_coords(self):
        coords = []
        for i in range(len(self.inp)):
            for j in range(len(self.inp[0])):
                if self.inp[i][j] > 9:
                    coords.append((i, j))
        return coords

    def perform_flash(self, i, j):
        coords = self.get_adj_coord(i, j)
        for x, y in coords:
            self.inp[x][y] += 1
        self.n_flashes += 1

    def get_adj_coord(self, i, j):
        # lu u ru
        # l  c r
        # ld d rd
        coords = [
            (i-1, j), # u
            (i - 1, j-1),  # lu
            (i - 1, j+1),  # ru

            (i+1, j+1),  # rd
            (i+1, j-1),  # ld
            (i+1, j), # d

            (i, j+1), # r
            (i, j-1), # l
        ]

        return [(x,y) for x,y in coords if (x>=0 and y>=0) and (x < len(self.inp) and y < len(self.inp[0]))]

    def pretty_print(self):
        for i in range(len(self.inp)):
            print("  ".join([str(o) for o in self.inp[i]]), end="\n")
        print()

    def simulate_until_all_flash(self):
        step = 0
        while True:
            self.increase_by_one()
            self.simulate_flashes_on_step()
            step += 1
            if sum([sum(x) for x in self.inp]) == 0:
                return step

def get_input1(filename):
    with open(filename) as f:
        input = [list(map(int, line.strip())) for line in f.readlines()]
    return input


def get_solution1(input):
    cave = CaveWithOctopuses(input)
    cave.pretty_print()
    cave.simulate_steps(100)
    cave.pretty_print()
    res, _ = cave.get_actual_flashes()
    print("Solution to part1: ", res)

def get_solution2(input):
    cave = CaveWithOctopuses(input)
    cave.pretty_print()
    res = cave.simulate_until_all_flash()
    print("Solution to part2 ", res)


if __name__ == "__main__":
    input = get_input1("input")
    get_solution1(input)
    get_solution2(input)
