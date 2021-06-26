import pygame
from . import Rocket

Rocket = Rocket.Rocket



class Hero:
    lives = 3
    rockets = 1
    def __init__(self, game, x, y):
        self.x = x
        self.game = game
        self.y = y
        self.sizex = 20
        self.sizey = 14
        self.heroinvis = 0
        self.shootcd = 0

    def oneup(self):
        self.lives += 1

    def getcoords(self):
        return pygame.Rect(self.x, self.y, self.sizex, self.sizey)

    def getx(self):
        return self.x

    def gety(self):
        return self.y

    def addscore(self, game, score):
        self.game.score += 50

    def isinvis(self):
        if self.heroinvis > 59:
            return True

    def shootcdf(self):
        if self.shootcd > 59:
            return True

    def draw(self):
        if self.heroinvis < 60:
            self.heroinvis += 1
        if self.shootcd < 60:
            self.shootcd += 1
        pygame.draw.rect(self.game.screen,
                         (210, 250, 251),
                         pygame.Rect(self.x, self.y, 20, 14))

    def shoot(self):
        if self.shootcdf():
            self.shootcd = 0
            if self.rockets == 1:
                self.game.rockets.append(Rocket(self.game, self.x + self.sizex / 2, self.y))
            elif self.rockets == 2:
                self.game.rockets.append(Rocket(self.game, self.x + self.sizex, self.y))
                self.game.rockets.append(Rocket(self.game, self.x, self.y))
            elif self.rockets == 3:
                self.game.rockets.append(Rocket(self.game, self.x + self.sizex / 2, self.y+10))
                self.game.rockets.append(Rocket(self.game, self.x + self.sizex, self.y+5))
                self.game.rockets.append(Rocket(self.game, self.x, self.y))
            else:
                self.game.rockets.append(Rocket(self.game, self.x + self.sizex / 2, self.y+5))
                self.game.rockets.append(Rocket(self.game, self.x + self.sizex, self.y+10))
                self.game.rockets.append(Rocket(self.game, self.x, self.y))
            return True

    def checkCollision(self, game):
        for bullet in game.bullets:
            if (self.x + self.sizex > bullet.x > self.x and
                    self.y + self.sizey > bullet.y > self.y):
                if self.isinvis():
                    self.heroinvis = 0
                    if self.lives == 0:
                        return True
                    else:
                        self.lives -= 1
