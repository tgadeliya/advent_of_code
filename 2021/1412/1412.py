from math import ceil
from collections import Counter


def get_input1(filename):
    with open(filename) as f:
        input = f.read().splitlines()
        seq = input[0]
        mapping = dict([x.split(" -> ") for x in input[2:]])
    return {"seq": seq, "map": mapping}


def get_solution1(input):
    n_steps = 10
    new_seq = perform_steps(input["seq"], input["map"], n_steps)
    c = Counter(new_seq).most_common()
    print(c)
    c_common = c[0][1]
    c_rare = c[-1][1]
    res = c_common - c_rare
    print("Solution to part1: ", res)


def perform_steps(seq, m, n):
    for i in range(n):
        seq = perform_step(seq, m)
    return seq

def perform_step(seq, m):
    d = [None] * (len(seq)-1)
    for i in range(len(seq)-1):
        d[i] = m[seq[i] + seq[i+1]]
    new_seq = [None] * (len(d) + len(seq))
    new_seq[1::2] = d
    new_seq[::2] = seq
    return new_seq


def get_solution2(input):
    seq, m = input["seq"], input["map"]
    up = {k: 0 for k, _ in m.items()}
    up_m = {k: [k[0]+v, v+k[1]] for k, v in m.items()}
    for i in range(1, len(seq)):
        up[seq[i-1]+seq[i]] += 1

    for i in range(40):
        up_t = {k: 0 for k, _ in m.items()}
        for k, v in up.items():
            for p in up_m[k]:
                up_t[p] += v
        up = up_t

    c = Counter(list(set(input["map"].values())))
    for k, v in up.items():
        c[k[0]] += v
        c[k[1]] += v
    c = c.most_common()

    c_common = c[0][1]
    c_rare = c[-1][1]
    res = c_common - c_rare
    print("Solution to part2: ", ceil(res/2))


if __name__ == "__main__":
    input = get_input1("input")
    get_solution1(input)
    get_solution2(input)
