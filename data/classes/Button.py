import pygame
from . import Engine

Engine = Engine.Engine
class Button:
    subbuttons = []
    mouse = None

    hovers = pygame.mixer.Sound('./data/sfx/hover.mp3')

    def __init__(self, screen,  size, pos, name):

        self.hovered = False
        self.width = size[0]
        self.height = size[1]
        self.maxheight = self.height * 5
        self.minheight = self.height
        self.position = pos
        self.name = str(name)
        self.screen = screen
        self.size = pygame.Rect(self.position[0], self.position[1], self.width, self.height)

    def draw(self):
        if self.hover():
            pygame.draw.rect(self.screen,
                             (100, 75, 100),
                             self.size)
        else:
            pygame.draw.rect(self.screen,
                             (100, 25, 100),
                             self.size)


    def click(self):
        if self.hover():
            return self.name

    def hover(self):
        mouse = pygame.mouse.get_pos()  # [0] = x    [1] = y
        if self.position[0] <= mouse[0] <= self.position[0] + self.width \
                and self.position[1] <= mouse[1] <= self.position[1] + self.height:
            return True


    def expand(self):
        if self.height < self.maxheight:
            self.height = self.maxheight
            self.size = pygame.Rect(self.position[0], self.position[1], self.width, self.height)

        pygame.draw.rect(self.screen,
                         (25, 150, 25),
                         self.size)

        for x in range(self.position[1], self.position[1] + self.height, 50):
            self.subbuttons.append(Button(self.screen, (self.width, 50), (self.position[0], x), x))

    def hide(self):
        if self.height > self.minheight:
            self.height = self.minheight
            self.size = pygame.Rect(self.position[0], self.position[1], self.width, self.height)
        self.subbuttons.clear()
        pygame.draw.rect(self.screen,
                         (50, 50, 50),
                         self.size)

    def textgen(self, fonts, fontSize, text, textColor, position, yAx):
        pygame.font.init()
        coords = (0,0)
        font = pygame.font.SysFont(fonts, fontSize)
        if position == "centre":
            if yAx:
                coords = (self.position[0] + self.width/2 - (font.size(text)[0] / 2), yAx)
            else:
                coords = (self.position[0] + self.width/2 - (font.size(text)[0] / 2), self.position[1] + self.height/2 - (font.size(text)[1] / 2))
        if position == "left":
            if yAx:
                coords = (self.position[0], yAx)
            else:
                coords = (self.position[0], self.position[1] - self.height/2 - (font.size(text)[1] / 2))
        if position == "right":
            if yAx:
                coords = (self.position[0] - self.width - (font.size(text)[0] / 2), yAx)
            else:
                coords = (self.position[0] - self.width - (font.size(text)[0] / 2), self.position[1] - self.height/2 - (font.size(text)[1] / 2))

        self.screen.blit(font.render(text, False, textColor), coords)
