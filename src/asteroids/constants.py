from importlib.resources import files
from pathlib import Path

# Util to get files
def get_static_files(name: str) -> Path:
    return Path(str(files("asteroids") / "static" / name))

# Screen values
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
WINDOW_TITLE = 'Asteroids'
ICON_PATH = get_static_files(name='images/icon.png')

# Generic obj values
LINE_WIDTH = 2

# Player values
PLAYER_RADIUS = 20
PLAYER_TURN_SPEED = 300
PLAYER_SPEED = 200
PLAYER_SHOOT_SPEED = 500
PLAYER_SHOOT_COOLDOWN_SECONDS = 0.3
PLAYER_LIVES = 3

# Shot values
SHOT_RADIUS = 5

# Asteroid values
ASTEROID_MIN_RADIUS = 20
ASTEROID_KINDS = 3
ASTEROID_SPAWN_RATE_SECONDS = 0.8
ASTEROID_MAX_RADIUS = ASTEROID_MIN_RADIUS * ASTEROID_KINDS

# Scoring
INITIAL_SCORE = 0
