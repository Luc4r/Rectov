import pygame

class Tile:
  def __init__(self, screen, x, y, tileColor):
    # Passed attributes
    self.screen = screen
    self.color = tileColor
    # Class attributes
    self.rect = pygame.Rect(x * 40, y * 40, 40, 40)

  def draw(self):
    pygame.draw.rect(self.screen, self.color, self.rect)