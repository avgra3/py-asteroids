from asteroids.constants import (
    ICON_PATH,
    BACKGROUND_IMAGE,
    WINDOW_TITLE,
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    EXPLOSION_SOUND,
)
from asteroids.scoreboard import ScoreBoard, LifeBoard
from asteroids.asteroid import Asteroid
from asteroids.asteroidfield import AsteroidField
from asteroids.shot import Shot
from asteroids.player import Player
from asteroids.logger import log_state, log_event
import pygame
import sys


def play_explosion() -> None:
    try:
        pygame.mixer.init()
        pygame.mixer.music.load(EXPLOSION_SOUND)
        pygame.mixer.music.play()
    except pygame.error:
        print("Sound was unable to play: No such audio device!")


def main():
    current_width, current_height = SCREEN_WIDTH, SCREEN_HEIGHT
    pygame.init()
    icon = pygame.image.load(ICON_PATH)
    pygame.display.set_caption(WINDOW_TITLE)
    pygame.display.set_icon(icon)
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 36)
    dt = 0.0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    background = pygame.transform.scale(
        pygame.image.load(BACKGROUND_IMAGE).convert(), (SCREEN_WIDTH, SCREEN_HEIGHT)
    )

    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)  # ty: ignore[invalid-assignment]
    Shot.containers = (shots, updatable, drawable)
    ScoreBoard.containers = (drawable,)
    LifeBoard.containers = (drawable,)

    player = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2)
    asteroidField = AsteroidField()
    score_board = ScoreBoard(0, 1, 140, 25, font)
    life_board = LifeBoard(0, 25, 140, 25, font)

    group = pygame.sprite.Group()

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.VIDEORESIZE:
                new_w = max(SCREEN_WIDTH, min(event.w, SCREEN_WIDTH))
                new_h = max(SCREEN_HEIGHT, min(event.h, SCREEN_HEIGHT))
                current_width, current_height = new_w, new_h
                screen = pygame.display.set_mode((current_width, current_height))
        # screen.fill('black')
        screen.blit(background, (0, 0))
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
                    play_explosion()
                    score_board.update_board()
                    log_event("asteroid_shot")
                    asteroid.split()
                    shot.kill()
                    if score_board.score % 5 == 0:
                        player.increment_life()

        for to_draw in drawable:
            to_draw.draw(screen)
        life_board.update_board(lives_left=player.lives)
        pygame.display.flip()


if __name__ == "__main__":
    main()
