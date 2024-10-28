"""random is needed to shuffle the pieces to make them random
    Time will be needed to shift the pieces over the board
    pygame is our main game framework """
import random
import time
import pygame
UNIT = 48
piece_list = []
SPEED = 800
red = pygame.image.load("images/Pixel.png")
orange = pygame.image.load("images/Pixel.png")
yellow = pygame.image.load("images/Pixel.png")
green = pygame.image.load("images/Pixel.png")
blue = pygame.image.load("images/Pixel.png")
purple = pygame.image.load("images/Pixel.png")
teal = pygame.image.load("images/Pixel.png")
red.fill((255, 0, 0), special_flags=pygame.BLEND_MULT)
orange.fill((255, 128, 0), special_flags=pygame.BLEND_MULT)
yellow.fill((255, 255, 0), special_flags=pygame.BLEND_MULT)
green.fill((0, 255, 0), special_flags=pygame.BLEND_MULT)
blue.fill((0, 0, 255), special_flags=pygame.BLEND_MULT)
purple.fill((196, 0, 196), special_flags=pygame.BLEND_MULT)
teal.fill((0, 255, 255), special_flags=pygame.BLEND_MULT)


def next_piece():
    """
        Determines the next piece to use. uses traditional tetris algorithm to prevent droughts:
        Parameters: (none)
    """
    global piece_list
    if not piece_list:
        piece_list = ["L", "T", "S", "Z", "I", "O", "J"]
        random.shuffle(piece_list)
    return piece_list.pop(0)


def generate_piece(piece_name="O", x=11 * UNIT, y=1 * UNIT):
    """
        Takes a piece from next_piece or a piece from the user and generates the components
        at the desired locations for that piece. Can also get prompted with x,y to change the
        starting position of the home piece.
        Parameters:
        piece_name (str): one of these strings ["L", "T", "S", "Z", "I", "O", "J"]
        x (int): the position in pixels of the x coordinate
        y (int): the position in pixels of the y coordinate
    """
    key = {
        "L": [
            [x, y, orange],
            [x, y - UNIT, orange],
            [x, y + UNIT, orange],
            [x + UNIT, y + UNIT, orange],
        ],
        "T": [
            [x, y, purple],
            [x, y - UNIT, purple],
            [x - UNIT, y, purple],
            [x + UNIT, y, purple],
        ],
        "Z": [
            [x, y, red],
            [x, y - UNIT, red],
            [x + UNIT, y, red],
            [x + UNIT, y + UNIT, red],
        ],
        "S": [
            [x + UNIT, y, green],
            [x + UNIT, y - UNIT, green],
            [x, y, green],
            [x, y + UNIT, green],
        ],
        "I": [
            [x, y, teal],
            [x, y - UNIT, teal],
            [x, y + UNIT, teal],
            [x, y + UNIT * 2, teal],
        ],
        "O": [
            [x, y, yellow],
            [x, y - UNIT, yellow],
            [x + UNIT, y, yellow],
            [x + UNIT, y - UNIT, yellow],
        ],
        "J": [
            [x + UNIT, y, blue],
            [x + UNIT, y - UNIT, blue],
            [x + UNIT, y + UNIT, blue],
            [x, y + UNIT, blue],
        ],
    }
    return key[piece_name]


def get_next_check(interval):
    """
        gets the next time that returns the time <interval> away from the current time.
        Parameters:
        interval (int): how many ms away we want the next check
    """
    interval /= 1000
    current_time = time.time()
    return current_time + interval


def drop_piece(arr):
    """
        Moves the piece down 1 in the game board collision should be checked prior
        Parameters:
        arr (arr[arr[int]]): The current piece
    """
    for i in arr:
        i[1] += UNIT


def move_piece(arr, command):
    """
        Moves the piece left or right 1 in the game board collision should be checked prior
        Parameters:
        arr (arr[arr[int]]): The current piece
        command (string): right or left to determine direction
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
        Parameters: (none)
    """
    board = [[0 for _ in range(15)] for _ in range(20)]
    for i, _ in enumerate(board):
        for j, _ in enumerate(board[i]):
            if i == 19 or j == 1 or j == 12:
                board[i][j] = 1
    return board


def stop_piece(arr, board):
    """
        Adds the current piece to the board
        Parameters:
        arr (arr[arr[int]]): The current piece
        board (arr[arr[int]]): The game board
    """
    # This adds the piece to the board so the arr can be used for the next piece
    for i in arr:
        x, y = get_x_y(i)
        board[y][x] = i
    return board


def check_lines(board):
    """
        checks for full lines, clears them, and moves above rows down
        Parameters:
        board (arr[arr[int]]): The game board
    """
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
                board.insert(0, new_line.copy())  # Add an empty line to the top of the board
                for row, _ in enumerate(board):
                    for space in board[row][2:]:
                        if row > line:  # Skips empty lines and lines below the cleared line
                            break
                        if isinstance(space, list):  # Moves everything down by one unit
                            space[1] += UNIT
    return board


def hold_piece(arr):
    """
        Should hold the current piece and either take out a new piece or the current held piece
        Parameters:
        arr (arr[arr[int]]): The current piece
    """
    # move the piece out of the game board and move the piece on hold back to the top if possible
    return


def update_difficulty(line_clears):
    pass
    """
        lowers the speed value if the lines cleared reaches the threshold
        line_clears (int): how many lines were cleared
    """
    return


def drop_collision_check(arr, board):
    """
        Checks to see if there is a block below or a border
        Parameters:
        arr (arr[arr[int]]): The current piece
        board (arr[arr[int]]): The game board
    """
    for i in arr:
        x, y = get_x_y(i)
        if board[y + 1][x] != 0:
            return True
    return False


def right_collision_check(arr, board):
    """
        Checks to see if there is a block to the right or a border
        Parameters:
        arr (arr[arr[int]]): The current piece
        board (arr[arr[int]]): The game board
    """
    for i in arr:
        x, y = get_x_y(i)
        if board[y][x + 1] != 0:
            return True
    return False


def left_collision_check(arr, board):
    """
        Checks to see if there is a block to the left or a border
        Parameters:
        arr (arr[arr[int]]): The current piece
        board (arr[arr[int]]): The game board
    """
    for i in arr:
        x, y = get_x_y(i)
        if board[y][x - 1] != 0:
            return True
    return False


def right_collision_rotation_check(arr, board):
    """
        Checks to see if the piece can rotate right without collision with border or other blocks
        Parameters:
        arr (arr[arr[int]]): The current piece
        board (arr[arr[int]]): The game board
    """
    for i in arr:
        x, y = get_x_y(i)
        try:
            if board[y][x] != 0:
                return True
        except IndexError:
            return True
    return False


def left_collision_rotation_check(arr, board):
    """
        Checks to see if the piece can rotate left without collision with border or other blocks
        Parameters:
        arr (arr[arr[int]]): The current piece
        board (arr[arr[int]]): The game board
    """
    for i in arr:
        x, y = get_x_y(i)
        try:
            if board[y][x] != 0:
                return True
        except IndexError:
            return True
    return False


def rotate(arr, direction, board):
    """
        rotates the piece by doing reflections over y=x and y=-x respective to
        the direction does not care about collision
        Parameters:
        arr (arr[arr[int]]): The current piece
        direction (string): clockwise or counterclockwise for direction
        board (arr[arr[int]]): The game board
    """

    # If it's the square piece, don't rotate.
    if (arr[0][0] == arr[1][0] and arr[2][0] == arr[3][0]) and (
        arr[0][1] == arr[2][1] and arr[1][1] == arr[3][1]
    ):
        return arr

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
    if left_collision_rotation_check(arr, board) and right_collision_rotation_check(arr, board):
        return array_prev
    while left_collision_rotation_check(arr, board):
        move_piece(arr, "right")
    while right_collision_rotation_check(arr, board):
        move_piece(arr, "left")
    return arr


def get_x_y(unit):
    """
        retrieves the x and y coordinate from the position on screen. this is where
        they are on the board array
        Parameters:
        unit (list[x(int),y(int),color]): the color is a pygame image that is displayed with a tint
    """
    x, y = int((unit[0] - 160) / 48), int((unit[1]) / 48)
    return x, y


def display_piece(arr, display_screen):
    """
        prints the game piece to the board this is separate from the board array and
        is not contained in the array
        this function displays the current piece over the board.
        Parameters:
        arr (arr[arr[int]]): The current piece
        display_screen (pygame.surface): pygame screen
    """
    for i in arr:
        display_screen.blit(i[2], (i[0], i[1]))


def display_board(board, display_screen):
    """
        This function displays board on the screen object
        Parameters:
        board (arr[arr[int]]): board
        display_screen (pygame.surface): pygame screen
    """
    for i in board:
        for j in i:
            if j != 0 and j != 1:
                display_screen.blit(j[2], (j[0], j[1]))


if __name__ == "__main__":

    # Initialize pygame
    pygame.init()

    # Create the screen and set dimensions
    X_WIDTH = 1056
    Y_WIDTH = 960
    screen = pygame.display.set_mode((X_WIDTH, Y_WIDTH))
    board_image = pygame.image.load("images/Background.png")

    # Set title
    pygame.display.set_caption("Tetris")

    # Adds the board background image
    screen.blit(board_image, (0, 0))

    # representation of board for background logic 0 is
    # empty 1 is boarder and lists are the tetris blocks
    game_board = create_board()

    # Timer for dropping blocks
    next_check = get_next_check(SPEED)

    # This is the 4 blocks that make up the tetris piece
    # [x_coordinate, y_coordinate, colored picture]
    current_piece = generate_piece()

    # Main game loop
    RUNNING = True
    while RUNNING:
        for event in pygame.event.get():
            # Closes the window if X is pressed
            if event.type == pygame.QUIT:
                RUNNING = False
            # This section executes each command on button press
            # and not again until they are released
            if event.type == pygame.KEYDOWN:
                # Moves piece to right if possible
                if event.key in [pygame.K_RIGHT, pygame.K_d]:
                    if not right_collision_check(current_piece, game_board):
                        move_piece(current_piece, "right")
                # Moves piece to left if possible
                elif event.key in [pygame.K_LEFT, pygame.K_a]:
                    if not left_collision_check(current_piece, game_board):
                        move_piece(current_piece, "left")
                # Moves piece down if possible and resets drop timer
                elif event.key in [pygame.K_DOWN, pygame.K_s]:
                    if not drop_collision_check(current_piece, game_board):
                        drop_piece(current_piece)
                        next_check = get_next_check(SPEED)
                # Quick drops piece to bottom and immediately starts the next piece
                elif event.key in [pygame.K_SPACE]:
                    while not drop_collision_check(current_piece, game_board):
                        drop_piece(current_piece)
                    stop_piece(current_piece, game_board)
                    next_check = 0
                # Rotates the piece clockwise
                elif event.key in [pygame.K_x, pygame.K_UP]:
                    current_piece = rotate(current_piece, "clockwise", game_board)
                # Rotates the piece counter-clockwise
                elif event.key in [pygame.K_z, pygame.K_RCTRL, pygame.K_LCTRL]:
                    current_piece = rotate(current_piece, "counter-clockwise", game_board)
                # Holds the current piece
                # elif event.key in [pygame.K_RSHIFT, pygame.K_LSHIFT, pygame.K_c]:
                #    holdPiece()

        # Display board
        screen.blit(board_image, (0, 0))
        # Display current piece
        display_piece(current_piece, screen)
        # Display all remaining pieces
        display_board(game_board, screen)

        # Determines when the piece drops and drops or locks piece if something is below
        if time.time() > next_check:
            if drop_collision_check(current_piece, game_board):
                game_board = stop_piece(current_piece, game_board)
                game_board = check_lines(game_board)
                current_piece = generate_piece(next_piece())
                # Clears Board when cannot place another piece
                if drop_collision_check(current_piece, game_board):
                    game_board = create_board()
            else:
                drop_piece(current_piece)
            next_check = get_next_check(SPEED)

        # Updates display to the screen
        pygame.display.update()
