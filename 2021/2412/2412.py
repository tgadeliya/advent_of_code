class ALU:
    def __init__(self):
        self.w = 0
        self.x = 0
        self.y = 0
        self.z = 0

    def evaluate(self):
        pass

def get_input1(filename):
    with open(filename) as f:
        input = [line.strip().split(" ") for line in f.readlines()]
    return input

def get_solution1(input):
    res = 0
    comp = ALU()

    for instruction in input:
        comp.evaluate(instruction)

    print("Solution to part1: ", res)

def get_solution2(input):
    res = 0
    print("Solution to part2: ", res)

if __name__ == "__main__":
    input = get_input1("input")
    get_solution1(input)
    get_solution2(input)
