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
    if(old_man.x > env.land_wcorner):
        old_man.m_left() # will move only if in the land area
  if key_pressed_is[pygame.K_d]:
    if(old_man.x < env.land_wcorner + env.land_width - old_man.width):
        old_man.m_right()
  if key_pressed_is[pygame.K_w]:
    if(old_man.y > env.land_hcorner):
        old_man.m_up()
  if key_pressed_is[pygame.K_s]:
    if(old_man.y < env.land_hcorner + env.land_height - old_man.height):
        old_man.m_down()
            
  env.disp_obj(old_man)
  # spawn old man to middle of the screen
  
    
  pygame.display.update()
