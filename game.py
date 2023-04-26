import sys, pygame
from env import Env
from old_man import Old_Man
pygame.init()

env = Env()

old_man = Old_Man()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    env.disp_obj(old_man.image, old_man.image_rect)
    
    pygame.display.flip()
