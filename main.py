import pygame
import sys
import math
import random
from PIL import Image


class blob(object):
    def __init__(self, x, y, radius, color, speed=0):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.speed = speed
        self.dir = (0, 0)
        self.area = math.pi * self.radius**2
        self.prevrad = 1

    def update_radius(self):
        self.radius = int(math.sqrt(self.area / math.pi))

    def update_area(self):
        self.area = math.pi * self.radius**2

    def show(self):
        if self.radius > 10:
            if self.radius / self.prevrad > 1.01:
                self.prevrad = self.radius
                im.resize((2*self.radius, 2*self.radius)
                          ).save("assets/images/streamworld1.png")
            win.blit(pygame.image.load("assets/images/streamworld1.png"),
                     (self.x-self.radius, self.y-self.radius))
        else:
            pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)


def main():
    player = blob(500, 300, 30, red, 5)
    posx = player.x
    posy = player.y
    foods = []
    for i in range(2000):
        foods.append(blob(random.randint(inix, endx), random.randint(
            iniy, endy), random.randint(2, 5), random.choice(colors)))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        mx, my = pygame.mouse.get_pos()
        x = mx - player.x
        y = my - player.y
        if x**2+y**2 > player.radius:
            dir = (x/math.sqrt(x**2+y**2), y/math.sqrt(x**2+y**2))
        else:
            dir = (0, 0)
        win.fill(black)
        pygame.draw.rect(win, white, (inix-posx+player.x, iniy-posy+player.y,
                                      endx-inix, endy-iniy), 5)
        if inix <= posx <= endx and iniy <= posy <= endy:
            posx += int(dir[0]*player.speed)
            posy += int(dir[1]*player.speed)
            for food in foods:
                food.x -= int(dir[0]*player.speed)
                food.y -= int(dir[1]*player.speed)
                if (food.x-player.x)**2+(food.y-player.y)**2 < player.radius**2-food.radius**2:
                    food.x = random.randint(
                        inix-posx+player.x, endx-posx+player.x)
                    food.y = random.randint(
                        iniy-posy+player.y, endy-posy+player.y)
                    player.area += food.area
                    player.update_radius()
                food.show()
        else:
            if posx < inix:
                posx = inix
                for food in foods:
                    food.x += int(dir[0]*player.speed)
            elif posx > endx:
                posx = endx
                for food in foods:
                    food.x += int(dir[0]*player.speed)
            if posy < iniy:
                posy = iniy
                for food in foods:
                    food.y += int(dir[1]*player.speed)
            elif posy > endy:
                posy = endy
                for food in foods:
                    food.y += int(dir[1]*player.speed)
        player.show()
        win.blit(pygame.font.SysFont(
            None, 30).render("Score: "+str(int(player.area)//5), True, white), [10, 10])
        win.blit(pygame.font.SysFont(
            None, int(4*player.radius/(len(name)))).render(name, True, white), [500-int(player.radius*0.825), 300-int(player.radius*(2/len(name)))])
        Clock.tick(fps)
        pygame.display.update()


pygame.init()
win = pygame.display.set_mode((1000, 600))
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
name = "AMIT"
im = Image.open("assets/images/streamworld.png")


main()
