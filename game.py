from utils.config import GameState

class Game():
    def __init__(self, screen):
        self.screen = screen
        self.game_state = GameState.NONE

    def set_up(self):
        self.game_state = GameState.RUNNING

    def update(self):
        pass
        