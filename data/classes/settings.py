import pygame
import time
from . import Button
from . import Engine
from . import Scoreboard
Button = Button.Button
Scoreboard = Scoreboard.Scoreboard
Engine = Engine.Engine


class Settings:
    buttons = []
    resolutionButtonNames = []
    resolutionDimensions = ['600x400', '800x600', '400x800', '1024x500', '1920×1080']
    menus = []
    gameres = (800, 600)
    player = "Player"
    active = False
    def __init__(self):
        pygame.init()
        pygame.mixer.init()

        pygame.display.set_caption("Space Invaders")
        pygame.display.set_icon(pygame.image.load('./data/graphics/alien.png'))

        gamesel = pygame.mixer.Sound('./data/sfx/game.mp3')
        select = pygame.mixer.Sound('./data/sfx/selection.mp3')
        cancelS = pygame.mixer.Sound('./data/sfx/cancel.mp3')

        self.BG = pygame.image.load('./data/graphics/SettingsBG.jpg')
        self.logo = pygame.image.load('./data/graphics/logo.png')
        self.cancel = pygame.image.load('./data/graphics/cancel.png')

        self.width = 800
        self.height = 600
        self.screen = pygame.display.set_mode((self.width, self.height))

        self.clock = pygame.time.Clock()
        done = False
        self.playername = None


        # self.buttons.append(button(self.screen, rozmiar,   pozycja, "nazwa"))
        self.buttons.append(Button(self.screen, (200, 50), (100, 200), "START"))
        self.buttons.append(Button(self.screen, (200, 50), (100, 275), "SCOREBOARD"))
        self.buttons.append(Button(self.screen, (100, 50), (self.width - 125, 25), "PLAYER"))
        self.buttons.append(Button(self.screen, (200, 50), (100, 425), "SETTINGS"))
        self.buttons.append(Button(self.screen, (200, 50), (100, self.height - 100), "QUIT"))
        reso = Button(self.screen, (200, 50), (350, 200), "RESOLUTION")
        cancels = Button(self.screen, (10, 10), (545, 195), "CANCELS")
        while not done:
            for menu in self.menus:
                menu.draw()
            for ev in pygame.event.get():
                if ev.type == pygame.QUIT:
                    pygame.quit()
                if ev.type == pygame.KEYDOWN:
                    if self.active:
                        if ev.key == pygame.K_RETURN:
                            self.player = ''
                        elif ev.key == pygame.K_BACKSPACE:
                            self.player = self.player[:-1]
                        else:
                            self.player += ev.unicode
                if ev.type == pygame.MOUSEBUTTONDOWN:



                    for button in self.buttons:
                        if button.click() == "START":
                            pygame.mixer.Sound.play(gamesel)
                            time.sleep(1)
                            game = Engine(self.gameres, self.playername)
                            pygame.quit()

                        if button.click() == "SCOREBOARD":
                            pygame.mixer.Sound.play(select)
                            self.menus.append(Scoreboard(self))

                        if button.click() == "SETTINGS":
                            pygame.mixer.Sound.play(select)
                            if not self.buttons.__contains__(reso):
                                self.buttons.append(reso)
                                self.buttons.append(cancels)

                        if button.click() == "PLAYER":
                            pygame.mixer.Sound.play(select)
                            self.playername = pygame.rect.Rect(button.position[0], button.position[1]+button.height+20, 100, 50)
                            cancelp = Button(self.screen, (10, 10), (button.position[0]+button.width-5, button.position[1]+button.height+15), "CANCELP")
                            self.buttons.append(cancelp)

                        if button.click() == "CANCELS":
                            pygame.mixer.Sound.play(cancelS)
                            self.buttons.remove(cancels)
                            self.buttons.remove(reso)

                        if button.click() == "CANCELP":
                            pygame.mixer.Sound.play(cancelS)
                            self.buttons.remove(cancelp)
                            self.playername = pygame.rect.Rect(-100, -100, 0, 0)

                        if button.click() == "QUIT":
                            pygame.mixer.Sound.play(cancelS)
                            time.sleep(0.5)
                            pygame.quit()

                        if len(self.resolutionButtonNames) != 0:
                            if button.click() == self.resolutionButtonNames[0]:
                                pygame.mixer.Sound.play(select)
                                self.gameres = (600, 400)
                            if button.click() == self.resolutionButtonNames[1]:
                                pygame.mixer.Sound.play(select)
                                self.gameres = (800, 600)
                            if button.click() == self.resolutionButtonNames[2]:
                                pygame.mixer.Sound.play(select)
                                self.gameres = (200, 800)
                            if button.click() == self.resolutionButtonNames[3]:
                                pygame.mixer.Sound.play(select)
                                self.gameres = (1024, 500)
                            if button.click() == self.resolutionButtonNames[4]:
                                pygame.mixer.Sound.play(select)
                                self.gameres = (1920, 1080)
                    if self.playername is not None:
                        if self.playername.collidepoint(ev.pos[0], ev.pos[1]):
                            self.active = not self.active
                        else:
                            self.active = False
            for button in self.buttons:
                try:
                    button.draw()
                    if button.name in self.resolutionButtonNames:
                        button.textgen("Jockerman", 20,
                                       self.resolutionDimensions[self.resolutionButtonNames.index(button.name)],
                                       (0, 0, 255), "centre", 0)
                    else:
                        if button.name == "CANCELS":
                            self.screen.blit(self.cancel, button.position)
                            continue
                        if button.name == "CANCELP":
                            self.screen.blit(self.cancel, button.position)
                            continue
                        button.textgen("Jockerman", 20, button.name, (0, 0, 255), "centre", 0)

                except UnboundLocalError:
                    print("ERROR 64")

                if button.hover() and button.name == "RESOLUTION" and button.height < button.maxheight:
                    button.expand()
                    for subbutton in button.subbuttons:
                        self.buttons.append(subbutton)
                        self.resolutionButtonNames.append(subbutton.name)

                if not button.hover() and button.name == "RESOLUTION":

                    for subbutton in button.subbuttons:
                        self.buttons.remove(subbutton)
                        self.resolutionButtonNames.clear()
                    button.hide()
                    button.textgen("Jockerman", 20, "Resolution: " + str(self.gameres), (0, 200, 50), "centre", 0)

            pygame.display.flip()

            self.screen.blit(self.BG, (0, 0))
            self.logo = pygame.transform.scale(self.logo, (250, 150))
            self.screen.blit(self.logo, (self.width/2 - self.logo.get_width()/2, 0))

            if self.playername is not None:
                pygame.draw.rect(self.screen, (100, 100, 100), self.playername)
                self.textgen("jockerman", 20, self.player, (0,200,50), (self.playername.center[0]-len(self.player)*3.75, self.playername.y + 15), None)
            self.clock.tick(60)

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
