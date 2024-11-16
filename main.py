
import tetris 
import pygame
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
scale = (info.current_h-80)/Y_WIDTH
# Adjusts the scaling to the nearest whole devisor of unit
UNIT = (48 * scale)
scale -= round(UNIT%1,8) / 48
UNIT = round(48 * scale)

# scale = 1
# unit = 48
score = 0
def play_clicked(screen):
    global score 
    score = tetris.play_tetris(screen, scale)
    
def settings_clicked(screen):
    pass

    
def high_score_clicked(screen):
    pass
    
    
if __name__ == "__main__":
    screen = pygame.display.set_mode((X_WIDTH*scale,Y_WIDTH*scale))
    start_image = pygame.image.load("images/StartScreen.png")
    game_over_image = pygame.image.load("images/GameOver.png")

    game_over_image = pygame.transform.scale(game_over_image,(X_WIDTH*scale,Y_WIDTH*scale))
    start_image = pygame.transform.scale(start_image,(X_WIDTH*scale,Y_WIDTH*scale))
    
    play_image = pygame.image.load("images/pixel3.png")
    settings_image = pygame.image.load("images/pixel2.png")
    high_score_image = pygame.image.load("images/pixel.png")
    w,h = play_image.get_width()*scale, play_image.get_height()*scale
    play_image = pygame.transform.scale(play_image,(w,h))
    settings_image = pygame.transform.scale(settings_image,(w,h))
    high_score_image = pygame.transform.scale(high_score_image,(w,h))
    play_button = Button(screen,510*scale,675*scale,w,h,image=play_image,
                         onClick=lambda: play_clicked(screen))
    high_score_image_button = Button(screen,320*scale,675*scale,w,h,image=high_score_image,
                         onClick=lambda: high_score_clicked(screen))
    settings_image_button = Button(screen,700*scale,675*scale,w,h,image=settings_image,
                         onClick=lambda: settings_clicked(screen))
    
    # Add cute little icon
    icon = pygame.image.load('images/icon.png')
    pygame.display.set_icon(icon)
    # Set title
    pygame.display.set_caption("Tetris")
    # Adds the board background image

    # Plays tetris music on repeat
    music = pygame.mixer.music.load("music.mp3")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(.1) 
    
    RUNNING = True
    while RUNNING:
        events = pygame.event.get()
        for event in events:
            # Closes the window if X is pressed
            if event.type == pygame.QUIT:
                RUNNING = False
        screen.blit(start_image, (0, 0))
        

        
        if score == -1:
            RUNNING = False
            
        pygame_widgets.update(events)
        pygame.display.update()
        
    print(score)
        
        

