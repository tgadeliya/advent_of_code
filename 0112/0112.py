def get_input1():
    with open("input") as f:
        nums = f.read().splitlines()
    return [int(n) for n in nums]

def solution_part1(input):
    num_inc = 0
    for i in range(1, len(input)):
        prev = input[i - 1]
        curr = input[i]
        if curr > prev:
            num_inc += 1
    print(num_inc)

def solution_part2(input):
    num_slid_inc = 0
    sums = []
    for i in range(len(input)-2):
        sums.append(input[i] + input[i+1] + input[i+2])


    for i in range(1, len(sums)):
        if sums[i] > sums[i-1]:
            num_slid_inc += 1
    print(num_slid_inc)



if __name__ == "__main__":
    input1 = get_input1()
    solution_part1(input1)
    test = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
    solution_part2(input1)


