import pygame

class Finish:
  def __init__(self, screen, colors, finish, x, y, width, height):
    self.screen = screen
    self.colors = colors

    self.rect = pygame.Rect(x * 40, y * 40, width * 40, height * 40)
    finish.append(self)

  def drawFinish(self):
    pygame.draw.rect(self.screen, self.colors["black"], self.rect)