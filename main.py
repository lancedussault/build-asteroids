import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from bullets import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    bullets = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (bullets, updatable, drawable)

    asteroid_field = AsteroidField()

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 
              
        for obj in updatable:
            obj.update(dt)
        
        for asteroid in asteroids:
            if asteroid.collision(player):
                print("Game Over!")
                sys.exit()

            for bullet in bullets:
                if asteroid.collision(bullet):
                    asteroid.split()
                    bullet.kill()
                    

        screen.fill('black')

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()


        dt = clock.tick(60) / 1000
   
    

if __name__ == "__main__":
    main()