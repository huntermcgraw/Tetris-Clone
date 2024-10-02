import pygame
import random
import asyncio
# Time will be needed to shift the pieces over time since it will change consistently
import time

piece_list = ['L', 'T', 'S', 'Z', 'I', 'O', 'J']
# [L, T, Squiggly, Reverse Squiggly, Line Piece, Square, Reverse L]
# forgiving next piece algorithm that's used in modern games to prevent piece droughts
# makes sure each piece is used before sending duplicates furthest a duplicate can be is 13 pieces
xkeyDict = {
    'L': [0, ],
    'T': [0, ],
    'Z': [0, 48, 0, -48],
    'S': [0, -48, 0, 48],
    'I': [0, ],
    'O': [0, -48, -48, 0],
    'J': [0, ],
}
ykeyDict = {
    'L': [0, ],
    'T': [0, ],
    'Z': [0, 0, -48, -48],
    'S': [0, 0, -48, -48],
    'I': [0, ],
    'O': [0, 0, -48, -48],
    'J': [0, ],
}
colorDict = {
    'L': (255, 128, 0),  # Orange
    'T': (196, 0, 196),  # Purple
    'Z': (0, 255, 0),  # Green
    'S': (255, 0, 0),  # Red
    'I': (0, 255, 255),  # Cyan
    'O': (255, 255, 0),  # Yellow
    'J': (0, 0, 255),  # Blue
}


def nextPiece():
    global piece_list
    if not piece_list:
        piece_list = ['L', 'T', 'S', 'Z', 'I', 'O', 'J']
    random.shuffle(piece_list)
    return piece_list.pop(0)


if __name__ == "__main__":
    
    # Initialize pygame
    pygame.init()
    
    # Creates first piece and populates first set of pieces
    piece = nextPiece()
    xkey = xkeyDict[piece]
    ykey = ykeyDict[piece]
    color = colorDict[piece]

    # Create the screen and set dimensions
    x_width = 1056
    y_width = 960
    screen = pygame.display.set_mode((x_width, y_width))
    screen.fill((20, 20, 20))
    # Set title
    pygame.display.set_caption("Tetris")

    # Puts the images on screen
    board_image = pygame.image.load('images/Background.png')
    pixels = [pygame.image.load('images/Pixel.png') for item in range(0, 4)]
    # Give the pixel its color
    for item in pixels:
        item.fill(color, special_flags=pygame.BLEND_MULT)

    # Visual representation of board for testing
    board = [[0 for _ in range(10)] for _ in range(24)]
    for i in board:
        temp = ""
        for j in i:
            temp += "["+str(j)+"]"
        print(temp)

    # The Information for moving the pieces around
    delta = 48  # How much the piece moves in one go, the size of each piece in pixels
    # Starting Location of the piece
    x = 480
    y = 0
    clock = pygame.time.Clock()
    # Main game loop
    running = True
    while running:
        for event in pygame.event.get():
            # Closes the window if X is pressed
            if event.type == pygame.QUIT:
                running = False
        key = 0
        # Get the piece moving
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            if 288 <= (x - delta):
                if -48 in xkey and (288 <= (x - delta - 48)):
                    x -= delta
        if keys[pygame.K_RIGHT]:
            if (x + delta) <= 720:
                if (48 in xkey and (x + delta + 48) <= 720) or 48 not in xkey:
                    x += delta
        if keys[pygame.K_UP]:
            if 0 <= (y - delta):
                if -48 in ykey and 0 <= (y - delta - 48):
                    y -= delta
        if keys[pygame.K_DOWN]:
            if (y + delta) <= 864:
                if (48 in ykey and (y + delta + 48) <= 864) or 48 not in ykey:
                    y += delta
        if keys[pygame.K_SPACE]:
            temp = xkey
            xkey = ykey
            ykey = temp
        # Have to redo the board to avoid the color painting the board
        screen.blit(board_image, (0, 0))
        for item in pixels:
            if key == 4:
                key = 0
            screen.blit(item, (x+xkey[key], y+ykey[key]))
            key += 1
        pygame.display.update()
        # Used to set the FPS
        clock.tick(11)
