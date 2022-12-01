
def get_input(filename):
    with open(filename) as f:
        input = [int(n) for n in f.readline().split(",")]
    return input


def get_solution1(input):
    inp = input
    new_fish = []
    for i in range(80):
        num_zeros = 0
        for j in range(len(inp)):
            if inp[j] == 0:
                num_zeros += 1
                inp[j] = 6
            else:
                inp[j] -= 1
        for c in range(len(new_fish)):
            if new_fish[c][1] == 0:
                new_fish[c][1] = 6
                num_zeros += new_fish[c][0]
            else:
                new_fish[c][1] -= 1

        new_fish.append([num_zeros, 8])
    added = sum([f for f, d in new_fish])
    print(len(inp) + added)

def get_solution2(input):
    inp = input
    new_fish = []
    for i in range(256):
        num_zeros = 0
        for j in range(len(inp)):
            if inp[j] == 0:
                num_zeros += 1
                inp[j] = 6
            else:
                inp[j] -= 1
        for c in range(len(new_fish)):
            if new_fish[c][1] == 0:
                new_fish[c][1] = 6
                num_zeros += new_fish[c][0]
            else:
                new_fish[c][1] -= 1

        new_fish.append([num_zeros, 8])
    added = sum([f for f, d in new_fish])
    print(len(inp) + added)

if __name__ == "__main__":
    input = get_input("input")
    get_solution1(input)
    get_solution2(input)
