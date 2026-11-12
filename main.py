from constants import WINDOW_TITLE
from scoreboard import ScoreBoard, LifeBoard
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from player import Player
import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state, log_event
import sys

def main():
    pygame.init()
    pygame.display.set_caption(WINDOW_TITLE)
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 36)
    dt = 0.0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    updatable = pygame.sprite.Group()
    drawable  = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable)
    ScoreBoard.containers = (drawable,)
    LifeBoard.containers = (drawable,)

    player = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2)
    asteroidField = AsteroidField()

    score_board = ScoreBoard(1, 1, 140, 25, font)
    life_board = LifeBoard(1, 25, 140, 25, font)

    group = pygame.sprite.Group()

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        dt = clock.tick(60) / 1_000
        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                log_event("player_hit")
                player.decrement_life()
                if player.lives <= 0:
                    print("Game over!")
                    sys.exit()
                player.reset()
            for shot in shots:
                if asteroid.collides_with(shot):
                    score_board.update()
                    log_event("asteroid_shot")
                    asteroid.split()
                    shot.kill()

        for to_draw in drawable:
            to_draw.draw(screen)
        life_board.update(lives_left=player.lives)
        pygame.display.flip()

if __name__ == "__main__":
    main()
