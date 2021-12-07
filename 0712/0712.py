import numpy as np

def get_input(filename):
    with open(filename) as f:
        input = [int(n) for n in f.readline().split(",")]
    return input


def solution_part1(input):
    opt_pos = int(round(np.median(input)))
    print(sum([abs(n-opt_pos) for n in input]))

def solution_part2(input):
    """
    Solution with mean, but rounding problem

    """
    opt_pos = np.mean(input)
    print(calc_cost2(opt_pos, input))

def solution_part2(input):
    """bruteforce, because solution with mean round to wrong number"""
    resl = []
    opt_posl = []
    for i in range(max(input)):
        opt_pos = i
        opt_posl.append(opt_pos)

        res = calc_cost2(opt_pos, input)
        resl.append(res)

    best_opt_pos = opt_posl[np.argmin(resl)]
    print(best_opt_pos)
    print(calc_cost2(best_opt_pos, input))

def calc_cost2(opt_pos, input):
    res = 0
    for i in input:
        diff = abs(opt_pos - i)
        res += int((diff * (diff+1))/2)
    return res

if __name__ == "__main__":
    input = get_input("input")
    solution_part1(input)
    solution_part2(input)