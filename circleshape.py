from __future__ import annotations
import pygame

class CircleShape(pygame.sprite.Sprite):
    containers: tuple[pygame.sprite.Group, ...]

    def __init__(self, x: float, y: float, radius: float) -> None:
        if hasattr(self, "containers"):
            super().__init__(*self.containers)
        else:
            super().__init__()

        self.position: pygame.Vector2 = pygame.Vector2(x, y)
        self.velocity: pygame.Vector2 = pygame.Vector2(0, 0)
        self.radius: float = radius

    def draw(self, screen: pygame.Surface) -> None:
        raise NotImplementedError("draw not implemented!")

    def update(self, dt: float) -> None:
        raise NotImplementedError("update not implemented!")

    def collides_with(self, other: CircleShape) -> bool:
        if self.position.distance_to(other.position) <= self.radius + other.radius:
            return True
        return False
