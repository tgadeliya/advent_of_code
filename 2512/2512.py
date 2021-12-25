from copy import deepcopy


def get_input1(filename):
    with open(filename) as f:
        input = [list(line.strip()) for line in f.readlines()]
    return input


def perform_step(b):
    board = deepcopy(b)

    h = len(b)
    w = len(b[0])
    # move ">"
    move_right = []
    for i in range(h):
        for j in range(w):
            if board[i][j] == ">" and b[i][(j + 1) % w] == ".":
                move_right.append((i, j))

    for i, j in move_right:
        board[i][j] = "."
        board[i][(j+1) % w] = ">"


    move_down = []
    for i in range(h):
        for j in range(w):
            if board[i][j] == "v" and board[(i+1) % h][j] == ".":
                move_down.append((i, j))

    for i, j in move_down:
        board[i][j] = "."
        board[(i+1) % h][j] = "v"


    return board

def pp(b):
    print(*["".join(l) for l in b], sep="\n")

def is_eq(b1, b2):
    for i in range(len(b1)):
        if b1[i] != b2[i]:
            return False
    return True

def get_solution1(input):
    res = 0
    prev = deepcopy(input)
    act = deepcopy(input)

    act = perform_step(prev)
    res += 1


    while not is_eq(prev, act):
        prev = deepcopy(act)
        act = deepcopy(perform_step(act))
        res += 1

    print("Solution to part1: ", res)

def get_solution2(input):
    res = 0
    # TODO: Solve previous puzzles
    print("Solution to part2: ", res)


if __name__ == "__main__":
    input = get_input1("input")
    # tests(input)
    get_solution1(input)
    # get_solution2(input)
