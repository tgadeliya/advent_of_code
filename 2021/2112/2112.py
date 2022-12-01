from collections import Counter

import numpy as np


class Game:
    def __init__(self, p1_start, p2_start):
        self.p1_pos = p1_start
        self.p2_pos = p2_start

        self.p1_score = 0
        self.p2_score = 0

        self.step = 1


    def play_game(self):
        while self.p1_score < 1000 and self.p2_score < 1000:
            self.p1_pos = ((self.p1_pos + self.roll3()) - 1) % 10 + 1
            self.p1_score += self.p1_pos

            if self.p1_score >= 1000:
                print(f"LOL As step={self.step}: p1={self.p1_score} , p2={self.p2_score}")
                return (self.step-1) * self.p2_score

            self.p2_pos = ((self.p2_pos + self.roll3()) - 1) % 10 + 1
            self.p2_score += self.p2_pos
            print(f"As step={self.step}: p1={self.p1_score} , p2={self.p2_score}")
        loser_score = min(self.p1_score, self.p2_score)
        return self.step * loser_score

    def roll3(self):
        res = 0
        for _ in range(3):
            res += roll_at_step(self.step)
            self.step += 1
        return res


def roll_at_step(step: int):
    return (step-1) % 100 + 1


def get_input1(filename):
    with open(filename) as f:
        p1 = f.readline().strip().split("starting position: ")[1]
        p2 = f.readline().strip().split("starting position: ")[1]
    return {"p1":int(p1), "p2": int(p2)}

def get_solution1(input):
    game = Game(input["p1"], input["p2"])
    res = game.play_game()
    print("Solution to part1: ", res)

def get_solution2(input):
    def gng(p):
        return [v for k,v in p]
    p1l = simulate_player(0, input["p1"], 0, 1).most_common()
    p2l = simulate_player(0, input["p2"], 0, 1).most_common()

    print(p1l)
    print(p2l)
    print( sum(gng(p1l)) )
    print( sum(gng(p2l)) - 32562 )

    p1_wins = 0
    p2_wins = 0

    print(f'{p1_wins:,}', p2_wins)
    print("Solution to part2: ", max(p1_wins, p2_wins))




def simulate_player(score, pos, depth, comb):
    if score >= 21:
        return Counter({depth: comb})
    else:
        c = Counter()
        for value, n_rep in [(6, 7), (5, 6), (7, 6), (4, 3), (8, 3), (3, 1), (9, 1)]:
            new_pos = ((pos + value) - 1) % 10 + 1
            new_score = score + new_pos
            # print(f"pos: {pos} -> {new_pos} ({value}); score: {score} -> {new_score}; comb={comb} & d={depth}")
            c += simulate_player(new_score, new_pos, depth+1, comb * n_rep)
        return c


def simulate_player(score, pos, depth, comb):
    if score >= 21:
        return Counter({depth: comb})
    else:
        c = Counter()
        for value, n_rep in [(6, 7), (5, 6), (7, 6), (4, 3), (8, 3), (3, 1), (9, 1)]:
            new_pos = ((pos + value) - 1) % 10 + 1
            new_score = score + new_pos
            # print(f"pos: {pos} -> {new_pos} ({value}); score: {score} -> {new_score}; comb={comb} & d={depth}")
            c += simulate_player(new_score, new_pos, depth+1, comb * n_rep)
        return c


def tests():
    print("testing roll_at_step")
    for i in [1, 100, 101, 999, 1000, 1001]:
        print(f"i={i}: roll = {roll_at_step(i)}")



if __name__ == "__main__":
    input = get_input1("input_test")
    # res = simulate_player(0, input["p1"], 0, 1).most_common()[::-1]
    # print(res)
    # get_solution1(input)
    get_solution2(input)
