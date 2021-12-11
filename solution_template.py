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
