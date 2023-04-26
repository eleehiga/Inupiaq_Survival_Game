import sys, pygame
from env import Env
from old_man import Old_Man
pygame.init()

env = Env()

old_man = Old_Man(env.width/2, env.height/2)


while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT: sys.exit()
    # if key pressed
    if event.type == pygame.KEYDOWN: 
        if event.key == pygame.K_a:
            old_man.m_right()
        if event.key == pygame.K_d:
            old_man.m_down()
        if event.key == pygame.K_w:
            old_man.m_up()
        if event.key == pygame.K_s:
            old_man.m_down()
            
  env.disp_obj(old_man)
  # spawn old man to middle of the screen
  
    
  pygame.display.flip()
