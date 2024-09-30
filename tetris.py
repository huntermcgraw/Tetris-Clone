import pygame
import random
# Time will be needed to shift the pieces over time since it will change consistently
import time

piece_list = ['L', 'T', 'S', 'Z', 'I', 'O', 'J']
# forgiving next piece algorithm that's used in modern games to prevent piece droughts
# makes sure each piece is used before sending duplicates furthest a duplicate can be is 13 pieces


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
    
    # Create the screen and set dimensions
    x_width = 1056
    y_width = 960
    screen = pygame.display.set_mode((x_width, y_width))
    screen.fill((20, 20, 20))
    board_image = pygame.image.load('images/Background.png')
    pixel1 = pygame.image.load('images/Pixel.png')

    # Set title
    pygame.display.set_caption("Tetris")
    # Adds the board background image
    screen.blit(board_image, (0, 0))
    # First makes the pixel red then adds it to the board
    pixel1.fill((0, 255, 0), special_flags=pygame.BLEND_MULT)
    screen.blit(pixel1, (240, 0))
    # Updates the screen
    pygame.display.update()

    # Visual representation of board for testing
    board = [[0 for _ in range(10)] for _ in range(24)]
    for i in board:
        temp = ""
        for j in i:
            temp += "["+str(j)+"]"
        print(temp)
    
    # Main game loop
    running = True
    while running:
        for event in pygame.event.get():
            # Closes the window if X is pressed
            if event.type == pygame.QUIT:
                running = False
            '''
            Code goes here
            '''
        pygame.display.update()
