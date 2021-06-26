import pygame
import random
from . import Hero
from . import Rocket
from . import Generator
from . import Block
from . import Bullet
from . import Alien
from . import Bonus

Hero = Hero.Hero
Rocket = Rocket.Rocket
Generator = Generator.Generator
Block = Block.Block
Alien = Alien.Alien
Bullet = Bullet.Bullet
Bonus = Bonus.Bonus
# @end imports


class Engine:
# @lists -----------------------------
    aliens = []
    rockets = []
    bullets = []
    blocks = []
    bonuses = []
    hero = []
# @booleans --------------------------
    lost = False
    done = False
    hit = False
    # screen = None
# --------------------------------
    score = 0
# @Sound
    pygame.mixer.init()
    BGMs = pygame.mixer.Sound('./data/sfx/BGM_start.mp3')
    BGM = pygame.mixer.Sound('./data/sfx/BGM.mp3')
    alienshoot = pygame.mixer.Sound('./data/sfx/alienshoot.mp3')
    buffup = pygame.mixer.Sound('./data/sfx/buff.mp3')
    laser = pygame.mixer.Sound('./data/sfx/laser1.mp3')
    boomR = pygame.mixer.Sound('./data/sfx/boomrock.mp3')
    splat = pygame.mixer.Sound('./data/sfx/splat.mp3')

    def __init__(self, gameres, playername):
        pygame.init()
        pygame.mixer.music.load('./data/sfx/BGM_start.mp3')
        pygame.mixer.music.play()

        self.player = playername
        self.width = gameres[0]
        self.height = gameres[1]
        self.screen = pygame.display.set_mode(gameres)
        pygame.display.set_caption("Space Invaders")
        pygame.display.set_icon(pygame.image.load('./data/graphics/alien.png'))
        self.clock = pygame.time.Clock()
        self.hero.append(Hero(self, self.width / 2, self.height - 20))
        generator = Generator(self)

# @Graphics --------------------------------------------------------------
        self.image_alien1 = pygame.image.load('./data/graphics/alien.png')
        self.image_alien2 = pygame.image.load('./data/graphics/alien2.png')
        self.image_alien3 = pygame.image.load('./data/graphics/alien3.png')
        self.image_rock = pygame.image.load('./data/graphics/rock.png')
        self.image_hero = pygame.image.load('./data/graphics/hero.png')
        self.bonus0 = pygame.image.load('./data/graphics/rocket.png')
        self.bonus1 = pygame.image.load('./data/graphics/hp.png')
        self.bonus2 = pygame.image.load('./data/graphics/ship.png')
        self.bonus3 = pygame.image.load('./data/graphics/shield.png')
        self.bonus4 = pygame.image.load('./data/graphics/speed.png')
        self.background = pygame.image.load('./data/graphics/gameBG.jpg')

# @Main loop -----------------------------------------------------------
        while not self.done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.done = True
                    pygame.quit()
            if not pygame.mixer.music.get_busy():
                pygame.mixer.music.load('./data/sfx/BGM.mp3')
                pygame.mixer.music.play(-1)

            self.text("Wynik: " + str(self.score))
            if len(self.aliens) == 0:
                self.score += 50
                generator.nextLvl(self)
                for alien in self.aliens:
                    alien.speed += 2

            pygame.display.flip()
            self.clock.tick(60)
            self.screen.fill((10, 10, 10))
            for x in range(0, self.width, 450):
                for y in range(0, self.height, 450):
                    self.screen.blit(self.background, (x, y))

# @Aliens   ------------------------------------------------------------
            for alien in self.aliens:
                alien.draw()
                if alien.getcolor() == 1:
                    self.screen.blit(self.image_alien1, alien.getcoords())
                if alien.getcolor() == 2:
                    self.screen.blit(self.image_alien2, alien.getcoords())
                if alien.getcolor() == 3:
                    self.screen.blit(self.image_alien3, alien.getcoords())
                alien.checkCollision(self)
                if alien.lower():
                    for alien in self.aliens:
                        alien.y += 5
                        alien.direction = alien.direction * -1
                if not self.hit:
                    var = random.randint(0, 100000)
                    if alien.y > self.height:
                        self.lost = True
                        self.displayText("Koniec gry! :( Twój wynik to " + str(self.score))
                    if var > 99950:
                        pygame.mixer.Sound.play(self.alienshoot)
                        self.bullets.append(Bullet(self, alien.x + 15, alien.y + 30))

# @Bullets  ------------------------------------------------------------
            for bullet in self.bullets:
                bullet.draw()

# @blocks   ------------------------------------------------------------
            for block in self.blocks:
                block.draw()
                self.screen.blit(self.image_rock, block.getcoords())
                block.checkCollision(self)

# @Bonus    ------------------------------------------------------------
            chance = random.randint(0, 10000)
            if chance > 9990:
                self.bonuses.append(
                    Bonus(self, random.randint(20, self.width - 50), random.randint(0, self.height - 30),
                          random.randint(0, 4)))
            for bonus in self.bonuses:
                if bonus.gettype() == "dual rockets":
                    self.screen.blit(self.bonus0, bonus.getcoords())
                if bonus.gettype() == "hp":
                    self.screen.blit(self.bonus1, bonus.getcoords())
                if bonus.gettype() == "points":
                    self.screen.blit(self.bonus2, bonus.getcoords())
                if bonus.gettype() == "newBlocks":
                    self.screen.blit(self.bonus3, bonus.getcoords())
                if bonus.gettype() == "Rocketspeed":
                    self.screen.blit(self.bonus4, bonus.getcoords())

                bonus.checkCollision(self)

# @Rocket   ------------------------------------------------------------
            for rocket in self.rockets:
                rocket.draw()

# @Hero     ------------------------------------------------------------
            if not self.lost:
                for hero in self.hero:
                    hero.draw()

                    pressed = pygame.key.get_pressed()
                    if pressed[pygame.K_LEFT]:
                        hero.x -= 2 if hero.x > 20 else 0
                    elif pressed[pygame.K_RIGHT]:
                        hero.x += 2 if hero.x < self.width - 20 else 0

                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            self.done = True
                        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and not self.lost:
                            if hero.shoot():
                                pygame.mixer.Sound.play(self.laser)

                    for i in range(0, hero.lives):
                        self.lives(i)
                    self.screen.blit(self.image_hero, hero.getcoords())
                    if hero.checkCollision(self):
                        self.displayText("Koniec gry! Twój wynik to " + str(self.score))
                        self.updatescore(self.score, self.player)
                        for alien in self.aliens:
                            alien.setDone(True)
                            self.lost = True
                        self.hit = True
            else:
                self.displayText("Koniec gry! Twój wynik to " + str(self.score))

# @Text blocks -----------------------------------------------------------------------
    def lives(self, i):
        pygame.font.init()
        font = pygame.font.SysFont('jockerman', 100)
        life = font.render("•", False, (0, 180, 0))
        self.screen.blit(life, (self.width - 20 * i - 20, -15))

    def text(self, text):
        pygame.font.init()
        font = pygame.font.SysFont('jokerman', 20)
        textsurface = font.render(text, False, (0, 180, 0))
        self.screen.blit(textsurface, (0, 0))
        tekst = font.render("Zycia:", False, (0, 180, 0))
        self.screen.blit(tekst, (self.width - 150, 0))

    def displayText(self, text):
        pygame.font.init()
        font = pygame.font.SysFont('jokerman', 30)
        textsurface = font.render(text, False, (0, 180, 0))
        self.screen.blit(textsurface, (self.width / 2 - (font.size(text)[0] / 2), self.height - 50))

    def addscore(self, score):
        self.score += score

    def updatescore(self, score, playername):
        sb = open('./data/scoreboard.txt')
        scoreboard = sb.readlines()
        sb.close()

        sb = open('./data/scoreboard.txt', 'w')
        inserted = False
        for lines in scoreboard:
            print(int(lines[-4:]))
            if score > int(lines[-5:]) and not inserted:
                newval = str(playername) + " " + str(score) + "\n"
                inserted = True
                sb.write(newval)
                sb.write(lines)
                continue
            sb.write(str(lines))


