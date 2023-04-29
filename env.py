import sys, pygame

class Env:
  screen_width = 640
  screen_height = 480
  land_width = int(screen_width*0.8)
  land_height = int(screen_height*0.8)
  size = screen_width, screen_height
  blue  = 0, 0, 255
  white  = 255, 255, 255

  def __init__(self):
    self.screen = pygame.display.set_mode(self.size)

  def disp_obj(self, obj):
    self.screen.fill(self.blue) # to reset background
    land_wcorner = (self.screen_width-self.land_width)/2
    land_hcorner = (self.screen_height-self.land_height)/2
    rect = (land_wcorner,land_hcorner,land_wcorner+self.land_width,land_hcorner+self.land_height)
    self.screen.fill(self.white, rect) # set part of screen to white
    self.screen.blit(obj.image, (obj.x, obj.y))
