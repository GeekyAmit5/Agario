import pygame
import sys
import math
import random


class blob:
    def __init__(self):
        self.x = 500
        self.y = 300
        self.radius = 30
        self.area = math.pi * self.radius**2
        self.color = red

    def show(self):
        self.radius = int(math.sqrt(self.area / math.pi))
        pygame.draw.circle(win, self.color, (500, 300), self.radius)


class food:
    def __init__(self):
        self.x = random.randint(-1910, 1910)
        self.y = random.randint(-1080, 1080)
        self.radius = random.randint(1, 5)
        self.area = math.pi * self.radius**2
        self.color = random.choice([white, black, red, green, blue, yellow])

    def show(self):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)


class bot:
    def __init__(self):
        self.x = random.randint(-1900, 1900)
        self.y = random.randint(-1050, 1050)
        self.radius = random.randint(10, 50)
        self.area = math.pi * self.radius**2
        self.color = random.choice([white, black, red, green, blue, yellow])

    def show(self):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)


def isCollide(f, b, c):
    if (b.x-f.x)**2 + (b.y-f.y)**2 < c:
        return True
    return False


def main():
    global bgx, bgy
    b1 = blob()
    foods = []
    for i in range(1000):
        foods.append(food())
    bots = []
    for i in range(30):
        bots.append(bot())
    while True:
        win.blit(bg, (bgx, bgy))
        b1.show()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        mx, my = pygame.mouse.get_pos()
        if mx < 450 and bgx < 450 - b1.radius:
            changex = speed
        elif mx > 550 and bgx > -3350 + b1.radius:
            changex = -speed
        else:
            changex = 0

        if my < 250 and bgy < 250 - b1.radius:
            changey = speed
        elif my > 350 and bgy > -1850 + b1.radius:
            changey = -speed
        else:
            changey = 0

        bgx += changex
        bgy += changey
        for f in foods:
            f.show()
            f.x += changex
            f.y += changey
            if (500-f.x)**2 + (300-f.y)**2 < b1.radius**2:
                b1.area += f.area
                f.x = random.randint(-1910, 1910)
                f.y = random.randint(-1080, 1080)
            for b in bots:
                if isCollide(f, b, b.radius**2):
                    b.area += f.area
                    f.x = random.randint(-1910, 1910)
                    f.y = random.randint(-1080, 1080)

        for b in bots:
            b.x += changex
            b.y += changey
            b.show()
            b.x += random.choice([speed, 0, -speed])
            b.y += random.choice([speed, 0, -speed])
            if isCollide(b1, b, 300):
                b1.area += b.area
                b.x = random.randint(-1910, 1910)
                b.y = random.randint(-1080, 1080)

        win.blit(pygame.font.SysFont(
            None, 30).render("Score: "+str(int(b1.area)//2-1400), True, white), [10, 10])
        Clock.tick(fps)
        pygame.display.update()


# imgae = 3840 * 2160
pygame.init()
win = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("Agario")
bg = pygame.image.load("assets/images/bg.jpg")
bgx, bgy = (-1420, -580)
white = (255, 255, 255)
black = (0, 0, 0)
green = (51, 204, 89)
red = (250, 51, 51)
blue = (50, 50, 250)
yellow = (250, 250, 50)
speed = 5
fps = 60
Clock = pygame.time.Clock()


main()
