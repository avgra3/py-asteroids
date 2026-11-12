from logger import log_event
from constants import ASTEROID_MIN_RADIUS
from constants import LINE_WIDTH
from circleshape import CircleShape
import pygame
import random

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, color="white", center=self.position, radius=self.radius, width=LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += (self.velocity * dt)

    def split(self) -> None:
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        rand_angles = random.uniform(20, 50)
        new_ast_one = self.velocity.rotate(rand_angles)
        new_ast_two = self.velocity.rotate(rand_angles * -1)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        print(self.position)
        left = Asteroid(self.position[0], self.position[1], new_radius)
        right = Asteroid(self.position[0], self.position[1], new_radius)
        left.velocity = new_ast_one * 1.2
        right.velocity = new_ast_two * 1.2




