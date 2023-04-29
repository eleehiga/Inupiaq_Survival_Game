import sys, pygame

class Village:
  width = 100
  height = 100
  size = width, height 

  def __init__(self, x, y):
    self.image = pygame.transform.scale(pygame.image.load("pictures/village.jpg"), self.size)
    self.image_rect = self.image.get_rect()
    self.x = x
    self.y = y-self.height # spawn point a little above the water

