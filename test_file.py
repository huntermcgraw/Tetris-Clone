import unittest
from tetris import check_lines, drop_collision_check

"""
Rotate() Function input:
[[500, 150, <Surface(50x50x32 SW)>], [500, 100, <Surface(50x50x32 SW)>], [550, 150, <Surface(50x50x32 SW)>], [450, 100, <Surface(50x50x32 SW)>]]
'clockwise'
[[1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1], [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1], [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1], [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1], [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1], [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1], [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1], [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1], [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1], [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1], [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1], [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1], [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1], [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1], [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1], [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1], [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1], [1, 1, 0, 0, 0, 0, 0, [550, 850, <Surface(50x50x32 SW)>], 0, 0, 0, 0, 1, 1, 1, 1], [1, 1, 0, 0, 0, [450, 900, <Surface(50x50x32 SW)>], [500, 900, <Surface(50x50x32 SW)>], [550, 900, <Surface(50x50x32 SW)>], 0, 0, 0, 0, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
0
'Z'

Returns:
[[500, 150, <Surface(50x50x32 SW)>], [550, 150, <Surface(50x50x32 SW)>], [500, 200, <Surface(50x50x32 SW)>], [550, 100, <Surface(50x50x32 SW)>]]
1
True
"""



class TestDropCollision(unittest.TestCase):
    def test_no_collision(self):
        board = [[0 for _ in range(16)] for _ in range(20)]
        for i, _ in enumerate(board):
            for j, _ in enumerate(board[i]):
                if i >= 19 or j <= 1 or j >= 12:
                    board[i][j] = 1

        board[11][3] = None
        array = [[500, 150, None], [450, 150, None], [550, 150, None], [550, 100, None]]

        self.assertEqual(drop_collision_check(array, board), False)

    def test_collision(self):
        board = [[0 for _ in range(16)] for _ in range(20)]
        for i, _ in enumerate(board):
            for j, _ in enumerate(board[i]):
                if i >= 19 or j <= 1 or j >= 12:
                    board[i][j] = 1
        array = [[500, 150, None], [450, 150, None], [550, 150, None], [550, 100, None]]

        self.assertEqual(drop_collision_check(array, board), False)

class TestCheckLines(unittest.TestCase):
    def test_no_full_line(self):
        before_board = [[0 for _ in range(16)] for _ in range(20)]
        for i, _ in enumerate(before_board):
            for j, _ in enumerate(before_board[i]):
                if i >= 19 or j <= 1 or j >= 12:
                    before_board[i][j] = 1
        after_board = [[0 for _ in range(16)] for _ in range(20)]
        for i, _ in enumerate(after_board):
            for j, _ in enumerate(after_board[i]):
                if i >= 19 or j <= 1 or j >= 12:
                    after_board[i][j] = 1
        self.assertEqual(check_lines(before_board), (after_board))

    def test_one_full_line(self):
        before_board = [[0 for _ in range(16)] for _ in range(20)]
        for i, _ in enumerate(before_board):
            for j, _ in enumerate(before_board[i]):
                if i >= 19 or j <= 1 or j >= 12:
                    before_board[i][j] = 1
        before_board[17] = [1, 1, [], [], [], [], [], [], [], [], [], [], 1, 1, 1, 1]
        before_board[18] = [1, 1, [], [], [], [], [], [], [], [], [], [], 1, 1, 1, 1]
        after_board = [[0 for _ in range(16)] for _ in range(20)]
        for i, _ in enumerate(after_board):
            for j, _ in enumerate(after_board[i]):
                if i >= 19 or j <= 1 or j >= 12:
                    after_board[i][j] = 1
        self.assertEqual(check_lines(before_board), (after_board, 2))


if __name__ == "__main__":
    unittest.main()