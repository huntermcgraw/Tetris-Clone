import tetris
import csv
import pygame
import time
import pygame_widgets
from pygame_widgets.button import Button

# initialize pygame
pygame.init()

# dimensions of the images for the game background
X_WIDTH = 1056
Y_WIDTH = 960
# gets the system information for scaling
info = pygame.display.Info()
# ratio of screen to image
scale = (info.current_h - 80) / Y_WIDTH
# Adjusts the scaling to the nearest whole devisor of unit
UNIT = 48 * scale
scale -= round(UNIT % 1, 8) / 48
UNIT = round(48 * scale)

# scale = 1
# unit = 48
score = 0
pixel_type = 1
def play_clicked(screen, type):
    global pixel_type
    global score
    if pixel_type == type:
        score = tetris.play_tetris(screen, pixel_type)
    pixel_type = type

def settings_clicked(screen):
    pass

def high_score_clicked(screen):
    pass

if __name__ == "__main__":
    flash_on = False
    flash_timer = 0
    flash_delay = 500
    screen = pygame.display.set_mode((X_WIDTH * scale, Y_WIDTH * scale))
    start_image = pygame.image.load("images/StartScreen.png")
    game_over_image = pygame.image.load("images/GameOver.png")
    font = pygame.font.Font('font.ttf',size=round(scale*40))
    start_game_text = font.render("Press a block to play", True, (255,255,255))
    game_over_image = pygame.transform.scale(
        game_over_image, (X_WIDTH * scale, Y_WIDTH * scale)
    )
    start_image = pygame.transform.scale(
        start_image, (X_WIDTH * scale, Y_WIDTH * scale)
    )
    outline = pygame.image.load("images/pixel.png")
    outline.fill((0, 255, 0), special_flags=pygame.BLEND_MULT)
    w = outline.get_height()
    outline = pygame.transform.scale(outline,(w*scale*1.24,w*scale*1.24))
    play_image = pygame.image.load("images/pixel.png")
    play_image2 = pygame.image.load("images/pixel2.png")
    play_image3 = pygame.image.load("images/pixel3.png")
    play_image4 = pygame.image.load("images/pixel3.png")

    w, h = play_image.get_width() * scale, play_image.get_height() * scale
    play_image = pygame.transform.scale(play_image, (w, h))
    play_image2 = pygame.transform.scale(play_image2, (w, h))
    play_image3 = pygame.transform.scale(play_image3, (w, h))
    play_image4 = pygame.transform.scale(play_image4, (w, h))
    play_button = Button(
        screen,
        288 * scale,
        624 * scale,
        w,
        h,
        image=play_image,
        onClick=lambda: play_clicked(screen,1),
    )
    play_button2 = Button(
        screen,
        432 * scale,
        624 * scale,
        w,
        h,
        image=play_image2,
        onClick=lambda: play_clicked(screen,2),
    )
    play_button3 = Button(
        screen,
        576 * scale,
        624 * scale,
        w,
        h,
        image=play_image3,
        onClick=lambda: play_clicked(screen,3),
    )
    play_button4 = Button(
        screen,
        720 * scale,
        624 * scale,
        w,
        h,
        image=play_image4,
        onClick=lambda: play_clicked(screen,4),
    )
    # Add cute little icon
    icon = pygame.image.load("images/icon.png")
    pygame.display.set_icon(icon)
    # Set title
    pygame.display.set_caption("Tetris")
    # Adds the board background image

    # Plays tetris music on repeat
    music = pygame.mixer.music.load("music.mp3")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.1)

    RUNNING = True
    while RUNNING:
        Time = time.time()
        if Time > flash_timer:
            flash_timer = tetris.get_next_check(flash_delay)
            flash_on = not flash_on
        events = pygame.event.get()
        for event in events:
            # Closes the window if X is pressed
            if event.type == pygame.QUIT:
                RUNNING = False
                
        
        screen.blit(start_image, (0, 0))
        if flash_on:
            screen.blit(start_game_text, (380*scale,550*scale))
        if score == -1:
            RUNNING = False
        if pixel_type == 1:
            screen.blit(outline, (288*scale-5*scale, 624*scale-5*scale))
        elif pixel_type == 2:
            screen.blit(outline, (432*scale-5*scale, 624*scale-5*scale))
        elif pixel_type == 3:
            screen.blit(outline, (576*scale-5*scale, 624*scale-5*scale))
        else:
            screen.blit(outline, (720*scale-5*scale, 624*scale-5*scale))
        
        pygame_widgets.update(events)
        pygame.display.update()

    with open("scores.csv", "r") as csv_file:
        csv_reader = csv.reader(csv_file)
        data = next(csv_reader)

    if score > int(data[0]):
        with open("scores.csv", "w") as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow([score])
