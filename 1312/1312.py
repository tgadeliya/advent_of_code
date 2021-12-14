from copy import deepcopy

class Paper:
    def __init__(self, dots):
        self.dots = deepcopy(dots)
        self.folding_instr = []

    def fold(self, instructions):
        res = []
        for axis, line in instructions:
            self.fold_along(axis, line)
            res.append(len(self.dots))
            print(f"Dots after folding: {len(self.dots)}")
        return res

    def fold_along(self, axis, line):
        folded = set()
        for x,y in self.dots:
            xt, yt = x, y
            if axis == "x" and xt > line:
               xt = line - (xt - line)
            elif axis == "y" and yt > line:
               yt = line - (yt - line)

            folded.add((xt, yt))

        self.dots = list(folded)

    def fold_and_visualize(self, instructions):
        self.fold(instructions)
        self.visualize()

    def visualize(self):
        mh, mw = -1, -1
        for x, y in self.dots:
            mh = max(mh, x)
            mw = max(mw, y)

        grid = ["-" * (mw+1) for _ in range(mh+1)]
        for i, j in self.dots:
            ns = grid[i][:j] + "#" + grid[i][j+1:]
            grid[i] = ns
        grid = ["".join(l)[::-1] for l in list(map(list, zip(*grid[::-1])))]
        print(*grid, sep="\n")

def get_input1(filename):
    with open(filename) as f:
        input = f.read().splitlines()
        idx = input.index("")
        coords =[[int(n) for n in x.split(",")] for x in input[:idx]]
        instructions = [[x.split("=")[0][-1], int(x.split("=")[1])]for x in input[idx+1:]]
    print(coords)
    return {
        "coords": coords,
        "instructions": instructions
    }
def get_solution1(input):
    paper = Paper(input["coords"])
    res = paper.fold(input["instructions"])
    print("Solution to part1: ", res[0])

def get_solution2(input):
    paper = Paper(input["coords"])
    res = paper.fold_and_visualize(input["instructions"])

    print("Solution to part2: ", res)

if __name__ == "__main__":
    input = get_input1("input")
    get_solution1(input)
    get_solution2(input)
