import pygame

from src.components.Coin import Coin

from src.utils.drawText import drawText, drawTextCentered

class LoadingScreen:
  def __init__(self, screen, colors, levelName, playerScore):
    # Passed attributes
    self.screen = screen
    self.colors = colors
    self.levelName = levelName
    self.playerScore = playerScore
    # Class attributes
    self.coinObject = Coin(self.screen, 13, 16)

  def drawMenuBackground(self):
    self.screen.fill(self.colors["background"])

  def drawLevelName(self):
    drawTextCentered(self.screen, text=self.levelName, y=200, fontSize=96)

  def drawPlayerScore(self):
    self.coinObject.draw()
    drawText(self.screen, text="{:06d}".format(self.playerScore), x=550, y=650)

  def draw(self):
    self.drawMenuBackground()
    self.drawLevelName()
    self.drawPlayerScore()