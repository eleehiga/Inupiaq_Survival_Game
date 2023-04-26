import sys, pygame

class Old_Man:
  speed = [2, 2]


  def __init__(self):
    self.ball = pygame.image.load("old_man.jpg")

  def get_om(self):
    ballrect = self.ball.get_rect()
    return ballrect
