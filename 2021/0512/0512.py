from collections import Counter

def get_input(filename = "input"):
    with open(filename) as f:
        sequences = f.readlines()

    sequences = [s.strip().split("->") for s in sequences]
    seqs_parsed = []
    for pair in sequences:
        a, b = pair[0].split(","), pair[1].split(",")
        a = [int(aa) for aa in a]
        b = [int(bb) for bb in b]
        seqs_parsed.append((a, b))

    # filter only hor and vertical
    # seqs_parsed = [p for p in seqs_parsed if (p[0][0] == p[1][0] or p[0][1] == p[1][1])]

    return seqs_parsed


def produce_line(pair):
    a, b = pair
    if a[0] == b[0]:
        fixed_pos = 0
        not_f_pos = 1
    else:
        fixed_pos = 1
        not_f_pos = 0

    start = min(a[not_f_pos], b[not_f_pos])
    end = max(a[not_f_pos], b[not_f_pos]) + 1
    line_points = []
    for i in range(start, end):
        point = list(a)
        point[not_f_pos] = i
        line_points.append(tuple(point))
    return line_points

def produce_diag_line(pair):
    # print(pair)
    a, b = pair

    x_min, x_max = min(a[0], b[0]), max(a[0], b[0])
    y_min, y_max = min(a[1], b[1]), max(a[1], b[1])
    x_coords = list(range(x_min, x_max+1))
    y_coords = list(range(y_min, y_max+1))

    x_coords = x_coords[::-1] if a[0] > b[0] else x_coords
    y_coords = y_coords[::-1] if a[1] > b[1] else y_coords


    # print(x_coords, y_coords)
    # print(list(zip(x_coords, y_coords)))
    # print("____")
    return list(zip(x_coords, y_coords))


def get_solution1(input):
    points = []
    for pair in input:
        line_points = produce_line(pair)
        points.extend(line_points)
    counted = len([val for p, val in Counter(points).most_common() if val > 1])
    return counted


def get_solution2(input):
    points = []
    for p in input:
        if p[0][0] == p[1][0] or p[0][1] == p[1][1]:
            line_points = produce_line(p)
        else:
            line_points = produce_diag_line(p)
        points.extend(line_points)
        counted = len([val for p, val in Counter(points).most_common() if val > 1])
    return counted

if __name__ == "__main__":
    input = get_input("input")
    # solution1 = get_solution1(input)
    # print(solution1)
    solution2 = get_solution2(input)
    print(solution2)