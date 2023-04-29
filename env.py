import sys, pygame

class Env:
  screen_width = 740
  screen_height = 580
  land_width = screen_width*0.7
  land_height = screen_height*0.7
  size = screen_width, screen_height
  blue  = 0, 0, 255
  white  = 255, 255, 255

  def __init__(self):
    self.screen = pygame.display.set_mode(self.size)
    self.land_wcorner = (self.screen_width-self.land_width)/2
    self.land_hcorner = (self.screen_height-self.land_height)/2
    self.rect = (self.land_wcorner,self.land_hcorner,self.land_width,self.land_height)
    # the end of the rectangle's w,h are relative and not absolute so I need not add the corner values

  def disp_obj(self, obj):
    self.screen.fill(self.blue) # to reset background
    self.screen.fill(self.white, self.rect) # set part of screen to white
    self.screen.blit(obj.image, (obj.x, obj.y))
