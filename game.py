import sys, pygame
from env import Env
pygame.init()

env = Env()
screen = env.set_env()

speed = [2, 2]
black = 0, 0, 0

ball = pygame.image.load("old_man.jpg")
ballrect = ball.get_rect()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > env.width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > env.height:
        speed[1] = -speed[1]

    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()
