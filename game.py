from utils.config import GameState
from utils.spritesheet import Map

class Game():
    def __init__(self, screen):
        self.screen = screen
        self.game_state = GameState.NONE
        self.map = Map("utils\\maps\\testmap.json", self.screen)

    def set_up(self):
        self.game_state = GameState.RUNNING

    def update(self):
        self.map.loadMap()
        