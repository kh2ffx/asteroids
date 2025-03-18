# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    # create game window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0 # delta_time
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    # infinite loop
    while True:
        
        #check if user has closed window and exits the game loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # fill game window with black
        screen.fill("black")

        # draw player
        player.draw(screen)

        # refresh window
        pygame.display.flip()

        # tick
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()

