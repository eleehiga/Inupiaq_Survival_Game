import sys, pygame

class Env:
  width = 640
  height = 480
  size = width, height
  black = 0, 0, 0

  def __init__(self):
    self.screen = pygame.display.set_mode(self.size)
    self.screen.fill(self.black)

  def disp_obj(self, obj):
    self.screen.fill(self.black) # to reset background
    self.screen.blit(obj.image, (obj.x, obj.y))
