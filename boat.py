import sys, pygame

class Boat:
  speed = [2, 2]
  width = 50
  height = 50
  size = width, height 
  velocity = 1

  def __init__(self, x, y):
    self.image = pygame.transform.scale(pygame.image.load("pictures/boat.jpg"), self.size)
    self.image_rect = self.image.get_rect()
    self.x = x
    self.y = y
  def m_left(self): self.x -= self.velocity
  def m_right(self): self.x += self.velocity
  def m_up(self): self.y -= self.velocity
  def m_down(self): self.y += self.velocity
