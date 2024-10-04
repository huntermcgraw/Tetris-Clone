import pygame
import random
import time

# Global variables
# Unit is the size of the squares for mutating pieces
UNIT = 48
piece_list = []
SPEED = 800
PIECE = ''


def nextPiece():
    # forgiving next piece algorithm that's used in modern games to prevent piece droughts. this
    # makes sure each piece is used before sending duplicates furthest a duplicate can be is 13 pieces
    # Chooses the next piece and returns the string variant
    global piece_list
    global PIECE
    if not piece_list:
        piece_list = ['L', 'T', 'S', 'Z', 'I', 'O', 'J']
    random.shuffle(piece_list)
    PIECE = piece_list.pop(0)
    return PIECE


def generatePiece(piece_name, x=(11 * UNIT), y=(1 * UNIT)):
    # Creates the 4 tetris blocks from the string given from nextPiece. The first block is
    # the "home block" this is the piece logic and rotations are based around
    key = {
        'L': [[x, y, orange], [x, y-UNIT, orange], [x, y+UNIT, orange], [x+UNIT, y+UNIT, orange]],
        'T': [[x, y, purple], [x, y-UNIT, purple], [x-UNIT, y, purple], [x+UNIT, y, purple]],
        'Z': [[x, y, red], [x, y-UNIT, red], [x+UNIT, y, red], [x+UNIT, y+UNIT, red]],
        'S': [[x+UNIT, y, green], [x+UNIT, y-UNIT, green], [x, y, green], [x, y+UNIT, green]],
        'I': [[x, y, teal], [x, y-UNIT, teal], [x, y+UNIT, teal], [x, y+UNIT*2, teal]],
        'O': [[x, y, yellow], [x, y-UNIT, yellow], [x+UNIT, y, yellow], [x+UNIT, y-UNIT, yellow]],
        'J': [[x+UNIT, y, blue], [x+UNIT, y-UNIT, blue], [x+UNIT, y+UNIT, blue], [x, y+UNIT, blue]],
    }
    return key[piece_name]


def getNextCheck(interval):
    # gets the next time that pieces will move down. interval is a time in ms
    interval /= 1000
    current_time = time.time()
    nextCheck = current_time + interval
    return nextCheck


def dropPiece(arr):
    # Moves the piece down. does not care about collision
    for i in arr:
        i[1] += UNIT


def movePiece(arr, command):
    # Moves the piece left or right. does not care about collision
    if command == "right":
        for i in arr:
            i[0] += UNIT
    elif command == "left":
        for i in arr:
            i[0] -= UNIT


def createBoard():
    # this creates the background board for the logic to be done on in the background
    board = [[0 for _ in range(15)] for _ in range(20)]
    for i in range(len(board)):
        for j in range(len(board[i])):
            if i == 19 or j == 1 or j == 12:
                board[i][j] = 1
    return board


def stopPiece(arr, board):
    # This adds the piece to the board so the arr can be used for the next piece
    for i in arr:
        x, y = getXY(i)
        board[y][x] = i
    return board


def checkLines():
    # clear lines add points and totals lines cleared
    return


def rotationCollisionCheck():
    # make this so when the player spins outside the area it will push them back in but
    # when they spin into another piece it just doesn't do it
    return


def holdPiece(arr):
    # move the piece out of the game board and move the piece on hold back to the top if possible
    return


def updateDifficulty(line_clears):
    # change the difficulty based on amount of lines cleared
    global SPEED
    SPEED = 800
    
    return


def dropCollisionCheck(arr, board):
    for i in arr:
        x, y = getXY(i)
        if board[y+1][x] != 0:
            return True
    return False


def rightCollisionCheck(arr, board):
    for i in arr:
        x, y = getXY(i)
        if board[y][x+1] != 0:
            return True
    return False


def leftCollisionCheck(arr, board):
    for i in arr:
        x, y = getXY(i)
        if board[y][x-1] != 0:
            return True
    return False


def rotate(arr, direction):
    if PIECE != 'O':
        master_x, master_y = getXY(arr[0])
        for i in arr:
            x, y = getXY(i)
            x -= master_x
            y -= master_y
            if direction == "clockwise":
                x1 = -y
                y1 = x
                i[0] = (x1 + master_x)*UNIT
                i[1] = (y1 + master_y)*UNIT
            else:
                x1 = y
                y1 = -x
                i[0] = (x1 + master_x)*UNIT
                i[1] = (y1 + master_y)*UNIT
            # Ignore this code you didnt see it
            i[0] += 4*UNIT
    return arr


def getXY(unit):
    x, y = int((unit[0]-160)/48), int((unit[1])/48)
    return x, y


def displayPiece(arr):
    for i in arr:
        screen.blit(i[2], (i[0], i[1]))


def displayBoard(board):
    for i in board:
        for j in i:
            if j != 0 and j != 1:
                screen.blit(j[2], (j[0], j[1]))


if __name__ == "__main__":
    
    # Initialize pygame
    pygame.init()
    
    # Create the screen and set dimensions
    x_width = 1056
    y_width = 600
    screen = pygame.display.set_mode((x_width, y_width))
    board_image = pygame.image.load('images/Background.png')
    pixel = pygame.image.load('images/Pixel.png')
    red = pygame.image.load('images/Pixel.png')
    orange = pygame.image.load('images/Pixel.png')
    yellow = pygame.image.load('images/Pixel.png')
    green = pygame.image.load('images/Pixel.png')
    blue = pygame.image.load('images/Pixel.png')
    purple = pygame.image.load('images/Pixel.png')
    teal = pygame.image.load('images/Pixel.png')
    red.fill((255, 0, 0), special_flags=pygame.BLEND_MULT)
    orange.fill((255, 165, 0), special_flags=pygame.BLEND_MULT)
    yellow.fill((255, 255, 0), special_flags=pygame.BLEND_MULT)
    green.fill((0, 150, 0), special_flags=pygame.BLEND_MULT)
    blue.fill((0, 0, 255), special_flags=pygame.BLEND_MULT)
    purple.fill((134, 1, 175), special_flags=pygame.BLEND_MULT)
    teal.fill((64, 224, 208), special_flags=pygame.BLEND_MULT)
    
    # Set title
    pygame.display.set_caption("Tetris")
    
    # Adds the board background image
    screen.blit(board_image, (0, 0))

    # representation of board for background logic 0 is empty 1 is boarder and lists are the tetris blocks
    game_board = createBoard()
    
    # Timer for dropping blocks 
    next_check = getNextCheck(SPEED)
    
    # This is the 4 blocks that make up the tetris piece [x_coordinate, y_coordinate, colored picture]
    current_piece = generatePiece(nextPiece())

    # Main game loop
    running = True
    while running:
        for event in pygame.event.get():
            # Closes the window if X is pressed
            if event.type == pygame.QUIT:
                running = False
            # This section executes each command on button press and not again until they are released
            if event.type == pygame.KEYDOWN:
                # Moves piece to right if possible
                if event.key == pygame.K_RIGHT:
                    if not rightCollisionCheck(current_piece, game_board):
                        movePiece(current_piece, "right")
                # Moves piece to left if possible
                elif event.key == pygame.K_LEFT:
                    if not leftCollisionCheck(current_piece, game_board):
                        movePiece(current_piece, "left")
                # Moves piece down if possible and resets drop timer
                elif event.key == pygame.K_DOWN:
                    if not dropCollisionCheck(current_piece,game_board):
                        dropPiece(current_piece)
                        next_check = getNextCheck(SPEED)
                # Quick drops piece to bottom and immediately starts the next piece
                elif event.key == pygame.K_UP:
                    while not dropCollisionCheck(current_piece,game_board):
                        dropPiece(current_piece)
                    stopPiece(current_piece,game_board)
                    next_check = 0
                # Rotates the piece clockwise 
                elif event.key == pygame.K_x:
                    current_piece = rotate(current_piece,"clockwise")
                # Rotates the piece counter-clockwise
                elif event.key == pygame.K_z:
                    current_piece = rotate(current_piece,"counter-clockwise")

        # Display board
        screen.blit(board_image, (0, 0))
        # Display current piece
        displayPiece(current_piece)
        # Display all remaining pieces
        displayBoard(game_board)

        # Determines when the piece drops and drops or locks piece if something is below
        if time.time() > next_check:
            if dropCollisionCheck(current_piece, game_board):
                game_board = stopPiece(current_piece, game_board)
                checkLines()
                current_piece = generatePiece(nextPiece())
            else:
                dropPiece(current_piece)
            next_check = getNextCheck(SPEED)
        
        # Updates display to the screen
        pygame.display.update()
