import pygame

class Tile:
  def __init__(self, screen, x, y, tile_color):
    # Passed attributes
    self.screen = screen
    self.color = tile_color
    # Class attributes
    self.rect = pygame.Rect(x * 40, y * 40, 40, 40)

  def draw(self):
    pygame.draw.rect(self.screen, self.color, self.rect)