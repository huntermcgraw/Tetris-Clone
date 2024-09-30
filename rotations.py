import pygame


class Tetris_Piece:
    def __init__(self, image_link) -> None:
        self.image = pygame.image.load(image_link)
        self.image_array = [
            self.image,
            pygame.transform.rotate(self.image, 90),
            pygame.transform.rotate(self.image, 180),
            pygame.transform.rotate(self.image, 270),
        ]
        self.index = 0
        self.current = self.image_array[self.index]

    def rotate(self):
        if self.index == 3:
            self.index = 0
        else:
            self.index += 1
        self.current = self.image_array[self.index]


l_piece = Tetris_Piece("./images/L BLOCK.png")
