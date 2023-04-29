import sys, pygame
from env import Env
from old_man import Old_Man
from village import Village
from whale import Whale
from driftwood import Driftwood
from boat import Boat
from timeit import default_timer

pygame.init()

env = Env()

old_man = Old_Man(env.screen_width/2, env.screen_height/2)
village = Village(env.land_wcorner+env.land_width/2,env.land_hcorner+env.land_height)
whale = Whale((env.screen_width+env.land_wcorner+env.land_width)/2, env.screen_height/2)
boat = Boat(-100,-100) # create it but put it off screen
land_mode = True

env.disp_obj(old_man)
# spawn old man to middle of the screen
env.disp_obj(village)
env.disp_obj(whale)

trees = []
for i in range(5):
    obj_tree = Driftwood(env.spawn_driftwood_x(), env.spawn_driftwood_y())
    trees.append(obj_tree)
    env.disp_obj(obj_tree)

# start game time
start = default_timer()

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT: sys.exit()
  # if key pressed
  key_pressed_is = pygame.key.get_pressed()

  if key_pressed_is[pygame.K_a]:
    if(land_mode):
      if(old_man.x > env.land_wcorner):
        old_man.m_left() # will move only if in the land area
    else:
      if(env.can_boat_left(boat)):
        boat.m_left()
  if key_pressed_is[pygame.K_d]:
    if(land_mode):
      if(old_man.x < env.land_wcorner + env.land_width - old_man.width):
        old_man.m_right()
    else:
      if(env.can_boat_right(boat)):
        boat.m_right()
  if key_pressed_is[pygame.K_w]:
    if(land_mode):
      if(old_man.y > env.land_hcorner):
        old_man.m_up()
    else:
      if(env.can_boat_up(boat)):
        boat.m_up()
  if key_pressed_is[pygame.K_s]:
    if(land_mode):
      if(old_man.y < env.land_hcorner + env.land_height - old_man.height):
        old_man.m_down()
    else:
      if(env.can_boat_down(boat)):
        boat.m_down()
  # if attack button
  if key_pressed_is[pygame.K_o]:
    env.destroy_wood(old_man,trees)
  # place button
  if key_pressed_is[pygame.K_p]:
    if(land_mode and old_man.sticks>=3):
      env.ride_boat(old_man,boat)
      land_mode = False
    if(not(land_mode)):
      if(env.kill_whale(boat,whale)):
        print("You completed the game in: "+str(int(default_timer()-start))+" seconds")
        exit()
            
  env.rst_bg()
  env.disp_obj(old_man)
  # spawn old man to middle of the screen
  env.disp_obj(village)
  env.disp_obj(boat)
  env.disp_obj(whale)
  for tree in trees:
      env.disp_obj(tree)
    
  pygame.display.update()
