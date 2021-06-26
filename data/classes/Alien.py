import pygame


class Alien:
    def __init__(self, game, x, y, color):
        self.x = x
        self.game = game
        self.y = y
        self.size = 30
        self.done = False
        self.direction = -1
        self.speed = 1
        self.loop = 0
        self.color = color

    def getcolor(self):
        return self.color

    def getcoords(self):
        return pygame.Rect(self.x, self.y, self.size, self.size)

    def draw(self):

        if self.done:
            self.y += 0
        else:
            if self.x < 0 or self.x > self.game.width - self.size:
                self.y += self.size
            else:
                if self.loop < 5:
                    self.loop += 1
                else:
                    self.loop = 0
                    self.x += self.direction * self.speed

    def lower(self):
        if self.x < 0 or self.x > self.game.width - self.size:

            if self.x < 0:
                self.x = 1
            else:
                self.x = self.game.width - self.size
            return True

    def setDone(self, var):
        self.done = var

    def checkCollision(self, game):
        for rocket in game.rockets:
            if (self.x + self.size > rocket.x > self.x and
                    self.y + self.size  > rocket.y > self.y):
                try:
                    game.rockets.remove(rocket)
                    game.aliens.remove(self)
                    pygame.mixer.Sound.play(game.splat)
                    game.score += 1
                except ValueError:
                    print("4")
