import sys, pygame

class Old_Man:
  speed = [2, 2]
  width = 50
  height = 50
  size = width, height 
  velocity = 0.1

  # invetory
  sticks = 0

  def __init__(self, x, y):
    self.image = pygame.transform.scale(pygame.image.load("pictures/old_man.jpg"), self.size)
    self.image_rect = self.image.get_rect()
    self.x = x
    self.y = y
  def m_left(self): self.x -= self.velocity
  def m_right(self): self.x += self.velocity
  def m_up(self): self.y -= self.velocity
  def m_down(self): self.y += self.velocity
