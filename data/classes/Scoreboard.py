import pygame
from . import Button
Button = Button.Button
class Scoreboard():
    buttons = []
    def __init__(self, game):
        pygame.init()

        self.width = 800
        self.height = 600
        self.game = game
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.sb = open('./data/scoreboard.txt')
        self.done = False
        self.text = self.sb.readlines()
        self.buttons.append(Button(self.screen, (200, 100), ((self.width/2)-100, self.height-100), "MENU"))

#  def textgen(self, fonts, fontSize, text, textColor, position, yAx):
    def draw(self):
        while not self.done:

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for returnB in self.buttons:
                        if returnB.click() == "MENU":
                            self.done = True
                if event.type == pygame.QUIT:
                    self.done = True
            self.screen.fill((0, 0, 0))
            for returnB in self.buttons:
                returnB.draw()
                returnB.textgen("jockerman", 30, "Powrot do menu", (255,255,255), "centre", None)
            self.textgen("jockerman", 40, self.text[0][:-1], (255, 255, 255), "centre", (self.height / 2) - 200)
            self.textgen("jockerman", 40, self.text[1][:-1], (255, 255, 255), "centre", (self.height / 2) - 150)
            self.textgen("jockerman", 40, self.text[2][:-1], (255, 255, 255), "centre", (self.height / 2) - 100)
            self.textgen("jockerman", 40, self.text[3][:-1], (255, 255, 255), "centre", (self.height / 2) - 50)
            self.textgen("jockerman", 40, self.text[4][:-1], (255, 255, 255), "centre", (self.height / 2) )
            pygame.display.flip()
                        

    def textgen(self, fonts, fontSize, text, textColor, position, yAx):
        pygame.font.init()
        coords = (0,0)
        font = pygame.font.SysFont(fonts, fontSize)
        if position == "centre":
            if yAx:
                coords = (self.width / 2 - (font.size(text)[0] / 2), yAx)
            else:
                coords = (self.width / 2 - (font.size(text)[0] / 2), self.height / 2 - (font.size(text)[1] / 2))
        if position == "left":
            if yAx:
                coords = (0, yAx)
            else:
                coords = (0, self.height/2 - (font.size(text)[1] / 2))
        if position == "right":
            if yAx:
                coords = (self.width - font.size(text)[0], yAx)
            else:
                coords = (self.width - font.size(text)[0], self.height / 2 - (font.size(text)[1] / 2))
        if coords == (0, 0) and position != (0, 0):
            coords = position

        self.screen.blit(font.render(text, False, textColor), coords)
