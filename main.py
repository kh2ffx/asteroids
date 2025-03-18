# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from asteroidfield import AsteroidField
from asteroid import Asteroid
from shot import Shot

def main():
    pygame.init()
    # create game window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0 # delta_time
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = (updatable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()
    # infinite loop
    while True:
        
        #check if user has closed window and exits the game loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # fill game window with black
        screen.fill("black")

        # update player
        updatable.update(dt)

        # draw player
        for obj in drawable:
            obj.draw(screen)

        # check for collisions
        for asteroid in asteroids:
            if asteroid.collision(player):
                print("Game over")
                return
            for shot in shots:
                if shot.collision(asteroid):
                    shot.kill()
                    asteroid.split()
            
        # refresh window
        pygame.display.flip()

        # tick
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()

