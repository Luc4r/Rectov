import pygame

from src.components.Coin import Coin

from src.utils.drawText import drawText

class UserInterface:
  def __init__(self, screen, colors, levelName, playerScore):
    self.screen = screen
    self.colors = colors
    self.levelName = levelName
    self.playerScore = playerScore
    self.coinIcon = Coin(screen, [], x=25, y=0)

  def drawLevelName(self):
    drawText(self.screen, text=self.levelName, x=100, y=10)

  def drawPlayerScore(self):
    self.coinIcon.drawCoin()
    drawText(self.screen, text="{:06d}".format(self.playerScore[0]), x=1030, y=10)

  def drawUI(self):
    self.drawLevelName()
    self.drawPlayerScore()