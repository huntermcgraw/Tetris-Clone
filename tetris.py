""" import random: random is needed to shuffle the pieces to make them random
    import time: Time will be needed to shift the pieces over the board
    import pygame: pygame is our main game framework
    import math: math is needed for some more complex calculations"""

import random
import time
import pygame
import math

# initialize pygame
pygame.init()

X_WIDTH = 1056
"""
Horizontal Width of the images for the game background
"""
Y_WIDTH = 960
"""
Vertical Width of the images for the game background
"""
info = pygame.display.Info()
"""
The video display information for the user’s screen
"""
scale = (info.current_h-80)/Y_WIDTH
"""
Used to scale the window to the user’s screen size, the ratio of screen to image
"""
UNIT = (48 * scale)
"""
The number of pixels between each grid.
"""
scale -= round(UNIT % 1, 8) / 48
UNIT = round(48 * scale)


def load_pixel_color(pixel_path="images/Pixel.png"):
    """
    Creates the colors dictionary used for each of the pieces
    :param pixel_path: (str) The file path to the 48x48 png being used for each square
    :return colors: (dict) the dictionary that contains each of the already colored pixel images
    """
    WHITE = pygame.image.load(pixel_path)
    w = WHITE.get_height()
    WHITE = pygame.transform.scale(WHITE, (w*scale, w*scale))
    colors = {
        "RED": WHITE.copy(),
        "ORANGE": WHITE.copy(),
        "YELLOW": WHITE.copy(),
        "GREEN": WHITE.copy(),
        "BLUE": WHITE.copy(),
        "PURPLE": WHITE.copy(),
        "TEAL": WHITE.copy(),
        "SHADOW": WHITE.copy()
    }
    colors["RED"].fill((255, 0, 0), special_flags=pygame.BLEND_MULT)
    colors["ORANGE"].fill((255, 128, 0), special_flags=pygame.BLEND_MULT)
    colors["YELLOW"].fill((255, 255, 0), special_flags=pygame.BLEND_MULT)
    colors["GREEN"].fill((0, 255, 0), special_flags=pygame.BLEND_MULT)
    colors["BLUE"].fill((0, 0, 255), special_flags=pygame.BLEND_MULT)
    colors["PURPLE"].fill((196, 0, 196), special_flags=pygame.BLEND_MULT)
    colors["TEAL"].fill((0, 255, 255), special_flags=pygame.BLEND_MULT)
    colors["SHADOW"].fill((50, 50, 50), special_flags=pygame.BLEND_MULT)
    return colors


def next_piece(piece_list):
    """
        Determines the next piece to use. uses traditional tetris algorithm to prevent droughts.
        :param piece_list: (list(str)) Contains the keys of pieces, that have not already been used, can be empty
        :return piece: (str) The piece to be used next
        :return piece_list: (list(str) Contains the keys of pieces, that have not already been used, can be empty
    """
    if not piece_list:
        piece_list = ["L", "T", "S", "Z", "I", "O", "J"]
        random.shuffle(piece_list)
    return piece_list.pop(0), piece_list


def generate_piece(piece_name="O", x=10 * UNIT, y=1 * UNIT, colors=None):
    """
        Takes a piece from next_piece or a piece from the user and generates the components
        at the desiRED locations for that piece. Can also get prompted with x,y to change the
        starting position of the home piece.
        :param piece_name: (str) one of these strings ["L", "T", "S", "Z", "I", "O", "J"] that describes which piece is currently being placed
        :param x; (int) the position in pixels of the x coordinate
        :param y: (int) the position in pixels of the y coordinate
        :param colors: (dict) the dictionary that contains each of the already colored pixel images
        :return: arr(arr(x, y, color)) The piece coordinates of the inputted piece name and it's color
    """
    RED = colors["RED"]
    ORANGE = colors["ORANGE"]
    YELLOW = colors["YELLOW"]
    GREEN = colors["GREEN"]
    BLUE = colors["BLUE"]
    PURPLE = colors["PURPLE"]
    TEAL = colors["TEAL"]
    key = {
        "L": [
            [x, y, ORANGE],
            [x - UNIT, y, ORANGE],
            [x + UNIT, y, ORANGE],
            [x + UNIT, y - UNIT, ORANGE],
        ],
        "T": [
            [x, y, PURPLE],
            [x, y - UNIT, PURPLE],
            [x - UNIT, y, PURPLE],
            [x + UNIT, y, PURPLE],
        ],
        "Z": [
            [x, y, RED],
            [x, y - UNIT, RED],
            [x + UNIT, y, RED],
            [x - UNIT, y - UNIT, RED],
        ],
        "S": [
            [x, y, GREEN],
            [x, y - UNIT, GREEN],
            [x + UNIT, y - UNIT, GREEN],
            [x - UNIT, y, GREEN],
        ],
        "I": [
            [x, y, TEAL],
            [x - UNIT, y, TEAL],
            [x + UNIT, y, TEAL],
            [x + UNIT * 2, y, TEAL],
        ],
        "O": [
            [x, y, YELLOW],
            [x, y - UNIT, YELLOW],
            [x + UNIT, y, YELLOW],
            [x + UNIT, y - UNIT, YELLOW],
        ],
        "J": [
            [x, y, BLUE],
            [x + UNIT, y, BLUE],
            [x - UNIT, y - UNIT, BLUE],
            [x - UNIT, y, BLUE],
        ],
    }
    return key[piece_name]


def get_next_check(interval):
    """
        gets the next time that returns the time <interval> away from the current time.
        :param interval: (int) how many ms away we want the next check
        :return: (int) the next interval
    """
    interval /= 1000
    current_time = time.time()
    return current_time + interval


def drop_piece(arr):
    """
        Moves the piece down 1 in the game board collision should be checked prior
        :param arr: (arr[arr[int]]) The current piece
    """
    for i in arr:
        i[1] += UNIT


def move_piece(arr, command):
    """
        Moves the piece left or right 1 in the game board collision should be checked prior
        :param arr: (arr[arr[int]]) The current piece
        :param command: (string) right or left to determine direction
    """
    if command == "right":
        for i in arr:
            i[0] += UNIT
    elif command == "left":
        for i in arr:
            i[0] -= UNIT


def create_board():
    """
        Creates an array for the game objects to be stored in
        :return: (arr[arr[int]]) The matrix containing the play board with the boards defining the play space
    """
    board = [[0 for _ in range(16)] for _ in range(20)]
    for i, _ in enumerate(board):
        for j, _ in enumerate(board[i]):
            if i >= 19 or j <= 1 or j >= 12:
                board[i][j] = 1
    return board


def stop_piece(arr, board):
    """
        Adds the current piece to the board
        :param arr: (arr[arr[int]]) The current piece
        :param board: (arr[arr[int]]) The game board
        :return: (arr[arr[int]]) The board after the piece is placed on the board
    """
    for i in arr:
        x, y = get_x_y(i)
        board[y][x] = i
    return board


def check_lines(board):
    """
        checks for full lines, clears them, and moves above rows down
        :param board: (arr[arr[int]]) The game board
        :return: (arr[arr[int]]) The board after full lines have been cleared
        :return: (int) The number of lines cleared
    """
    count = 0
    # clear lines add points and totals lines cleared
    new_line = [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0]
    # If the bottom row is empty all the rows have to be empty
    if board[18] == new_line:
        return board
    for line, _ in enumerate(board):
        # If the row is empty, skip it
        if board[line] != new_line:
            length = 0
            for column in board[line][2:]:
                # Checks to see if every spot on the board is a piece
                if isinstance(column, list):
                    length += 1
            # If every space in the line is a piece
            if length == 10:
                board.pop(line)  # Remove the line
                count += 1
                board.insert(0, new_line.copy())  # Add an empty line to the top of the board
                for row, _ in enumerate(board):
                    for space in board[row][2:]:
                        if row > line:  # Skips empty lines and lines below the cleared line
                            break
                        if isinstance(space, list):  # Moves everything down by one unit
                            space[1] += UNIT
    return board, count


def drop_collision_check(arr, board):
    """
        Checks to see if there is a block below or a border
        :param arr: (arr[arr[int]]) The current piece
        :param board: (arr[arr[int]]) The game board
        :return: (bool) True if the piece cannot move down by 1, False if the piece can move down by 1
    """
    for i in arr:
        x, y = get_x_y(i)
        if board[y + 1][x] != 0:
            return True
    return False


def right_collision_check(arr, board):
    """
        Checks to see if there is a block to the right or a border
        :param arr: (arr[arr[int]]) The current piece
        :param board: (arr[arr[int]]) The game board
        :return: (bool) True if the piece cannot move right by 1, False if the piece can move right by 1
    """
    for i in arr:
        x, y = get_x_y(i)
        if board[y][x + 1] != 0:
            return True
    return False


def left_collision_check(arr, board):
    """
        Checks to see if there is a block to the left or a border
        :param arr: (arr[arr[int]]) The current piece
        :param board: (arr[arr[int]]) The game board
        :return: (bool) True if the piece cannot move left by 1, False if the piece can move left by 1
    """
    for i in arr:
        x, y = get_x_y(i)
        if board[y][x - 1] != 0:
            return True
    return False


def review_check(arr, board):
    """
        Checks to see if the piece can be placed where it is trying to be placed or if something is already there
        :param arr: (arr[arr[int]]) The current piece
        :param board: (arr[arr[int]]) The game board
        :return: (bool) True if the piece cannot be placed, False if the piece can be placed
    """
    for i in arr:
        x, y = get_x_y(i)
        try:
            if board[y][x] != 0:
                return True
        except IndexError:
            return True
    return False


def rotate(arr, direction, board, rotations, piece_name):
    """
        rotates the piece by doing reflections over y=x and y=-x respective to
        the direction does not care about collision
        :param arr: (arr[arr[int]]) The current piece
        :param direction: (string) clockwise or counterclockwise for direction
        :param board: (arr[arr[int]]) The game board
        :param rotations: (int) how many rotations the current piece can do
        :param piece_name: (str) one of these strings ["L", "T", "S", "Z", "I", "O", "J"] that describes which piece is currently being placed
        :return: (arr[arr[int]]) The Piece being placed with its new coordinates
        :return: (int) How many rotations the piece did
        :return: (bool) Was the piece rotated
    """
    # excludes the O piece
    if piece_name == "O":
        return arr, rotations, False
    array_prev = []
    master_x, master_y = get_x_y(arr[0])
    for i in arr:
        array_prev.append(i.copy())
        x, y = get_x_y(i)
        x -= master_x
        y -= master_y
        if direction == "clockwise":
            x1 = -y
            y1 = x
            i[0] = (x1 + master_x) * UNIT
            i[1] = (y1 + master_y) * UNIT
        else:
            x1 = y
            y1 = -x
            i[0] = (x1 + master_x) * UNIT
            i[1] = (y1 + master_y) * UNIT
        i[0] += 4 * UNIT

    # change rotations
    if direction == "clockwise":
        final_rotation = (1 + rotations) % 4
    else:
        final_rotation = (-1 + rotations) % 4
    # separate I piece logic
    if piece_name == "I":
        # base check for ["I"]
        if direction == "clockwise":
            if rotations == 0:
                for i in arr:
                    i[0] += 1 * UNIT
            elif rotations == 2:
                for i in arr:
                    i[0] -= 1 * UNIT
            if rotations == 1:
                for i in arr:
                    i[1] += 1 * UNIT
            elif rotations == 3:
                for i in arr:
                    i[1] -= 1 * UNIT
        else:
            if rotations == 3:
                for i in arr:
                    i[0] += 1 * UNIT
            elif rotations == 1:
                for i in arr:
                    i[0] -= 1 * UNIT
            if rotations == 0:
                for i in arr:
                    i[1] += 1 * UNIT
            elif rotations == 2:
                for i in arr:
                    i[1] -= 1 * UNIT
        if not review_check(arr, board):
            return arr, final_rotation, True
        # second check
        if direction == "clockwise":
            if rotations == 0:
                for i in arr:
                    i[0] -= 2 * UNIT
            elif rotations == 1:
                for i in arr:
                    i[0] -= 1 * UNIT
            elif rotations == 2:
                for i in arr:
                    i[0] += 2 * UNIT
            elif rotations == 3:
                for i in arr:
                    i[0] += 1 * UNIT
        else:
            if rotations == 0:
                for i in arr:
                    i[0] -= 1 * UNIT
            elif rotations == 1:
                for i in arr:
                    i[0] += 2 * UNIT
            elif rotations == 2:
                for i in arr:
                    i[0] += 1 * UNIT
            elif rotations == 3:
                for i in arr:
                    i[0] -= 2 * UNIT
        if not review_check(arr, board):
            return arr, final_rotation, True
        # third check
        if direction == "clockwise":
            if rotations == 0 or rotations == 1:
                for i in arr:
                    i[0] += 3 * UNIT
            else:
                for i in arr:
                    i[0] -= 3 * UNIT
        else:
            if rotations == 1 or rotations == 2:
                for i in arr:
                    i[0] -= 3 * UNIT
            else:
                for i in arr:
                    i[0] += 3 * UNIT
        if not review_check(arr, board):
            return arr, final_rotation, True
        # fourth check
        if direction == "clockwise":
            if rotations == 0 or rotations == 1:
                for i in arr:
                    i[0] -= 3 * UNIT
            else:
                for i in arr:
                    i[0] += 3 * UNIT
        else:
            if rotations == 1 or rotations == 2:
                for i in arr:
                    i[0] += 3 * UNIT
            else:
                for i in arr:
                    i[0] -= 3 * UNIT
        if direction == "clockwise":
            if rotations == 0:
                for i in arr:
                    i[1] += 1 * UNIT
            elif rotations == 1:
                for i in arr:
                    i[1] -= 2 * UNIT
            elif rotations == 2:
                for i in arr:
                    i[1] -= 1 * UNIT
            elif rotations == 3:
                for i in arr:
                    i[1] += 2 * UNIT
        else:
            if rotations == 0:
                for i in arr:
                    i[1] -= 2 * UNIT
            elif rotations == 1:
                for i in arr:
                    i[1] -= 1 * UNIT
            elif rotations == 2:
                for i in arr:
                    i[1] += 2 * UNIT
            elif rotations == 3:
                for i in arr:
                    i[1] += 1 * UNIT
        if not review_check(arr, board):
            return arr, final_rotation, True
        # fifth check
        if direction == "clockwise":
            if rotations == 0 or rotations == 1:
                for i in arr:
                    i[0] += 3 * UNIT
            else:
                for i in arr:
                    i[0] -= 3 * UNIT
            if rotations == 0 or rotations == 3:
                for i in arr:
                    i[1] -= 3 * UNIT
            else:
                for i in arr:
                    i[1] += 3 * UNIT
        else:
            if rotations == 1 or rotations == 2:
                for i in arr:
                    i[0] += 3 * UNIT
            else:
                for i in arr:
                    i[0] -= 3 * UNIT
            if rotations == 0 or rotations == 1:
                for i in arr:
                    i[1] += 3 * UNIT
            else:
                for i in arr:
                    i[1] -= 3 * UNIT
        if not review_check(arr, board):
            return arr, final_rotation, True
        return array_prev, rotations, False
    # base check for ["L", "T", "S", "Z", "J"]
    if not review_check(arr, board):
        return arr, final_rotation, True
    # second check
    if direction == "clockwise":
        if rotations == 0 or rotations == 3:
            for i in arr:
                i[0] -= 1 * UNIT
        else:
            for i in arr:
                i[0] += 1 * UNIT
    else:
        if rotations == 1 or rotations == 2:
            for i in arr:
                i[0] += 1 * UNIT
        else:
            for i in arr:
                i[0] -= 1 * UNIT
    if not review_check(arr, board):
        return arr, final_rotation, True
    # third check
    if rotations == 0 or rotations == 2:
        for i in arr:
            i[1] -= 1 * UNIT
    else:
        for i in arr:
            i[1] += 1 * UNIT
    if not review_check(arr, board):
        return arr, final_rotation, True
    # fourth check
    if rotations == 0 or rotations == 2:
        for i in arr:
            i[1] += 3 * UNIT
    else:
        for i in arr:
            i[1] -= 3 * UNIT
    if direction == "clockwise":
        if rotations == 0 or rotations == 3:
            for i in arr:
                i[0] += 1 * UNIT
        else:
            for i in arr:
                i[0] -= 1 * UNIT
    else:
        if rotations == 0 or rotations == 1:
            for i in arr:
                i[0] -= 1 * UNIT
        else:
            for i in arr:
                i[0] += 1 * UNIT
    if not review_check(arr, board):
        return arr, final_rotation, True
    # fifth check
    if direction == "clockwise":
        if rotations == 0 or rotations == 3:
            for i in arr:
                i[0] -= 1 * UNIT
        else:
            for i in arr:
                i[0] += 1 * UNIT
    else:
        if rotations == 0 or rotations == 1:
            for i in arr:
                i[0] += 1 * UNIT
        else:
            for i in arr:
                i[0] -= 1 * UNIT
    if not review_check(arr, board):
        return arr, final_rotation, True
    return array_prev, rotations, False


def get_x_y(unit):
    """
        retrieves the x and y coordinate from the position on screen. this is where
        they are on the board array
        :param unit: (list[x(int),y(int),color]) the color is a pygame image that is displayed with a tint
        :return: (int), (int) The x and y coordinates of the piece in the game board matrix
    """
    x, y = int((unit[0] - 160*scale) / UNIT), int((unit[1]) / UNIT)
    return x, y


def display_piece(arr, display_screen):
    """
        prints the game piece to the board this is separate from the board array and
        is not contained in the array
        this function displays the current piece over the board.
        :param arr: (arr[arr[int]]) The current piece
        :param display_screen: (pygame.surface) pygame screen
    """
    if arr:
        for i in arr:
            display_screen.blit(i[2], (i[0], i[1]))


def display_board(board, display_screen):
    """
        This function displays board on the screen object
        :param board: (arr[arr[int]]) board
        :param display_screen: (pygame.surface) pygame screen
    """
    for i in board:
        for j in i:
            if j != 0 and j != 1:
                display_screen.blit(j[2], (j[0], j[1]))


def update_score(_lines, _btb_tetris, _score, _t_spin, _level):
    """updates score according to lines cleared, level and if it was a t_spin
        :param _lines: (int) # of lines cleared
        :param _btb_tetris: (bool) If there was a back-to-back tetris
        :param _score: (int) What the current score is
        :param _t_spin: (bool) If the last placement was a t-spin
        :param _level: (int) What level the game is currently on
        :return: (int) The player's score
        :return: (bool) Was there a back-to-back tetris
    """
    if _t_spin:
        if _lines == 1:
            _score += ((800 + _btb_tetris * 400)*_level)
            _btb_tetris = True
        elif _lines == 2:
            _score += ((1200 + _btb_tetris * 600)*_level)
            _btb_tetris = True
        elif _lines == 3:
            _score += ((1600 + _btb_tetris * 800)*_level)
            _btb_tetris = True
    elif _lines == 1:
        _score += 100*_level
        _btb_tetris = False
    elif _lines == 2:
        _score += 300*_level
        _btb_tetris = False
    elif _lines == 3:
        _score += 500*_level
        _btb_tetris = False
    elif _lines == 4:
        _score += ((800 + _btb_tetris * 400)*_level)
        _btb_tetris = True
    return _score, _btb_tetris


def update_difficulty(cleared_lines):
    """
    Changes difficulty/speed depending on how many lines have been cleared
    :param cleared_lines: (int) Number of lines cleared
    :return: (int) the difficulty
    """
    check = math.floor(cleared_lines/10)
    match check:
        case 0:
            return check+1, 800, 800
        case 1:
            return check+1, 716.67, 800
        case 2:
            return check+1, 633.33, 800
        case 3:
            return check+1, 550, 800
        case 4:
            return check+1, 466.67, 800
        case 5:
            return check+1, 383.33, 800
        case 6:
            return check+1, 300, 800
        case 7:
            return check+1, 216.67, 800
        case 8:
            return check+1, 133.33, 800
        case 9:
            return check+1, 100, 716.67
        case 10 | 11 | 12:
            return check+1, 83.33, 633.33
        case 13 | 14 | 15:
            return check+1, 66.67, 550
        case 16 | 17 | 18:
            return check+1, 50, 466.67
        case 19 | 20 | 21 | 22 | 23 | 24 | 25 | 26 | 27 | 28:
            return check+1, 33.33, 383.33
        case _:
            return check+1, 16.67, 300


def t_spin_check(arr, board):
    """
    Checks to see if a t-spin occurred
    :param arr: (arr[arr[int]]) The current piece
    :param board: (arr[arr[int]]) The game board
    :return: (bool) Was there a t-spin
    """
    count = 0
    x, y = get_x_y(arr[0])
    if board[y+1][x+1] != 0:
        count += 1
    if board[y-1][x+1] != 0:
        count += 1
    if board[y+1][x-1] != 0:
        count += 1
    if board[y-1][x-1] != 0:
        count += 1

    return count >= 3


def get_shadow(arr, board, colors):
    """
    Creates a "shadow" of the piece currently being placed and puts it at the lowest possible point the block
    can fall to
    :param arr: (arr[arr[int]]) The current piece
    :param board: (arr[arr[int]]) The game board
    :param colors: (dict) the dictionary that contains each of the already colored pixel images
    :return: (arr[arr[int]]) The shadow piece being "placed"
    """
    placeholder = []
    for item in arr:
        x, y, surface = item
        new_surface = surface.copy()
        placeholder.append([x, y, new_surface])
    for i in placeholder:
        i[2] = colors["SHADOW"]
    while not drop_collision_check(placeholder, board):
        drop_piece(placeholder)
    return placeholder


def play_tetris(screen, pixel_type):
    """
    Run the game
    :param screen: pygame screen the board is displayed on
    :param pixel_type: (int) Indicates which 48x48 Pixel#.png is being used
    :return: (int) The score the player ended the game with
    """
    board_image = pygame.image.load("images/Background.png")
    w, h = board_image.get_width(), board_image.get_height()
    board_image = pygame.transform.scale(board_image, (w*scale, h*scale))
    # Set title
    pygame.display.set_caption("Tetris")
    # Adds the board background image
    screen.blit(board_image, (0, 0))

    # Add cute little icon
    icon = pygame.image.load('images/icon.png')
    pygame.display.set_icon(icon)
    # representation of board for background logic 0 is
    # empty 1 is boarder and lists are the tetris blocks
    game_board = create_board()

    # default drop speed in (ms) and time events for dropping and locking pieces
    speed = 800
    next_check = get_next_check(speed)
    piece_stop_delay = speed

    down_pressed = False
    left_pressed = False
    right_pressed = False
    left_held = False
    right_held = False
    down_speed = 50  # ms
    l_r_delay = 500  # ms
    l_r_repeat = 50  # ms
    next_down_check = 0
    next_left_check = 0
    next_right_check = 0

    # generate pieces to drop
    piece_list = []
    piece_letter, piece_list = next_piece(piece_list)
    future_piece, piece_list = next_piece(piece_list)

    # paths for separate images for pieces

    if pixel_type == 1:
        pixel = "images/Pixel.png"
    elif pixel_type == 2:
        pixel = "images/Pixel2.png"
    elif pixel_type == 3:
        pixel = "images/Pixel3.png"
    else:
        pixel = "images/Pixel4.png"

    # color the path selected and return the color dictionary
    colors = load_pixel_color(pixel)

    # generate the next piece in the desired location
    if future_piece == "O" or future_piece == "I":
        future_piece_arr = generate_piece(piece_name=future_piece, x=18 * UNIT, y=5 * UNIT, colors=colors)
    else:
        future_piece_arr = generate_piece(piece_name=future_piece, x=int(18.5 * UNIT), y=5 * UNIT, colors=colors)

    current_piece = generate_piece(piece_letter, colors=colors)
    shadow = get_shadow(current_piece, game_board, colors)
    held_piece = None
    held_piece_arr = None
    held_used = False
    current_piece_rotations = 0
    cleared_lines = 0
    score = 0
    piece_stop_check = 0
    level = 1
    piece_not_below = True
    t_spin = False
    btb_tetris = False
    last_move_rotation = False

    # Create all visual text and fields
    font = pygame.font.Font('font.ttf', size=round(scale*40))
    WHITE = (255, 255, 255)
    score_header = font.render(f"Score:", True, WHITE)
    score_text = font.render(f"{score}", True, WHITE)
    level_header = font.render(f"Level:", True, WHITE)
    level_text = font.render(f"{level}", True, WHITE)
    lines_header = font.render(f"Lines Cleared", True, WHITE)
    lines_text = font.render(f"{cleared_lines}", True, WHITE)
    held_piece_text = font.render("Held Piece", True, WHITE)
    future_piece_text = font.render("Next Piece", True, WHITE)

    # Main game loop
    RUNNING = True
    while RUNNING:
        Time = time.time()
        for event in pygame.event.get():
            # Closes the window if X is pressed
            if event.type == pygame.QUIT:
                RUNNING = False
            # This section executes each command on button press
            # and not again until they are released
            if event.type == pygame.KEYUP:
                if event.key in [pygame.K_DOWN, pygame.K_s]:
                    down_pressed = False
                if event.key in [pygame.K_RIGHT, pygame.K_d]:
                    right_pressed = False
                    right_held = False
                if event.key in [pygame.K_LEFT, pygame.K_a]:
                    left_pressed = False
                    left_held = False
            if event.type == pygame.KEYDOWN:
                # Moves piece to right if possible
                if event.key in [pygame.K_RIGHT, pygame.K_d]:
                    right_pressed = True
                    if not right_collision_check(current_piece, game_board):
                        next_right_check = get_next_check(l_r_delay)
                        move_piece(current_piece, "right")
                        shadow = get_shadow(current_piece, game_board, colors)
                        piece_not_below = True
                # Moves piece to left if possible
                elif event.key in [pygame.K_LEFT, pygame.K_a]:
                    if not left_collision_check(current_piece, game_board):
                        next_left_check = get_next_check(l_r_delay)
                        move_piece(current_piece, "left")
                        shadow = get_shadow(current_piece, game_board, colors)
                        piece_not_below = True
                    left_pressed = True
                # Moves piece down if possible and resets drop timer
                elif event.key in [pygame.K_DOWN, pygame.K_s]:
                    down_pressed = True
                # Quick drops piece to bottom and immediately starts the next piece
                elif event.key in [pygame.K_SPACE]:
                    while not drop_collision_check(current_piece, game_board):
                        drop_piece(current_piece)
                        score += 2
                    score_text = font.render(f"{score}", True, WHITE)
                    piece_stop_check = 0
                    piece_not_below = False
                    stop_piece(current_piece, game_board)
                    next_check = get_next_check(speed)
                    current_piece_rotations = 0
                    last_move_rotation = False
                # Rotates the piece clockwise
                elif event.key in [pygame.K_x, pygame.K_UP]:
                    current_piece, current_piece_rotations, last_move_rotation = rotate(current_piece, "clockwise", game_board, current_piece_rotations, piece_letter)
                    piece_not_below = last_move_rotation
                    shadow = get_shadow(current_piece, game_board, colors)
                # Rotates the piece counter-clockwise
                elif event.key in [pygame.K_z, pygame.K_RCTRL, pygame.K_LCTRL]:
                    current_piece, current_piece_rotations, last_move_rotation = rotate(current_piece, "counter-clockwise", game_board, current_piece_rotations, piece_letter)
                    piece_not_below = last_move_rotation
                    shadow = get_shadow(current_piece, game_board, colors)
                # Holds the current piece
                elif event.key in [pygame.K_RSHIFT, pygame.K_LSHIFT, pygame.K_c]:
                    if not held_used:
                        if not held_piece:
                            held_piece = piece_letter
                            piece_letter = future_piece
                            future_piece, piece_list = next_piece(piece_list)
                            if future_piece == "O" or future_piece == "I":
                                future_piece_arr = generate_piece(piece_name=future_piece, x=18 * UNIT, y=5 * UNIT, colors=colors)
                            else:
                                future_piece_arr = generate_piece(piece_name=future_piece, x=int(18.5 * UNIT), y=5 * UNIT, colors=colors)
                            current_piece = generate_piece(piece_letter, colors=colors)
                            shadow = get_shadow(current_piece, game_board, colors)
                        elif held_piece:
                            current_piece = generate_piece(held_piece, colors=colors)
                            shadow = get_shadow(current_piece, game_board, colors)
                            piece_letter, held_piece = held_piece, piece_letter
                        held_used = True
                        if held_piece == "O" or held_piece == "I":
                            held_piece_arr = generate_piece(piece_name=held_piece, x=2*UNIT, y=5*UNIT, colors=colors)
                        else:
                            held_piece_arr = generate_piece(piece_name=held_piece, x=int(2.5*UNIT), y=5*UNIT, colors=colors)

        if down_pressed:
            if Time > next_down_check:
                if not drop_collision_check(current_piece, game_board):
                    drop_piece(current_piece)
                    next_down_check = get_next_check(down_speed)
                    next_check = get_next_check(speed)
                    score += 1
                    score_text = font.render(f"{score}", True, WHITE)
                    last_move_rotation = False
        if not (left_pressed and right_pressed):
            if left_pressed:
                if left_held:
                    if Time > next_left_check:
                        next_left_check = get_next_check(l_r_repeat)
                        if not left_collision_check(current_piece, game_board):
                            move_piece(current_piece, "left")
                            shadow = get_shadow(current_piece, game_board, colors)
                            piece_not_below = True
                elif Time > next_left_check:
                    left_held = True
            if right_pressed:
                if right_held:
                    if Time > next_right_check:
                        next_right_check = get_next_check(l_r_repeat)
                        if not right_collision_check(current_piece, game_board):
                            move_piece(current_piece, "right")
                            shadow = get_shadow(current_piece, game_board, colors)
                            piece_not_below = True
                elif Time > next_right_check:
                    right_held = True

        if drop_collision_check(current_piece, game_board) and piece_not_below:
            piece_stop_check = get_next_check(piece_stop_delay)
            piece_not_below = False
        elif drop_collision_check(current_piece, game_board):
            if Time > piece_stop_check:
                # Places piece
                if piece_letter == "T" and t_spin_check(current_piece, game_board) and last_move_rotation:
                    t_spin = True
                    # colors = load_pixel_color(pixel2)
                held_used = False
                current_piece_rotations = 0
                # Apply the piece to the board
                game_board = stop_piece(current_piece, game_board)

                # Remove full lines
                game_board, lines = check_lines(game_board)
                cleared_lines += lines

                # Update statistics
                lines_text = font.render(f"{cleared_lines}", True, WHITE)
                score, btb_tetris = update_score(lines, btb_tetris, score, t_spin, level)
                t_spin = False
                level, speed, piece_stop_delay = update_difficulty(cleared_lines)
                score_text = font.render(f"{score}", True, WHITE)
                level_text = font.render(f"{level}", True, WHITE)

                # Rotate pieces
                piece_letter = future_piece
                future_piece, piece_list = next_piece(piece_list)

                # Place new next piece in position
                if future_piece == "O" or future_piece == "I":
                    future_piece_arr = generate_piece(piece_name=future_piece, x=18 * UNIT, y=5 * UNIT, colors=colors)
                else:
                    future_piece_arr = generate_piece(piece_name=future_piece, x=int(18.5 * UNIT), y=5 * UNIT, colors=colors)

                # Create new piece
                current_piece = generate_piece(piece_letter, colors=colors)
                shadow = get_shadow(current_piece, game_board, colors)

                # If no space for new piece end game
                if drop_collision_check(current_piece, game_board):
                    return score
        else:
            piece_not_below = True
        if Time > next_check and piece_not_below:
            drop_piece(current_piece)
            next_check = get_next_check(speed)

        # Display board
        screen.blit(board_image, (0, 0))
        display_board(game_board, screen)

        # Display held piece, next piece, current piece, and shadow
        display_piece(held_piece_arr, screen)
        display_piece(future_piece_arr, screen)
        display_piece(shadow, screen)
        display_piece(current_piece, screen)

        # Display text fields
        screen.blit(score_header, (scale*825, scale*390))
        screen.blit(level_header, (scale*825, scale*435))
        screen.blit(lines_header, (scale*820, scale*535))
        screen.blit(score_text, (scale*915, scale*390))
        screen.blit(level_text, (scale*915, scale*435))
        screen.blit(lines_text, (scale*905 - scale*int((math.log10(cleared_lines + 1)) * 6), scale*575))
        screen.blit(held_piece_text, (scale*70, scale*50))
        screen.blit(future_piece_text, (scale*840, scale*50))
        # Updates display to the screen
        pygame.display.update()
    return score
