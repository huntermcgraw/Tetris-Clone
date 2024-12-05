import unittest
from tetris import check_lines, drop_collision_check, rotate, update_score, t_spin_check

class TestTSpinCheck(unittest.TestCase):
    board = [[1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1], [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
             [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1], [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
             [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1], [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
             [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1], [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
             [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1], [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
             [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1], [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
             [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1], [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
             [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1], [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
             [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1], [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
             [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
    def test_no_t_spin(self):
        array = [[500, 150, None], [500, 100, None], [550, 150, None], [450, 100, None]]
        self.assertEqual(t_spin_check(array, self.board), 0)

    def test_t_spin(self):
        array = [[100, 150, None], [100, 100, None], [150, 150, None], [50, 100, None]]
        board = self.board.copy()
        board[3][4] = [None]
        self.assertEqual(t_spin_check(array, board), 1)

class TestUpdateScore(unittest.TestCase):
    def test_t_spin_1_line(self):
        self.assertEqual(update_score(1, True, 0, True, 1), (1200, True))
    def test_t_spin_2_lines(self):
        self.assertEqual(update_score(2, True, 0, True, 2), (3600, True))
    def test_t_spin_3_lines(self):
        self.assertEqual(update_score(3, False, 0, True, 1), (1600, True))
    def test_1_line(self):
        self.assertEqual(update_score(1, False, 0, False, 3), (300, False))
    def test_2_lines(self):
        self.assertEqual(update_score(2, False, 0, False, 1), (300, False))
    def test_3_lines(self):
        self.assertEqual(update_score(3, False, 0, False, 5), (2500, False))
    def test_4_lines(self):
        self.assertEqual(update_score(4, False, 0, False, 2), (1600, True))



class TestRotate(unittest.TestCase):
    board = [[1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1], [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
             [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1], [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
             [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1], [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
             [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1], [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
             [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1], [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
             [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1], [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
             [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1], [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
             [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1], [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
             [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1], [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
             [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
    def test_rotate_clockwise_rot0(self):
        array = [[500, 150, None], [500, 100, None], [550, 150, None], [450, 100, None]]
        direction = 'clockwise'
        board = self.board.copy()
        board[17] = [1, 1, 0, 0, 0, 0, 0, [550, 850, None], 0, 0, 0, 0, 1, 1, 1, 1]
        board[18] = [1, 1, 0, 0, 0, [450, 900, None], [500, 900, None], [550, 900, None], 0, 0, 0, 0, 1, 1, 1, 1]
        rotations = 0
        piece_name = 'Z'
        self.assertEqual(rotate(array, direction, board, rotations, piece_name), ([[500, 150, None], [550, 150, None], [500, 200, None], [550, 100, None]], 1, True))

    def test_rotate_clockwise_rot1(self):
        array = [[500, 150, None], [500, 100, None], [550, 150, None], [450, 100, None]]
        direction = 'clockwise'
        board = self.board.copy()
        board[17] = [1, 1, 0, 0, 0, 0, 0, [550, 850, None], 0, 0, 0, 0, 1, 1, 1, 1]
        board[18] = [1, 1, 0, 0, 0, [450, 900, None], [500, 900, None], [550, 900, None], 0, 0, 0, 0, 1, 1, 1, 1]
        rotations = 1
        piece_name = 'Z'
        self.assertEqual(rotate(array, direction, board, rotations, piece_name), ([[500, 150, None], [550, 150, None], [500, 200, None], [550, 100, None]], 2, True))

    def test_rotate_clockwise_rot2(self):
        array = [[500, 150, None], [500, 100, None], [550, 150, None], [450, 100, None]]
        direction = 'clockwise'
        board = self.board.copy()
        board[17] = [1, 1, 0, 0, 0, 0, 0, [550, 850, None], 0, 0, 0, 0, 1, 1, 1, 1]
        board[18] = [1, 1, 0, 0, 0, [450, 900, None], [500, 900, None], [550, 900, None], 0, 0, 0, 0, 1, 1, 1, 1]
        rotations = 2
        piece_name = 'Z'
        self.assertEqual(rotate(array, direction, board, rotations, piece_name), ([[500, 150, None], [550, 150, None], [500, 200, None], [550, 100, None]], 3, True))

    def test_rotate_clockwise_rot3(self):
        array = [[500, 150, None], [500, 100, None], [550, 150, None], [450, 100, None]]
        direction = 'clockwise'
        board = self.board.copy()
        board[17] = [1, 1, 0, 0, 0, 0, 0, [550, 850, None], 0, 0, 0, 0, 1, 1, 1, 1]
        board[18] = [1, 1, 0, 0, 0, [450, 900, None], [500, 900, None], [550, 900, None], 0, 0, 0, 0, 1, 1, 1, 1]
        rotations = 3
        piece_name = 'Z'
        self.assertEqual(rotate(array, direction, board, rotations, piece_name), ([[500, 150, None], [550, 150, None], [500, 200, None], [550, 100, None]], 0, True))

    def test_rotate_counterclockwise(self):
        array = [[500, 150, None], [500, 100, None], [550, 150, None], [450, 100, None]]
        direction = 'counter-clockwise'
        board = self.board.copy()
        board[17] = [1, 1, 0, 0, 0, 0, 0, [550, 850, None], 0, 0, 0, 0, 1, 1, 1, 1]
        board[18] = [1, 1, 0, 0, 0, [450, 900, None], [500, 900, None], [550, 900, None], 0, 0, 0, 0, 1, 1, 1, 1]
        rotations = 0
        piece_name = 'Z'
        self.assertEqual(rotate(array, direction, board, rotations, piece_name),
                         ([[500, 150, None], [450, 150, None], [500, 100, None], [450, 200, None]], 3, True))

    def test_square(self):
        array = [[500, 150, None], [500, 100, None], [550, 150, None], [550, 100, None]]
        direction = 'counter-clockwise'
        board = self.board.copy()
        board[17] = [1, 1, 0, 0, 0, 0, 0, [550, 850, None], 0, 0, 0, 0, 1, 1, 1, 1]
        board[18] = [1, 1, 0, 0, 0, [450, 900, None], [500, 900, None], [550, 900, None], 0, 0, 0, 0, 1, 1, 1, 1]
        rotations = 0
        piece_name = 'O'
        self.assertEqual(rotate(array, direction, board, rotations, piece_name),
                         ([[500, 150, None], [500, 100, None], [550, 150, None], [550, 100, None]], 0, False))

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