import pygame
import sys


class blob:
    def __init__(self, color, radius=40):
        self.color = color
        self.radius = radius

    def show(self):
        pygame.draw.circle(win, self.color, (500-self.radius //
                                             2, 300-self.radius//2), self.radius)


class food:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def show(self):
        pygame.draw.circle(win, self.color, (self.x, self.y), 5)


def game():
    global bgx, bgy, b1, f1
    mx, my = pygame.mouse.get_pos()
    if 450 < mx < 550 and 250 < my < 350:
        pass
    else:
        x = mx - 500
        y = my - 300
        bgx -= x/(1+abs(x)) * (abs(x)/500)
        bgy -= y/(1+abs(y))*(abs(y)/500)
        f1.x += int(x/(1+abs(x)) * (abs(x)/500))
        f1.y += int(y/(1+abs(y))*(abs(y)/500))


def main():
    global bgx, bgy, b1, f1
    while True:
        win.blit(bg, (bgx, bgy))
        b1.show()
        f1.show()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        game()
        pygame.display.update()


# imgae = 3840 * 2160
pygame.init()
win = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("Agario")
bg = pygame.image.load("assets/images/bg.jpg")
bgx, bgy = (-1420, -580)
white = (255, 255, 255)
black = (0, 0, 0)
b1 = blob(white)
f1 = food(600, 400, black)

main()
