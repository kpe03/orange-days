import utils.config
from utils.config import GameState
from utils.spritesheet import Map
from models.player import Player
from utils.level import Level

class Game():
    def __init__(self, screen):
        self.screen = screen
        self.game_state = GameState.NONE
        self.level = Level()

    def set_up(self):
        self.game_state = GameState.RUNNING
        

    def update(self):
        # self.map.loadMap()
        # self.player.update()
        self.level.update()
        