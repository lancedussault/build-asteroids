import pygame
import random
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, 'white', self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return 
        random_degree = random.uniform(20, 50)
        vector1 = self.velocity.rotate(random_degree)
        vector2 = self.velocity.rotate(-random_degree)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        mini_asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
        mini_asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)

        mini_asteroid_1.velocity = vector1 * 1.2
        mini_asteroid_2.velocity = vector2 * 1.2