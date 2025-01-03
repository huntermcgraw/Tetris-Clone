import tetris
import csv
import pygame
import time
import pygame_widgets
from pygame_widgets.button import Button
import os
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
screen_width = info.current_w
"""
The width of the user’s screen
"""

with open("scores.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file)
    """
    The reader for the high score file
    """
    high_score = next(csv_reader)
    """
    The current high score, as read by csv_reader
    """

# ratio of screen to image
scale = (info.current_h - 80) / Y_WIDTH
"""
Used to scale the window to the user’s screen size, the ratio of screen to image
"""
os.environ['SDL_VIDEO_WINDOW_POS'] = f"{int((screen_width - X_WIDTH*scale) // 2)},30"
UNIT = 48 * scale
"""
Adjusts the scaling to the nearest whole divisor of unit
"""
scale -= round(UNIT % 1, 8) / 48
UNIT = round(48 * scale)

# scale = 1
# unit = 48
score = 0
"""
Store the player's most recent score
"""
pixel_type = 1
"""
Which Pixel#.png the user is playing with
"""
music_on = True
"""
Boolean if the music is on
"""


def play_clicked(play_screen, new_type):
    """
    Starts the game with the inputted pixel type
    :param play_screen: The pygame object the screen is displayed on
    :param new_type: (int) The number corresponding to the pixel#.png the user is going to use for the blocks
    :return: (int) the score the player ended the game with
    """
    global pixel_type
    global score
    if pixel_type == new_type:
        score = tetris.play_tetris(play_screen, pixel_type)
    pixel_type = new_type

    return score


def toggle_sound(button, button_on, button_off):
    """
    Mutes or unmutes the sound
    :param button: The pygame button object that user interacts with
    :param button_on: The pygame loaded image for sound being on
    :param button_off: The pygame loaded image for sound being off
    :return: (None)
    """
    global music_on
    music_on = not music_on
    if music_on:
        button.image = button_on
        pygame.mixer.music.set_volume(0.1)
        return
    button.image = button_off
    pygame.mixer.music.set_volume(0)
    return


def get_high_score():
    """
    Records and returns the highest score the player has reached
    :return: (int) The highest score the player reached
    """
    with open("scores.csv", "r") as file:
        reader = csv.reader(file)
        new_high_score = next(reader)

    if score > int(new_high_score[0]):
        with open("scores.csv", "w") as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow([score])

        return score

    return int(new_high_score[0])


if __name__ == "__main__":
    flash_on = False
    flash_timer = 0
    flash_delay = 500
    screen = pygame.display.set_mode((X_WIDTH * scale, Y_WIDTH * scale))
    start_image = pygame.image.load("images/StartScreen.png")
    game_over_image = pygame.image.load("images/GameOver.png")
    font = pygame.font.Font('font.ttf', size=round(scale*40))
    start_game_text = font.render("Press a block to play", True, (255, 255, 255))
    score = int(high_score[0])
    high_score_text = font.render(f"HIGH: {score}", True, (255, 255, 255))
    game_over_image = pygame.transform.scale(
        game_over_image, (X_WIDTH * scale, Y_WIDTH * scale)
    )
    start_image = pygame.transform.scale(
        start_image, (X_WIDTH * scale, Y_WIDTH * scale)
    )
    outline = pygame.image.load("images/Pixel.png")
    outline.fill((0, 255, 0), special_flags=pygame.BLEND_MULT)
    w = outline.get_height()
    outline = pygame.transform.scale(outline, (w*scale*1.24, w*scale*1.24))
    play_image = pygame.image.load("images/Pixel.png")
    play_image2 = pygame.image.load("images/Pixel2.png")
    play_image3 = pygame.image.load("images/Pixel3.png")
    play_image4 = pygame.image.load("images/Pixel4.png")
    sound_button_on = pygame.image.load("images/VolumeOn.png")
    sound_button_off = pygame.image.load("images/VolumeOff.png")
    sound_button_on = pygame.transform.scale(sound_button_on, (w*scale*2, w*scale*2))
    sound_button_off = pygame.transform.scale(sound_button_off, (w*scale*2, w*scale*2))
    w, h = play_image.get_width() * scale, play_image.get_height() * scale
    play_image = pygame.transform.scale(play_image, (w, h))
    play_image2 = pygame.transform.scale(play_image2, (w, h))
    play_image3 = pygame.transform.scale(play_image3, (w, h))
    play_image4 = pygame.transform.scale(play_image4, (w, h))
    print(scale)
    play_button = Button(
        screen,
        int(288 * scale),
        int(624 * scale),
        int(w),
        int(h),
        image=play_image,
        onClick=lambda: play_clicked(screen, 1),
    )
    play_button2 = Button(
        screen,
        int(432 * scale),
        int(624 * scale),
        int(w),
        int(h),
        image=play_image2,
        onClick=lambda: play_clicked(screen, 2),
    )
    play_button3 = Button(
        screen,
        int(576 * scale),
        int(624 * scale),
        int(w),
        int(h),
        image=play_image3,
        onClick=lambda: play_clicked(screen, 3),
    )
    play_button4 = Button(
        screen,
        int(720 * scale),
        int(624 * scale),
        int(w),
        int(h),
        image=play_image4,
        onClick=lambda: play_clicked(screen, 4),
    )
    sound_button = Button(
        screen,
        int(960 * scale),
        int(864 * scale),
        int(sound_button_on.get_width()),
        int(sound_button_on.get_height()),
        image=sound_button_on,
        onClick=lambda:
            toggle_sound(sound_button, sound_button_on, sound_button_off),
    )
    # Add cute little icon
    icon = pygame.image.load("images/icon.png")
    pygame.display.set_icon(icon)
    # Set title
    pygame.display.set_caption("Tetris")
    # Adds the board background image

    # Plays tetris music on repeat
    pygame.mixer.music.load("Blokken.mp3")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.1)
    music_on = True

    RUNNING = True
    while RUNNING:

        pygame.display.flip()
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
            screen.blit(start_game_text, (380*scale, 550*scale))
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

        high_score = get_high_score()
        if score > high_score:
            high_score = score
        high_score_text = font.render(f"HIGH: {high_score}", True, (255, 255, 255))
        if high_score > 999999:
            high_score_x = 410 * scale - 5 * scale
        elif high_score > 99999:
            high_score_x = 420 * scale - 5 * scale
        elif high_score > 9999:
            high_score_x = 425 * scale - 5 * scale
        elif high_score > 999:
            high_score_x = 435 * scale - 5 * scale
        else:
            high_score_x = 445 * scale - 5 * scale

        screen.blit(high_score_text, (scale*475 - scale*int((math.log10(high_score + 1)) * 6), 724 * scale - 5 * scale))

        pygame_widgets.update(events)
        pygame.display.update()
