from asteroids.circleshape import CircleShape
from asteroids.constants import (
	INITIAL_SCORE,
	PLAYER_LIVES,
	PLAYER_SHOOT_COOLDOWN_SECONDS,
	PLAYER_TURN_SPEED,
	PLAYER_SPEED,
	PLAYER_SHOOT_SPEED,
	LINE_WIDTH,
	PLAYER_RADIUS,
)

from asteroids.shot import Shot
import pygame


class Player(CircleShape):
	def __init__(self, x: float, y: float) -> None:
		super().__init__(x, y, PLAYER_RADIUS)
		self.rotation = 0
		self.shoot_timer = 0
		self.lives = PLAYER_LIVES
		self.score = INITIAL_SCORE
		self.init_x = x
		self.init_y = y
		self.speed = PLAYER_SPEED
		self.turn_speed = PLAYER_TURN_SPEED

	def reset(self) -> None:
		self.position = pygame.Vector2(self.init_x, self.init_y)
		self.rotation = 0
		self.shoot_timer = 0

	def decrement_life(self) -> None:
		self.lives -= 1

	def increment_life(self) -> None:
		self.lives += 1

	def triangle(self) -> list[pygame.Vector2]:
		forward = pygame.Vector2(0, 1).rotate(self.rotation)
		right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
		a = self.position + forward * self.radius
		b = self.position - forward * self.radius - right
		c = self.position - forward * self.radius + right
		return [a, b, c]

	def draw(self, screen: pygame.Surface) -> None:
		pygame.draw.polygon(screen, 'white', self.triangle(), LINE_WIDTH)

	def rotate(self, dt) -> None:
		self.rotation += self.turn_speed * dt

	def move(self, dt) -> None:
		unit_vector = pygame.Vector2(0, 1)
		rotated_vector = unit_vector.rotate(self.rotation)
		rotated_with_speed_vector = rotated_vector * self.speed * dt
		self.position += rotated_with_speed_vector

	def update(self, dt: float) -> None:
		self.shoot_timer -= dt
		keys = pygame.key.get_pressed()

		if keys[pygame.K_a]:
			self.rotate(dt=-1 * dt)
		if keys[pygame.K_d]:
			self.rotate(dt=dt)
		if keys[pygame.K_w]:
			self.move(dt=dt)
		if keys[pygame.K_s]:
			self.move(dt=-1 * dt)
		if keys[pygame.K_SPACE]:
			self.shoot()

	def shoot(self) -> None:
		if self.shoot_timer > 0:
			return
		self.shoot_timer = PLAYER_SHOOT_COOLDOWN_SECONDS
		shot = Shot(*self.position)
		shot.velocity = (
			pygame.Vector2(0, 1).rotate(self.rotation)
		) * PLAYER_SHOOT_SPEED
