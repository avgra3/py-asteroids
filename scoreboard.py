from rectangleshape import RectangleShape
import pygame

class ScoreBoard(RectangleShape):
    def __init__(self, left, top, width, height, font) -> None:
        super().__init__(left, top, width, height)
        self.font = pygame.font.SysFont(None, 36)
        self.score = 0
        self.text = font.render(f"Score: {self.score}", True, (255, 255, 255))

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.rect(surface=screen, rect=self.rectangle, color="blue")
        screen.blit(self.text, self.rectangle)

    def update(self) -> None:
        self.score += 1
        self.text = self.font.render(f"Score: {self.score:,}", True, (255, 255, 255))

class LifeBoard(RectangleShape):
    def __init__(self, left, top, width, height, font) -> None:
        super().__init__(left, top, width, height)
        self.text = font.render("", True, (255, 255, 255))
        self.font = pygame.font.SysFont(None, 36)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.rect(surface=screen, rect=self.rectangle, color="red")
        screen.blit(self.text, self.rectangle)

    def update(self, lives_left: int) -> None:
        self.text = self.font.render(f"Lives left: {lives_left:,}", True, (255, 255, 255))

