import pygame
from . import Hero
from . import Generator
from . import Rocket

Rocket = Rocket.Rocket
Generator = Generator.Generator
Hero = Hero.Hero


class Bonus:
    def __init__(self, game, x, y, type):
        self.type = None
        self.game = game
        self.x = x
        self.y = y
        self.size = 16

        if type == 0:
            self.type = "dual rockets"
        elif type == 1:
            self.type = "hp"
        elif type == 2:
            self.type = "points"
        elif type == 3:
            self.type = "newBlocks"
        elif type == 4:
            self.type = "Rocketspeed"

    def gettype(self):
        return self.type

    def getcoords(self):
        return (self.x, self.y)

    def draw(self):
        pygame.draw.rect(self.game.screen,
                         (100, 100, 100),
                         pygame.Rect(self.x, self.y, self.size, self.size))

    def checkCollision(self, game):
        for rocket in game.rockets:
            if (self.x + self.size > rocket.x > self.x and
                    self.y + self.size > rocket.y > self.y):
                try:
                    game.rockets.remove(rocket)
                    game.bonuses.remove(self)
                    self.givebuff(self.game)
                except ValueError:
                    print("5")

        for hero in game.hero:
            if (self.x + self.size > hero.x > self.x and
                    self.y + self.size > hero.y > self.y):
                try:
                    game.bonuses.remove(self)
                except ValueError:
                    print("6")

    def givebuff(self, game):
        pygame.mixer.Sound.play(self.game.buffup)
        if self.type == "dual rockets":
            if Hero.rockets < 4:
                Hero.rockets += 1
            else:
                Hero.rockets = 3
        elif self.type == "hp":
            if self.game.hero[0].lives < 5:
                Hero.oneup(self.game.hero[0])
        elif self.type == "points":
            self.game.score += 50
        elif self.type == "newBlocks":
            Generator.newblocks(self, self.game)
        elif self.type == "Rocketspeed":
            if Rocket.speed < 5:
                Rocket.speed += Rocket.speed * 0.5


