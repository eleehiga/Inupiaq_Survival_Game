import sys, pygame

class Village:
  width = 50
  height = 50
  size = width, height 

  def __init__(self, x, y):
    self.image = pygame.transform.scale(pygame.image.load("pictures/village.jpg"), self.size)
    self.image_rect = self.image.get_rect()
    self.x = x
    self.y = y

