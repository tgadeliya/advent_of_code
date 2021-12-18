from math import floor, ceil
import typing as T
import json


class SFN:
    def __init__(self, val, d=0, parent=None, side=None):
        self.init_val = val
        self.side = side
        self.d = d
        self.parent = parent

        if type(val[0]) is int and type(val[1]) is int:
            self.l = val[0]
            self.r = val[1]
        else:
            l, r = val
            self.l = SFN(l, d + 1, parent=self, side="l") if type(l) is list else l
            self.r = SFN(r, d + 1, parent=self, side="r") if type(r) is list else r

    def __repr__(self):
        return f" [{self.l},{self.r}]"

    def __add__(self, other):
        l = self.init_val
        r = other.init_val
        obj = SFN([l, r], 0)

        return obj


stop_explode_search = False
stop_split_search = False
stop_distribute = False

def split(N):
    def split_num(N):
        def get_split_num(N, side):
            val = N.l if side == 'l' else N.r
            return SFN([floor(val/2), ceil(val/2)], d=N.d + 1, parent=N, side=side)

        global stop_split_search
        if stop_split_search:
            return N

        if type(N) is int:
            return N
        elif (type(N.l) is int and N.l >= 10) or (type(N.r) is int and N.r >= 10):
            if type(N.l) is int and N.l >= 10:
                N.l = get_split_num(N, "l")
            else:
                N.r = get_split_num(N, "r")
            return N
        else:
            N.l = split(N.l)
            N.r = split(N.r)
        return N

    res = split_num(N)
    print("After split: ", res)
    return res


def swap_side(s):
    return "r" if s == "l" else "l"

def get_side_node(N, side):
    return N.r if side == "r" else N.l

def explode(N):

    def distr_to_f_occur(N, side, val):
        first = N.r if side == "r" else N.l
        second = N.l if side == "r" else N.r

        if type(first) is int:
            if side == "r":
                N.r += val
            else:
                N.l += val
            return
        else:
            distr_to_f_occur(first, side, val)

        if type(second) is int:
            if side == "r":
                N.r += val
            else:
                N.l += val
            return
        else:
            distr_to_f_occur(second, side, val)

    def distribute_to_side(N, side_of_exp, val):
        p = N.parent
        while not p is None:
            if (p.side is None) or p.side == side_of_exp:
                # We came from the side whether parent node is
                # So go higher
                p = p.parent
            else:
                # There is node near, so we can assign value
                # in this node
                node = get_side_node(p.parent, side_of_exp)
                if type(node) == int:
                    if side_of_exp == "r":
                        p.parent.r += val
                    else:
                        p.parent.l += val
                else:
                    distr_to_f_occur(node, swap_side(side_of_exp), val)
                return

    def find_explode_candidate(N):
        global stop_explode_search
        if stop_explode_search:
            return N

        if type(N) == int:
            return N
        elif type(N.l) is int and N.d == 4 and type(N.r) is int:
            stop_explode_search = True

            neigh_side = swap_side(N.side)
            neigh_node = get_side_node(N.parent, neigh_side)
            to_neigh_val = get_side_node(N, neigh_side)

            direction = N.side
            direction_val = get_side_node(N, direction)

            if type(neigh_node) == int:
                # Out neigh node is int, so we can use it
                neigh_int = get_side_node(N.parent, neigh_side)
                if neigh_side == "r":
                    N.parent.r += to_neigh_val
                else:
                    N.parent.l += to_neigh_val
            else:
                # Out neigh node is not int, so we need go deep and
                # choose first closest number to specified direction
                distr_to_f_occur(
                    neigh_node,
                    direction,
                    to_neigh_val
                )

            # Other side num should traverse higher and find closest
            distribute_to_side(N, N.side, direction_val)
            return 0
        else:
            N.l = find_explode_candidate(N.l)
            N.r = find_explode_candidate(N.r)

        return N

    global stop_explode_search
    res = find_explode_candidate(N)
    print("After explode:", res)
    stop_explode_search = False
    return res

def reduce(N):
    def iterate_till(op, N):
        N_prev = N
        N_act = op(N)

        while N_prev != N_act:
            N_prev = N_act
            N_act = op(N_act)
        return N_act

    global stop_explode_search
    global stop_split_search
    while True:

        N_red = N
        N_red_act = iterate_till(explode, N_red)

        N_red_act = iterate_till(split, N_red_act)
        stop_split_search = False

        if str(N_red) == str(N_red_act):
            break
        else:
            N_red = N_red_act

    return N

def get_number_magnitude(num):
    if type(num) is int:
        return num
    else:
        return 3 * get_number_magnitude(num.l) + 2 * get_number_magnitude(num.r)

def get_input(filename):
    with open(filename) as f:
        input = [SFN(json.loads(line)) for line in f.read().splitlines()]
    return input

def get_solution1(input):
    num_sum = input[0]  # TODO: Change to 0
    for i in range(1, len(input)):
        num_sum += input[i]
        num_sum = reduce(num_sum)
    res = get_number_magnitude(num_sum)
    print("Solution to part1: ", res)


def get_solution2(input):
    res = 0
    print("Solution to part2: ", res)


def test_split():
    test = [
        [[[[0, 7], 4], [15, [0, 13]]], [1, 1]],
        [[[[0, 7], 4], [[7, 8], [0, 13]]], [1, 1]],
        [[[[0, 7], 4], [[7, 8], [0, 7]]], [1, 1]],
    ]
    for t in test:
        num = SFN(t)
        print(num)
        num = split(num)
        print(num)
        print("--------")

def test_explode():
    test = [
        [[[[[4, 3], 4], 4], [7, [[8, 4], 9]]], [1, 1]],
        [[[[0, 7], 4], [7, [[8, 4], 9]]], [1, 1]],
        [[[[0, 7], 4], [[7, 8], [0, [6, 7]]]], [1, 1]]
    ]
    for t in test:
        num = SFN(t)
        print(num)
        num = explode(num)
        global stop_explode_search
        stop_explode_search = False
        # print(num)
        print("--------")

def test_reduce():
    test = [
        [[[[[4, 3], 4], 4], [7, [[8, 4], 9]]], [1, 1]],
    ]
    for t in test:
        num = SFN(t)
        # print(num)
        num = reduce(num)
        # print(num)
        print("--------")

if __name__ == "__main__":
    input = get_input("input_test")
    test_reduce()
    # test_explode()

    # get_solution1(input)
    # get_solution2(input)
