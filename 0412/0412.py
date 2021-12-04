
class Board:
    def __init__(self, values):
        self.values = values
        self.bingo_list = [0 for _ in range(25)]
        self.val_list = [v for row in values for v in row]
        self.val_set = set(self.val_list)
        self.sum_of_values = sum([sum(row) for row  in values])
        self.bingo_app_seq = []

    def check_new_number(self, num):
        if num not in self.val_set:
            return -1
        else:
            self.bingo_app_seq.append(num)
            self.update_msk(num)
            res = self.check_msk()
            if not res:
                return -1
            else:
                remain_sum = self.sum_of_values - sum(self.bingo_app_seq)
                return num * remain_sum

    def update_msk(self, n):
        idx = self.val_list.index(n)
        self.bingo_list[idx] = 1

    def check_msk(self):
        for i in range(5):
            col_res = self.check_col(i)
            row_res = self.check_row(i)
            if col_res or row_res:
                return True
        return False

    def check_row(self, i):
        start_pos = 5 * i
        end_pos = start_pos + 5
        num_f = sum(self.bingo_list[start_pos:end_pos])
        return num_f == 5

    def check_col(self, i):
        res = sum([self.bingo_list[i + 5*j] for j in range(5)])
        return res == 5

def get_input(filename = "input"):
    with open(filename) as f:
        sequence = [int(n) for n in f.readline().split(",")]
        boards = [[int(n) for n in line.split()] for line in f.read().splitlines() if line != ""]
        boards_split = []
        assert len(boards) % 5 == 0
        num_boards = len(boards) // 5
        for board_idx in range(num_boards):
            boards_split.append(boards[board_idx * 5: (board_idx+1) * 5])
    return sequence, boards_split


def solution_part1(seq, board_vals):
    boards_obj = [Board(board_val) for board_val in board_vals]
    for num in seq:
        for board in boards_obj:
            res = board.check_new_number(num)
            if res != -1:
                return res

def solution_part2(seq, board_vals):
    boards_obj = [Board(board_val) for board_val in board_vals]
    win_idx = []
    for num in seq:
        for i in range(len(boards_obj)):
            res = boards_obj[i].check_new_number(num)
            if res != -1 and i not in win_idx:
                print(i, res)
                win_idx.append(i)

if __name__ == "__main__":
    sequence, boards = get_input("input")
    # solution1 = solution_part1(sequence, boards)
    solution_part2(sequence, boards)

