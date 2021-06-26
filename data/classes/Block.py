import pygame


class Block:
    def __init__(self, game, x, y):
        self.x = x
        self.game = game
        self.y = y
        self.size = 10

    def getcoords(self):
        return pygame.Rect(self.x, self.y, self.size, self.size)

    def draw(self):
        pygame.draw.rect(self.game.screen,
                         (100, 100, 100),
                         pygame.Rect(self.x, self.y, self.size, self.size))

    def checkCollision(self, game):
        for rocket in game.rockets:
            if (self.x + self.size > rocket.x > self.x and
                    self.y + self.size > rocket.y > self.y ):
                try:
                    game.rockets.remove(rocket)
                    pygame.mixer.Sound.play(game.boomR)
                    game.blocks.remove(self)
                except ValueError:
                    print("1")

        for bullet in game.bullets:
            if (self.x + self.size > bullet.x > self.x and
                    self.y + self.size > bullet.y > self.y):
                try:
                    game.bullets.remove(bullet)
                    game.blocks.remove(self)
                    pygame.mixer.Sound.play(game.boomR)
                except ValueError:
                    print("2")

        for alien in game.aliens:
            if (self.x + self.size > alien.x > self.x and
                    self.y + self.size > alien.y > self.y):
                try:
                    game.aliens.remove(alien)
                    game.blocks.remove(self)
                except ValueError:
                    print("3")