from direct.showbase.ShowBase import ShowBase
from mapmanager import *
from hero import *

class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.set_background_color(0.0, 0.5, 0.75, 1)
        self.land = Mapmanager()   # создаем карту
        self.hero = Hero((2, 4, 1), self.land)
        self.land.loadLand('tg.txt')

        base.camLens.setFov(90)

game = Game()
game.run()