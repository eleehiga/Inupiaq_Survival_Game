import sys, pygame

class Env:
  size = width, height = 320, 240
  speed = [2, 2]
  black = 0, 0, 0
  def __init__(self):
    self.speed = [2, 2]
    self.black = 0, 0, 0

  def set_env(self):
    screen = pygame.display.set_mode(self.size)
    return screen
