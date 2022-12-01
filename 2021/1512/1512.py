from collections import deque
from itertools import chain
from queue import PriorityQueue

def get_input1(filename):
    with open(filename) as f:
        input = [[int(n) for n in list(line)] for line in f.read().splitlines()]
    return input

def get_solution1(input):
    start = 0,0
    end = len(input), len(input[0])
    res = a_star_search(input, start, end)
    print("Solution to part1: ", res)

def get_solution2(input):
    start = 0, 0
    end = len(input), len(input[0])
    res = a_star_search(input, start ,end)
    print("Solution to part2: ", res)


def a_star_search(grid, start, end):
    to_visit = PriorityQueue()
    to_visit.put([0, start])

    came_from = val_grid_like(grid, None)
    cost_so_far = val_grid_like(grid, 0)

    while not to_visit.empty():
        _, c = to_visit.get()

        if c == end:
            break

        for x, y in get_neighbours(grid, c[0], c[1]):
            new_cost = cost_so_far[c[0]][c[1]] + grid[x][y]
            if (not cost_so_far[x][y]) or new_cost < cost_so_far[x][y]:
                cost_so_far[x][y] = new_cost
                priority = new_cost
                to_visit.put([priority, (x, y)])
                came_from[x][y] = (c[0], c[1])

    return cost_so_far[-1][-1]

def generate_new_map(grid):
    new_grid = []
    for i in range(5):
        new_row = [increase_grid(grid, i)]
        for j in range(1, 5):
            up = i + j
            tile = increase_grid(grid, up)
            new_row.append(tile)
        new_row = [list(chain.from_iterable(p)) for p in zip(*new_row)]
        new_grid.extend(new_row)

    # print(*[ " ".join(map(str,p)) for p in  new_grid], sep="\n")
    return new_grid

def increase_grid(g, up):
    ng = val_grid_like(g, 1)
    for i in range(len(g)):
        for j in range(len(g[0])):
            ng[i][j] = g[i][j] + up
            if ng[i][j] > 9:
                ng[i][j] -= 9
    return ng

def get_neighbours(grid, x, y):
    n = [(x,y+1), (x,y-1), (x+1,y), (x-1, y)]
    return [p for p in n if (0 <= p[0] < len(grid)) and (0 <= p[1] < len(grid[0]))]


def val_grid_like(grid, val):
    return [ [val for _ in range(len(grid[0]))] for _ in range(len(grid))]

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
    input = get_input1("input")
    get_solution1(input)
    input2 = generate_new_map(input)
    get_solution2(input2)
