def get_input1():
    with open("input") as f:
        nums = f.read().splitlines()
    return [n for n in nums]

def get_input_test():
    with open("input_test") as f:
        nums = f.read().splitlines()
    return [n for n in nums]


def get_ones(inp, i):
    c = 0
    for s in inp:
        c += 1 if s[i] == "1" else 0
    return c


def solution_part1(input):
    num = len(input)
    l = len(input[0])

    pos_ones = [get_ones(input, i) for i in range(l)]
    gamma = ["1" if nones > (num - nones) else "0" for nones in pos_ones]
    epsilon = ["1" if n == "0" else "0" for n in gamma]

    print(gamma, epsilon)
    gamma = int("".join(gamma), 2)
    epsilon = int("".join(epsilon), 2)
    print(gamma, epsilon, gamma * epsilon)


def get_c_numbers(input, idx):
    print(len(input), idx)
    l = len(input)
    if l == 1:
        return -1, input[0]

    ones = sum([int(i[idx]) for i in input])
    if ones > (l - ones):
        new_input = [i for i in input if i[idx] == "1"]
        mode_num = "1"
    elif ones == (l - ones):
        new_input = [i for i in input if i[idx] == "1"]
        mode_num = "1"
    else:
        new_input = [i for i in input if i[idx] == "0"]
        mode_num = "0"

    return mode_num, new_input

def get_l_numbers(input, idx):
    print(len(input), idx)
    l = len(input)
    if l == 1:
        return -1, input[0]

    ones = sum([int(i[idx]) for i in input])
    if ones < (l - ones):
        new_input = [i for i in input if i[idx] == "1"]
        mode_num = "1"
    else:
        new_input = [i for i in input if i[idx] == "0"]
        mode_num = "0"
    return mode_num, new_input


def solution_part2(input):
    l = len(input[0])

    inp = input
    i = 0
    cnum = 1
    while cnum != -1:
        cnum, inp = get_c_numbers(inp, i)
        i += 1
    ox_gen = list(inp)

    inp = input
    i = 0
    cnum = 1
    while cnum != -1:
        cnum, inp = get_l_numbers(inp, i)
        i += 1
    
    cru = list(inp)
    
    print("".join(ox_gen))
    print("".join(cru))
    print(int("".join(ox_gen), 2) * int("".join(cru), 2))

if __name__ == "__main__":
    input1 = get_input1()
    # solution_part1(input1)
    test = get_input_test()
    solution_part2(input1)
