import typing as T
import numpy as np

m = {
    ".": 0,
    "#": 1
}
mapping: T.Dict

def get_input1(filename):
    global mapping
    with open(filename) as f:
        mapping = [m[p] for p in f.readline().strip()]
        f.readline()
        image = [list(map(lambda x: m[x], line)) for line in f.read().splitlines()]
    return {
        "image": np.array(image)
    }

def get_solution1(input):
    image = input["image"]
    image = perform_n_steps(image, 2)
    print("Solution to part1: ", np.sum(image))

def get_solution2(input):
    image = input["image"]
    image = perform_n_steps(image, 50)
    print("Solution to part1: ", np.sum(image))

def pad_value_given_step(i):
    if i == 0:
        return 0 # "."
    else:
        pad = mapping[0]
        for j in range(1,i):
            pad = mapping[-1] if pad == 1 else mapping[0]
        return pad # char -> int


def perform_n_steps(image, n_steps):
    for i in range(n_steps):
        image = np.pad(image, (2, 2), constant_values=pad_value_given_step(i))
        image = perform_step(image)

    return image

def perform_step(image):
    new_image = np.copy(image[1:-1, 1:-1])
    for i in range(1, len(image)-1):
        for j in range(1, len(image[0])-1):
            ne = get_element(i, j, image)
            new_image[i-1][j-1] = ne

    return new_image

def get_element(i, j, image):
    def l2s(l):
        return "".join([str(e) for e in l])
    g = [l2s(image[k][j-1:j+2]) for k in [i-1, i, i+1]]
    string_num = "".join(g)
    number = int(string_num, 2)
    return mapping[number]



if __name__ == "__main__":
    input = get_input1("input")
    # get_solution1(input)
    get_solution2(input)
