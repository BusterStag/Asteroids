from circleshape import *
import random
import pygame
from constants import *


class Asteroid(CircleShape):
        def __init__(self, x, y, radius):
            super().__init__(x, y, radius)

        def draw(self, screen):
            pygame.draw.circle(screen,"white",self.position, self.radius, 2)

        def update(self, dt):
            self.position += (self.velocity * dt)

        def split(self):
            self.kill()
            if self.radius <= ASTEROID_MIN_RADIUS:
                return
            traj = random.uniform(20, 50)
            ra1 = self.velocity.rotate(traj)
            ra2 = self.velocity.rotate(-traj)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid.velocity = ra1 * 1.2
            asteroid = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid.velocity = ra2 * 1.2


