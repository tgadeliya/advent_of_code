import numpy as np
from collections import deque

def get_input1(filename):
    with open(filename) as f:
        input = [list(map(int, line.strip())) for line in f.readlines()]
    return input


def solution_part1(input):
    res = 0
    all_low_coord = []
    for i in range(len(input)):
        for j in range(len(input[0])):
            val = input[i][j]
            is_low = compare_location(input, i, j)
            if is_low:
                all_low_coord.append((i, j))
                res += val+1
    print(res)
    return all_low_coord

def compare_location(inp, i, j):
    def is_valid(x, y):
        left_up = x < 0 or y < 0
        down_right = x >= len(inp) or y >= len(inp[0])
        return False if left_up or down_right else True

    up = (i-1, j)
    down = (i+1, j)
    left = (i, j-1)
    right = (i, j+1)
    coord = [up, down, left, right]

    val = inp[i][j]
    is_low = True
    for x, y in coord:
        if is_valid(x, y):
            if val >= inp[x][y]:
                is_low = False
                break
    return is_low

def get_near_locations(inp, i, j):
    def is_valid(x, y):
        left_up = x < 0 or y < 0
        down_right = x >= len(inp) or y >= len(inp[0])
        return False if left_up or down_right else True

    up = (i-1, j)
    down = (i+1, j)
    left = (i, j-1)
    right = (i, j+1)
    coord = [up, down, left, right]

    val = inp[i][j]
    is_low = True
    for x, y in coord:
        if is_valid(x, y):
            if val >= inp[x][y]:
                is_low = False
                break
    to_visit = []
    return is_low


def solution_part2(input, lcoord):
    basin_sizes = []
    for i, j in lcoord:
        b_size = calc_basin_size(input, i, j)
        basin_sizes.append(b_size)
    elems = sorted(basin_sizes, reverse=True)[:3]
    res = np.prod(elems)
    print(elems)
    print(res)

def gen_near_vis(inp, i, j, visited):

    def is_valid(x, y):
        left_up = x < 0 or y < 0
        down_right = x >= len(inp) or y >= len(inp[0])
        return False if left_up or down_right else True

    u, d, l, r = (i-1, j), (i+1, j), (i, j-1), (i, j+1)
    coord = [u, d, l, r]
    coord = [x for x in coord if is_valid(x[0], x[1]) and (x[0], x[1]) not in visited and inp[x[0]][x[1]] != 9]
    new_c = []
    for x, y in coord:
        act_val = inp[i][j]
        pot_val = inp[x][y]
        if act_val < pot_val:
            new_c.append((x, y))

    return deque(new_c)

def calc_basin_size(input, i, j):
    visited = [(i,j)]
    res = 1
    to_visit: deque = gen_near_vis(input, i, j, visited)
    while len(to_visit) > 0:
        # print("---")
        # print(to_visit)
        x,y = to_visit.popleft()
        res += 1
        visited.append((x,y))
        new_vis = gen_near_vis(input, x, y, visited)
        new_vis = [x for x in new_vis if to_visit.count(x) == 0]
        to_visit.extend(new_vis)
    return res


if __name__ == "__main__":
    input = get_input1("input")
    all_low_coord = solution_part1(input)
    solution_part2(input, all_low_coord)
