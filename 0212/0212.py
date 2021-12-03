def get_input1():
    with open("input") as f:
        nums = f.read().splitlines()
    return [n.split(" ") for n in nums]

def solution_part1(input):
    start_pos = [0, 0]
    for command, val in input:
        val = int(val)
        if command == "down":
            start_pos[1] += val
        elif command == "forward":
            start_pos[0] += val
        elif command == "up":
            start_pos[1] -= val
            
    print(start_pos, start_pos[0] * start_pos[1])

def solution_part2(input):
    start_pos = [0, 0]
    depth = 0
    for command, val in input:
        val = int(val)
        if command == "down":
            start_pos[1] += val
        elif command == "forward":
            start_pos[0] += val
            depth += val * start_pos[1]
        elif command == "up":
            start_pos[1] -= val
        print(start_pos, depth)
    print(depth, start_pos, start_pos[0] * depth)


if __name__ == "__main__":
    input1 = get_input1()
    solution_part1(input1)
    solution_part2(input1)
