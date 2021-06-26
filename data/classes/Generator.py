import random
from . import Alien
from . import Block
Alien = Alien.Alien
Block = Block.Block


class Generator:
    def __init__(self, game):
        margin = 30
        width = 50
        for x in range(margin, game.width - margin, width):
            for y in range(margin, int(game.height / 2), width):
                game.aliens.append(Alien(game, x, y, random.randint(1, 3)))
        for x in range(margin, game.width - margin, 100):
            game.blocks.append(Block(game, x, game.height - 80))
            game.blocks.append(Block(game, x, game.height - 70))
        for x in range(margin + 10, game.width - margin, 100):
            game.blocks.append(Block(game, x, game.height - 80))
        for x in range(margin + 20, game.width - margin, 100):
            game.blocks.append(Block(game, x, game.height - 80))
        for x in range(margin + 30, game.width - margin, 100):
            game.blocks.append(Block(game, x, game.height - 80))
            game.blocks.append(Block(game, x, game.height - 70))

    def nextLvl(self, game):
        margin = 30
        width = 50
        for x in range(margin, game.width - margin, width):
            for y in range(margin, int(game.height / 2), width):
                game.aliens.append(Alien(game, x, y, random.randint(1, 3)))

    def newblocks(self, game):
        game.blocks.clear()
        margin = 30
        width = 50

        for x in range(margin, game.width - margin, 100):
            game.blocks.append(Block(game, x, game.height - 80))
            game.blocks.append(Block(game, x, game.height - 70))
        for x in range(margin + 10, game.width - margin, 100):
            game.blocks.append(Block(game, x, game.height - 80))
        for x in range(margin + 20, game.width - margin, 100):
            game.blocks.append(Block(game, x, game.height - 80))
        for x in range(margin + 30, game.width - margin, 100):
            game.blocks.append(Block(game, x, game.height - 80))
            game.blocks.append(Block(game, x, game.height - 70))

