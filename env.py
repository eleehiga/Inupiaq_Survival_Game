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
    self.taken.append([obj.x, obj.y, obj.x+obj.width, obj.y+obj.height])
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
    while x == -1 or not(self.conflict_x(x)):
      x = random.randint(int(1.00*self.land_wcorner),int(0.95*(self.land_wcorner+self.land_width)))
    return x
  def spawn_in_land_y(self):
    y = -1
    while y == -1 or not(self.conflict_y(y)):
      y = random.randint(int(1.00*self.land_hcorner),int(0.95*(self.land_hcorner+self.land_height)))
    return y 
  def spawn_driftwood_x(self):
    return self.spawn_in_land_x()
  def spawn_driftwood_y(self):
    return self.spawn_in_land_y()
