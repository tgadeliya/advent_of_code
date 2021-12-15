def get_input1(filename):
    with open(filename) as f:
        input = [[int(n) for n in list(line)] for line in f.read().splitlines()]
    return input

def get_solution1(input):
    res = calc_shortest_path(input)
    print("Solution to part1: ", res)

def get_solution2(input):
    res = 0
    print("Solution to part2: ", res)


def calc_shortest_path(input):
    """
    Not working dynamic programming solution :)
    """
    grid = [[0 for _ in range(len(input[0]))]for _ in range(len(input))]
    grid[0][0] = 0
    # precalc first col and first row
    for i in range(1, len(grid)):
        grid[i][0] = grid[i-1][0] + input[i][0]

    for j in range(1, len(input[0])):
        grid[0][j] = grid[0][j-1] + input[0][j]

    # precalc full table
    for i in range(1, len(grid)):
        for j in range(1,len(grid[0])):
                grid[i][j] = input[i][j] + min(grid[i-1][j], grid[i][j-1])

    # print(*["".join([str(n) for n in g]) for g in input], sep="\n")
    print(*[" ".join([str(n) for n in g]) for g in grid], sep="\n")

    return grid[-1][-1]

if __name__ == "__main__":
    input = get_input1("input_test2")
    get_solution1(input)
    get_solution2(input)
