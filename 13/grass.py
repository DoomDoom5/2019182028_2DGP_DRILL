from pico2d import *

class Grass:
    y = 30
    def __init__(self):
        self.image = load_image('grass.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(400, self.y)


