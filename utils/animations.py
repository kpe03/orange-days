
class Animation:
    def __init__(self, images, deltaTime=7):
        self.images = images
        self.index = 0
        self.timer = 0
        self.image = self.images[self.index]
        self.deltaTime = deltaTime
        
    #update frames of animation
    def update(self):
        self.timer += 1
        if self.timer % self.deltaTime == 0:
            if self.index < len(self.images) - 1:
                self.index += 1
            else:
                self.index = 0
        self.image = self.images[self.index]
