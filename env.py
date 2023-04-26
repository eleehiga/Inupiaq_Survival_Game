import sys, pygame

class Env:
  size = width, height = 320, 240
  black = 0, 0, 0

  def __init__(self):
    screen = pygame.display.set_mode(self.size)
    screen.fill(self.black)
