import pygame

class Wall:
  def __init__(self, screen, walls, x, y, wallColor):
    self.screen = screen
    self.color = wallColor

    self.rect = pygame.Rect(x * 40, y * 40, 40, 40)
    walls.append(self)

  def drawWall(self):
    pygame.draw.rect(self.screen, self.color, self.rect)