from enum import IntEnum

class GameState(IntEnum):
    NONE = 0
    RUNNING = 1
    ENDED = 2
    
#screen dimensions
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
SCREEN_CENTER = [int(SCREEN_WIDTH / 2), int(SCREEN_HEIGHT / 2)]
#tiles:
TILE_SIZE = 16
SCALE = 64

#speed:
WALK_SPEED = 1.2
RUN_SPEED = 1.5

LAYERS = {
    'water': 0,
    'ground': 1,
    'main': 2
}