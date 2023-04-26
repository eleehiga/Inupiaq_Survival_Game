import sys, pygame

class Old_Man:
  speed = [2, 2]
  size = 50, 50 
  velocity = 0.1

  def __init__(self, x, y):
    self.image = pygame.transform.scale(pygame.image.load("old_man.jpg"), self.size)
    self.image_rect = self.image.get_rect()
    self.x = x
    self.y = y
  def m_left(self): self.x -= self.velocity
  def m_right(self): self.x += self.velocity
  def m_up(self): self.y -= self.velocity
  def m_down(self): self.y += self.velocity
