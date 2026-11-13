from __future__ import annotations
import pygame


class RectangleShape(pygame.sprite.Sprite):
	containers: tuple[pygame.sprite.Group, ...]

	def __init__(self, left, top, width, height) -> None:
		if hasattr(self, 'containers'):
			super().__init__(*self.containers)
		else:
			super().__init__()
		self.rectangle = pygame.Rect(left, top, width, height)

	def draw(self, screen: pygame.Surface) -> None:
		raise NotImplementedError('draw not implemented')

	def update(self, dt: float) -> None:
		raise NotImplementedError('update not implemented!')
