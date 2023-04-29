import sys, pygame

class Driftwood:
  width = 30
  height = 30
  size = width, height 

  def __init__(self, x, y):
    self.image = pygame.transform.scale(pygame.image.load("driftwood.jpg"), self.size)
    self.image_rect = self.image.get_rect()
    self.x = x
    self.y = y

