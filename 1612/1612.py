res = 0
ress = ""

def type_id_mapping(tid:int):
    d = {
        0: "+",
        1: "*",
        2: "min",
        3: "max",
        5: ">=",
        6: "<=",
        7: "=="
    }
    return d.get(tid, "LOL"+str(tid))


def parse(packet):
    if packet == "":
        return 0, ""

    global res, ress
    literal_value = 0
    print("prev res:", res)
    V, T, packet = split_commands(packet)
    print(f"V={V}; T={T}")

    if T == 4:
        parts = []
        print("T=4")
        while packet[0] != "0":
            parts.append(packet[1:5])
            packet = packet[5:]

        parts.append(packet[1:5])
        literal_value = int("".join(parts), 2)
        ress += f" {str(literal_value)}"
        packet = packet[5:]
    else:
        ress += f"{type_id_mapping(T)}"

        LT = int(packet[0], 2)  # Length Type
        packet = packet[1:]
        print(f"LT={LT}")
        if LT == 1:  # Definied number of packets
            L = int(packet[:11], 2)  # Number of sub-packets
            packet = packet[11:]

            while L > 0:
                L -= 1
                lt, packet = parse(packet)
                literal_value += lt
        else:
            L = int(packet[:15], 2)  # Total packets length
            packet = packet[15:]
            remain = L
            while remain > 0:
                packet_len = len(packet)
                lt, packet = parse(packet)
                literal_value += lt
                remain -= (packet_len - len(packet))

    return literal_value, packet

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
    print("out:", parse(input))
    print("Solution to part1: ", res)

def get_solution2(input):
    print("out:", parse(input))
    print(ress)
    print("Solution to part2: ", ress)


if __name__ == "__main__":
    input = get_input1("input_test4")
    # get_solution1(input)
    get_solution2(input)

