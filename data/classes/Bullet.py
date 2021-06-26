import pygame


class Bullet:
    def __init__(self, game, x, y):
        self.x = x
        self.y = y
        self.game = game

    def draw(self):
        pygame.draw.rect(self.game.screen,
                         (0, 255, 0),
                         pygame.Rect(self.x, self.y, 2, 6))
        self.y += 1
