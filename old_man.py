import sys, pygame

class Old_Man:
  speed = [2, 2]

  def __init__(self):
    self.image = pygame.image.load("old_man.jpg")
    self.image_rect = self.image.get_rect()
