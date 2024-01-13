from models.entity import Entity
from utils.spritesheet import Spritesheet

class Player(Entity):
    def __init__(self, position, screen):
        super(Player, self).__init__(position, screen)
        self.sprite = Spritesheet('assets\Characters\Basic Charakter Spritesheet.png')
        self.animations = self.setUp()

    def setUp(self):
        self.walk = {
            "up": self.sprite.getImageList([49, 52, 55, 58]),
            "down": self.sprite.getImageList([13, 16, 19, 22]),
            "left": self.sprite.getImageList([119, 122, 125, 128]),
            "right": self.sprite.getImageList([85, 88, 91, 94])
        }
        self.idle = {
            "up": self.sprite.getImage(49),
            "down": self.sprite.getImage(13),
            "left": self.sprite.getImage(119),
            "right": self.sprite.getImage(85)
        }

    #todo:vectors?
    def updatePosition(self, coords):
        self.position[0] += coords[0]
        self.position[1] += coords[1]

    #handles input/animation updates
    def update(self):
        pass