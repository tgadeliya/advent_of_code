scorem = {
    ")": 3, "]": 57, ">": 25137, "}": 1197
}
m = {
    ")": "(", "]": "[", "}": "{", ">": "<"
}


def get_input1(filename):
    with open(filename) as f:
        input = [line.strip() for line in f.readlines()]
    return input


def get_solution1(input):
    res = 0
    for string in input:
        status, out = is_string_balanced(string)
        if status == "incomplete":
            continue
        elif status == "corrupted":
            res += scorem[out]
    print(res)

def get_solution2(input):
    res = []
    ms = {"]":2, ">":4, ")":1, "}":3}
    mss = {"[":"]", "<":">", "(":")", "{":"}"}

    for string in input:
        res_t = 0
        status, out = is_string_balanced(string)
        if status == "incomplete":
            for o in out[::-1]:
                res_t *= 5
                inv = mss[o]
                res_t += ms[inv]
            res.append(res_t)
        elif status == "corrupted":
            continue
    res_s = sorted(res)
    print(res_s[len(res_s)//2])

def is_string_balanced(s):
    stack = []
    for c in s:
        if c in "({[<":
            stack.append(c)
        else:
            if stack[-1] == m[c]:
                stack.pop()
            else:
                return "corrupted", c
    return ("complete", stack) if len(stack) == 0 else ("incomplete", stack)

if __name__ == "__main__":
    input = get_input1("input")
    get_solution1(input)
    get_solution2(input)