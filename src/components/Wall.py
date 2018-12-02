import pygame

class Wall:
  def __init__(self, screen, colors, walls, x, y):
    self.screen = screen
    self.colors = colors

    self.rect = pygame.Rect(x * 40, y * 40, 40, 40)
    walls.append(self)

  def displayWall(self):
    pygame.draw.rect(self.screen, self.colors["white"], self.rect)