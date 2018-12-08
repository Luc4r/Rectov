import pygame

from src.utils.displayText import displayTextCentered

class LoadingScreen:
  def __init__(self, screen, colors, levelName, playerScore):
    self.screen = screen
    self.colors = colors
    self.levelName = levelName
    self.playerScore = playerScore

  def drawLevelName(self):
    displayTextCentered(self.screen, text=self.levelName, y=200, fontSize=96)

  def drawPlayerScore(self):
    coinObject = pygame.Rect(550, 665, 10, 10)
    pygame.draw.rect(self.screen, self.colors["yellow"], coinObject)
    displayTextCentered(self.screen, text="{:06d}".format(self.playerScore[0]), y=660)

  def drawLoadingScreen(self):
    self.screen.fill((22, 22, 22))
    self.drawLevelName()
    self.drawPlayerScore()