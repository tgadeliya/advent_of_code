import operator
from collections import deque
from functools import reduce

res = 0

def type_id_mapping(tid:int):
    d = {
        0: sum,
        1: lambda x: reduce(operator.mul, x, 1),
        2: min,
        3: max,
        4: lambda x: x[0],
        5: lambda x: operator.__gt__(x[0], x[1]),
        6: lambda x: operator.__lt__(x[0], x[1]),
        7: lambda x: operator.__eq__(x[0], x[1]),
    }
    return d.get(tid, None)


def parse(packet):
    if packet == "":
        return 0, ""

    global res, ress
    res_t = {"op": None, "lv": []}
    V, T, packet = split_commands(packet)

    res_t["op"] = type_id_mapping(T)
    if T == 4:
        parts = []
        while packet[0] != "0":
            parts.append(packet[1:5])
            packet = packet[5:]

        parts.append(packet[1:5])
        literal_value = int("".join(parts), 2)
        res_t["lv"].append(literal_value)
        packet = packet[5:]
    else:
        LT = int(packet[0], 2)  # Length Type
        packet = packet[1:]
        if LT == 1:  # Definied number of packets
            L = int(packet[:11], 2)  # Number of sub-packets
            packet = packet[11:]

            while L > 0:
                L -= 1
                lt, packet = parse(packet)
                res_t["lv"].append(lt)
        else:
            L = int(packet[:15], 2)  # Total packets length
            packet = packet[15:]
            remain = L
            while remain > 0:
                packet_len = len(packet)
                lt, packet = parse(packet)
                res_t["lv"].append(lt)
                remain -= (packet_len - len(packet))

    print(res_t)
    res_t = res_t["op"](res_t["lv"])
    return res_t, packet


def split_list(l, p):
    div, mod = divmod(len(l), p)
    return [l[div*i: div * (i+1)] for i in range(p)]


def split_commands(l):
    return int(l[:3], 2), int(l[3:6], 2), l[6:]


def get_input1(filename):
    with open(filename) as f:
        input = list(f.readline().strip())
    return to_binary(input)


def to_binary(inp):
    return "".join(["{:b}".format(int(n, 16)).zfill(4) for n in inp])


def get_solution1(input):
    parse(input)
    print("Solution to part1: ", res)


def get_solution2(input):
    res, _ = parse(input)
    print("Solution to part2: ", int(res))


def parsee(e):
    ee = e.popleft()
    if ee in (min, max):
        return ee()
    if type(ee) != int:
        return ee(parsee(e), parsee(e))
    else:
        return ee

if __name__ == "__main__":
    input = get_input1("input")
    # get_solution1(input)
    get_solution2(input)

