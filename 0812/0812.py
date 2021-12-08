

NUM2SEG = {
    0: 6,
    1: 2,
    2: 5,
    3: 5,
    4: 4,
    6: 6,
    7: 3,
    8: 7,
    9: 6
}

seg2NUM = {
    2: 1,
    4: 4,
    3: 7,
    7: 8
}


def get_input(filename):
    with open(filename) as f:
        input =[line.split("|")[1].split(" ")[1:] for line in f.read().splitlines()]
    return input


def get_input2(filename):
    with open(filename) as f:
        input =[[x.split() for x in l.split(" | ")] for l in  f.read().splitlines()]
    return input


def solution_part1(input):
    sum = 0
    for line in input:
        lengths = [len(l) for l in line]
        for length in lengths:
            if length in seg2NUM.keys():
                sum += 1
    print(sum)


def solution_part2(input):
    sum = 0
    for line in input:
        segm, output = line
        number = get_number_given_inp(segm, output)
        print(number)
        sum += number
    print(sum)


def get_number_given_inp(seg, out):
    numbers = restore_given_seg(seg)
    res = ""
    for o in out:
        num = numbers["".join(sorted(o))]
        res += str(num)
    return int(res)

def restore_given_seg(seg):
    # 22222
    # 3   1
    # 3   1
    # 3   1
    # 44444
    # 5   7
    # 5   7
    # 5   7
    # 66666
    # len2num = {
    #     2: [1],
    #     3: [7],
    #     4: [4],
    #     5: [2,3,5],
    #     6: [0,6,9],
    #     7: [8],
    # }

    seg_len = [len(s) for s in seg]

    num2seqs = {
        1: set(seg[seg_len.index(2)]),
        4: set(seg[seg_len.index(4)]),
        7: set(seg[seg_len.index(3)]),
        8: set(seg[seg_len.index(7)]),
    }

    len2seqs = {
        2: [num2seqs[1]],
        3: [num2seqs[7]],
        4: [num2seqs[4]],
        5: [set(s) for s in seg if len(s) == 5],
        6: [set(s) for s in seg if len(s) == 6],
        7: [num2seqs[8]],
    }

    num2seqs[6] = [s for s in len2seqs[6] if abs(len(s - num2seqs[1]) - len(s)) == 1][0]
    num2seqs[3] = [s for s in len2seqs[5] if abs(len(s - num2seqs[1]) - len(s)) == 2][0]
    num2seqs[9] = num2seqs[3] | num2seqs[4]

    num2seqs[5] = num2seqs[9] - (num2seqs[8] - num2seqs[6])

    almost_zero = (num2seqs[8] - num2seqs[4]) | num2seqs[1]
    num2seqs[0] = [s for s in len2seqs[6] if len(s - almost_zero) == 1][0]
    num2seqs[2] = set([s for s in seg if set(s) not in num2seqs.values()][0])

    return {"".join(sorted(v)): k for k, v in num2seqs.items()}


if __name__ == "__main__":
    # input = get_input("input")
    # solution_part1(input)
    input2 = get_input2("input")
    solution_part2(input2)
