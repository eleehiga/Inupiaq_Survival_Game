import sys, pygame

class Env:
  size = width, height = 640, 480
  black = 0, 0, 0

  def __init__(self):
    self.screen = pygame.display.set_mode(self.size)
    self.screen.fill(self.black)

  def disp_obj(self, image, image_rect):
    self.screen.blit(image, image_rect)
