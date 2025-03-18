# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *

def main():
    pygame.init()
    
    # create game window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    # infinite loop
    while True:
        
        #check if user has closed window and exits the game loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # fill game window with black
        pygame.Surface.fill(screen, (0, 0, 0))

        # refresh window
        pygame.display.flip()

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()
