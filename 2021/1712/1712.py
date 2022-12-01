from dataclasses import dataclass
import typing as T


@dataclass
class Point:
    x: int
    y: int

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, x: int, y: int):
        self.x += x
        self.y += y

@dataclass
class Velocity:
    x: int
    y: int

@dataclass
class Target:
    x_bound: T.Tuple[int, int]
    y_bound: T.Tuple[int, int]

    def __init__(self, x_b, y_b):
        self.x_bound = x_b
        self.y_bound = y_b

    def is_inside(self, p: Point):
        inside_x = self.x_bound[0] <= p.x <= self.x_bound[1]
        inside_y = self.y_bound[0] <= p.y <= self.y_bound[1]
        return inside_x and inside_y

    def is_reachable(self, p: Point):
        # inside_x = p.x <= self.x_bound[1]
        # print(p)
        inside_y = self.y_bound[0] <= p.y
        return inside_y



class Trajectory:
    def __init__(self, init_vel: Velocity, target: Target):
        self.pos = Point(0, 0)
        self.av = init_vel
        self.max_h = 0  # CHECK
        self.t = target

    def calculate_traj(self):
        while True:
            self.perform_step()
            if self.t.is_inside(self.pos):
                # print("INSIDE")
                break
            if not self.t.is_reachable(self.pos):
                # print("NOT REACHABLE")
                self.max_h = -1
                break
            # print(self.pos)

        return self.max_h

    def stop_searching(self):
        # if self.t.x_bound[0] <= self.pos.x <= self.t.x_bound[1] and self.pos.y > self.t.y_bound[0]:
        #     return True

        success_stop = self.t.is_inside(self.pos)
        unsuccess_stop = self.t.is_reachable(self.pos)
        if success_stop:
            return True
        if unsuccess_stop:
            self.max_h = -1
            return False
        return True

    def perform_step(self):
        self.add_velocity_to_pos()
        # update velocity
        self.update_velocity()
        # update height
        self.max_h = max(self.max_h, self.pos.y)
        return self.pos

    def add_velocity_to_pos(self):
        xv, yv = self.av.x, self.av.y
        self.pos.add(xv, yv)

    def update_velocity(self):
        if self.av.x != 0:
            self.av.x -= (1 if self.av.x > 0 else -1)
        self.av.y -= 1


def get_input1(filename):
    with open(filename) as f:
        input = f.readline().strip().replace("target area: ", "")
        x, y = input.split(", ")
        xb, yb = x.replace("x=", "").split(".."), y.replace("y=", "").split("..")
        x_b = [int(x) for x in xb]
        y_b = [int(x) for x in yb]
    return Target(x_b, y_b)

def get_solution1(input):
    max_h = -1
    for i in range(0, 500):
        for j in range(0, 500):
            vel = Velocity(i, j)
            traj = Trajectory(vel, input)
            max_h_t = traj.calculate_traj()
            max_h = max(max_h, max_h_t)

    print("Solution to part1: ", max_h)

def get_solution2(input):
    res = 0
    res_l = []
    for i in range(-500, 500):
        for j in range(-500, 500):
            vel = Velocity(i, j)
            traj = Trajectory(vel, input)
            max_h_t = traj.calculate_traj()
            # return 0
            if max_h_t != -1:
                res += 1
                res_l.append((i,j))
    # print(sorted(res_l))
    print("Solution to part2: ", res)

if __name__ == "__main__":
    input = get_input1("input")
    # get_solution1(input)
    get_solution2(input)
