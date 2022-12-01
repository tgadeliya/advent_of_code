from collections import defaultdict


class Cave:
    def __init__(self, vertices_pairs):
        self.g = self.build_graph(vertices_pairs)
        self.vertices = [k for k,v in self.g.items()]
        self.vertices_small = [v for v in self.vertices if v.islower()]

    def build_graph(self, vertices_pairs):
        g = defaultdict(list)
        for v1, v2 in vertices_pairs:
            g[v1].append(v2)
            g[v2].append(v1)
        return g

    def find_ways_from_start_to_end(self, small_node_max_vis=1):
        complete_pathes = []

        queue = []
        actual_path = []
        queue.append("start")
        actual_path.append("start")

        def step(node, prev_p):
            if node == "end":
                complete_pathes.append(prev_p + ["end"])
            elif node in self.vertices_small and (prev_p.count(node) > small_node_max_vis - 1):
                return None
            else:
                for v in self.g[node]:
                    if v != "start":
                        step(v, prev_p + [node])

        step("start", [])
        return len(complete_pathes)

    def pretty_print(self, l):
        print(
            "\n".join([",".join(p) for p in l])
        )

    def find_ways_from_start_to_end2(self):
        complete_pathes = []

        queue = []
        actual_path = []
        queue.append("start")
        actual_path.append("start")

        def step(node, prev_p):
            if node == "end":
                complete_pathes.append(prev_p + ["end"])
            elif node in self.vertices_small and (any([prev_p.count(vs)>1  for vs in self.vertices_small]) and prev_p.count(node)>0):
                return None
            else:
                for v in self.g[node]:
                    if v != "start":
                        step(v, prev_p + [node])

        step("start", [])
        return len(complete_pathes)

def get_input1(filename):
    with open(filename) as f:
        input = [line.strip().split("-") for line in f.readlines()]
    return input


def get_solution1(input):
    g = Cave(input)
    res = g.find_ways_from_start_to_end()
    print("Solution to part1: ", res)


def get_solution2(input):
    g = Cave(input)
    res = g.find_ways_from_start_to_end2()
    print("Solution to part2: ", res)



if __name__ == "__main__":
    input = get_input1("input")
    get_solution1(input)
    get_solution2(input)
