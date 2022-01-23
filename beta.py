import pygame
import sys
import math
import time
import random
from PIL import Image


class blob(object):
    def __init__(self, x, y, radius, color, speed=5, dir=(random.uniform(-1, 1), random.uniform(-1, 1)), time=random.randint(3, 10), lasttime=time.time()):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.speed = speed
        self.dir = dir
        self.radio = 1
        self.area = math.pi * self.radius**2
        self.prevdir = (random.uniform(-1, 1), random.uniform(-1, 1))
        self.prevrad = 1
        self.time = time
        self.lasttime = lasttime
        # self.image = random.choice(skins)

    def update_radius(self):
        self.radius = int(math.sqrt(self.area / math.pi))

    def update_area(self):
        self.area = math.pi * self.radius**2

    def update_radio(self):
        self.radio = self.area//10000
        self.area -= self.radio

    def update_speed(self):
        self.speed = self.area//10000

    def show(self):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)


def main():
    player = blob(650, 350, 50, red, 5)
    bots = []
    for i in range(30):
        bots.append(blob(random.randint(inix, endx), random.randint(
            iniy, endy), random.randint(20, 120), random.choice(colors)))
    foods = []
    for i in range(200):
        foods.append(blob(random.randint(inix, endx), random.randint(
            iniy, endy), random.randint(4, 7), random.choice(colors)))
    mass = []
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player.area > 2500:
                    mass.append(
                        (blob(player.x+int(player.dir[0]*player.radius), player.y+int(player.dir[1]*player.radius), 20, green, 20, player.dir)))
                    player.area -= mass[-1].area
        mx, my = pygame.mouse.get_pos()
        x = mx - player.x
        y = my - player.y
        if x**2+y**2 > player.radius:
            player.dir = (x/math.sqrt(x**2+y**2), y/math.sqrt(x**2+y**2))
        else:
            player.dir = (0, 0)
        win.fill(black)
        for m in mass:
            m.x -= int(player.dir[0]*player.speed)
            m.y -= int(player.dir[1]*player.speed)
            if math.sqrt((m.x-player.x)**2+(m.y-player.y)**2) < player.radius + 200:
                m.x += int(m.dir[0]*m.speed)
                m.y += int(m.dir[1]*m.speed)
            else:
                m.speed = 0
            if (m.x-player.x)**2+(m.y-player.y)**2 < player.radius**2-1.25*m.radius**2:
                player.area += m.area
                player.update_radius()
                mass.remove(m)
            m.show()
        for food in foods:
            food.x -= int(player.dir[0]*player.speed)
            food.y -= int(player.dir[1]*player.speed)
            if (food.x-player.x)**2+(food.y-player.y)**2 < player.radius**2-1.25*food.radius**2:
                food.x = random.randint(inix, endx)
                food.y = random.randint(inix, endx)
                player.area += food.area
                player.update_radius()
            for bot in bots:
                if (bot.x-food.x)**2+(bot.y-food.y)**2 < bot.radius**2-1.25*food.radius**2:
                    food.x = random.randint(inix, endx)
                    food.y = random.randint(inix, endx)
                    bot.area += food.area
                    bot.update_radius()
            food.show()
        for bot in bots:
            if time.time() - bot.lasttime > bot.time:
                bot.lasttime = time.time()
                x = bot.prevdir[0] + random.uniform(-1, 1)
                y = bot.prevdir[1] + random.uniform(-1, 1)
                if x**2+y**2:
                    bot.dir = (x/math.sqrt(x**2+y**2), y/math.sqrt(x**2+y**2))
                else:
                    bot.dir = (0, 0)
            for m in mass:
                if (bot.x-m.x)**2+(bot.y-m.y)**2 < bot.radius**2-1.25*m.radius**2:
                    bot.area += m.area
                    mass.remove(m)
            bot.update_radio()
            bot.update_radius()
            bot.x -= int(player.dir[0]*player.speed)
            bot.y -= int(player.dir[1]*player.speed)
            bot.x += int(bot.dir[0]*bot.speed)
            bot.y += int(bot.dir[1]*bot.speed)
            if (bot.x-player.x)**2+(bot.y-player.y)**2 < player.radius**2-1.25*bot.radius**2:
                player.area += bot.area
                player.update_radius()
                bot.x = random.randint(inix, endx)
                bot.y = random.randint(inix, endx)
                bot.radius = random.randint(20, 100)
                bot.update_area()
            elif (bot.x-player.x)**2+(bot.y-player.y)**2 < bot.radius**2-1.25*player.radius**2:
                win.blit(pygame.font.SysFont(
                    None, 200).render("GAME OVER", True, white), [150, 250])
                bot.area += player.area
                bot.update_radio()
                pygame.display.update()
                time.sleep(0.5)
                pygame.quit()
                sys.exit()
            for p in bots:
                if (bot.x-p.x)**2+(bot.y-p.y)**2 < p.radius**2-1.1*bot.radius**2:
                    p.area += bot.area
                    p.update_radius()
                    bot.x = random.randint(inix, endx)
                    bot.y = random.randint(inix, endx)
                    bot.radius = random.randint(20, 100)
                    bot.update_area()
                elif (bot.x-p.x)**2+(bot.y-p.y)**2 < bot.radius**2-1.1*p.radius**2:
                    bot.area += p.area
                    bot.update_radius()
                    p.x = random.randint(inix, endx)
                    p.y = random.randint(inix, endx)
                    p.radius = random.randint(20, 100)
                    p.update_area()
            bot.show()
        # player.show()
        if abs(player.radius-player.prevrad) > 7:
            player.prevrad = player.radius
            im.resize((2*player.radius, 2*player.radius)
                      ).save("assets/images/streamworld1.png")
        win.blit(pygame.image.load("assets/images/streamworld1.png"),
                 (player.x-player.radius, player.y-player.radius))
        player.update_radio()
        player.update_radius()
        win.blit(pygame.font.SysFont(
            None, 30).render("Score: "+str(int(player.area)//5), True, white), [10, 10])
        win.blit(pygame.font.SysFont(
            None, int(4*player.radius/(len(name)))).render(name, True, black), [player.x-int(player.radius*0.825), player.y-int(player.radius*(2/len(name)))])
        Clock.tick(fps)
        pygame.display.update()


pygame.init()
win = pygame.display.set_mode((1300, 700))
pygame.display.set_caption("Agario")
white = (255, 255, 255)
black = (0, 0, 0)
green = (51, 204, 89)
red = (250, 51, 51)
blue = (50, 50, 250)
yellow = (250, 250, 50)
colors = [white, red, blue, green, yellow]
fps = 60
Clock = pygame.time.Clock()
inix = -500
iniy = -500
endx = 1500
endy = 1100
name = "ELON"
im = Image.open("assets/images/streamworld.png")


main()
