import pygame

class Menu:
  def __init__(self, screen):
    self.screen = screen
    self.activeOption = 0
    self.isGameRunning = False

  def drawRect(self, x, y):
    rect = pygame.Rect(x, y, 40, 40)
    pygame.draw.rect(self.screen, (255, 120, 5), rect)
    pygame.display.update()