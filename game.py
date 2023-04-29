import sys, pygame
from env import Env
from old_man import Old_Man
pygame.init()

env = Env()

old_man = Old_Man(env.screen_width/2, env.screen_height/2)


while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT: sys.exit()
  # if key pressed
  key_pressed_is = pygame.key.get_pressed()

  if key_pressed_is[pygame.K_a]:
    old_man.m_left()
  if key_pressed_is[pygame.K_d]:
    old_man.m_right()
  if key_pressed_is[pygame.K_w]:
    old_man.m_up()
  if key_pressed_is[pygame.K_s]:
    old_man.m_down()
            
  env.disp_obj(old_man)
  # spawn old man to middle of the screen
  
    
  pygame.display.update()
