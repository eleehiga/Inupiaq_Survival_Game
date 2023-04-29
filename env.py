import sys, pygame
import random

class Env:
  screen_width = 840
  screen_height = 680
  land_width = int(screen_width*0.7)
  land_height = int(screen_height*0.7)
  size = screen_width, screen_height
  blue  = 0, 0, 255
  white  = 255, 255, 255
  # rectangles absolute then relative for where an object is
  taken = []
  driftwood_rects = []
  old_man_x = -100
  old_man_y = -100

  def __init__(self):
    self.screen = pygame.display.set_mode(self.size)
    self.land_wcorner = (self.screen_width-self.land_width)//4
    self.land_hcorner = (self.screen_height-self.land_height)//2
    self.rect = (self.land_wcorner,self.land_hcorner,self.land_width,self.land_height)
    # the end of the rectangle's w,h are relative and not absolute so I need not add the corner values
  
  def rst_bg(self):
    self.screen.fill(self.blue) # to reset background
    self.screen.fill(self.white, self.rect) # set part of screen to white
  def disp_obj(self, obj):
    self.screen.blit(obj.image, (obj.x, obj.y))
    obj_rect = [obj.x, obj.y, obj.x+obj.width, obj.y+obj.height]
    self.taken.append(obj_rect)
  def conflict_x(self, x):
    for take in self.taken:
        if(x > take[0] and x < take[2]):
            return True
    return False
  def conflict_y(self, y):
    for take in self.taken:
        if(y > take[1] and y < take[3]):
            return True
    return False
  def spawn_in_land_x(self):
    x = -1
    # complete the loop if true in loop
    while x == -1 or self.conflict_x(x):
      x = random.randint(int(1.01*self.land_wcorner),int(0.95*(self.land_wcorner+self.land_width)))
    return x
  def spawn_in_land_y(self):
    y = -1
    while y == -1 or self.conflict_y(y):
      y = random.randint(int(1.01*self.land_hcorner),int(0.95*(self.land_hcorner+self.land_height)))
    return y 
  def spawn_driftwood_x(self):
    return self.spawn_in_land_x()
  def spawn_driftwood_y(self):
    return self.spawn_in_land_y()
  def destroy_wood(self, old_man, trees):
    for tree in trees:
        if(tree.x > old_man.x and tree.x < old_man.x + old_man.width and tree.y > old_man.y and tree.y < old_man.y + old_man.height):
            tree.x = -100
            tree.y = -100
            old_man.sticks += 1
            print("obtained 1 stick")
  def ride_boat(self, old_man, boat):
      if(old_man.x < 1.01*self.land_wcorner or old_man.y < 1.01*self.land_hcorner or old_man.x > self.land_wcorner+self.land_width-1.1*old_man.width or old_man.y > self.land_hcorner+self.land_height-1.1*old_man.height):
         old_man_x = old_man.x
         old_man_y = old_man.y
         print("riding an umiak",old_man_x)
