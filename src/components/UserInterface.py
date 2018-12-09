import pygame

from src.components.Coin import Coin

from src.utils.displayText import displayText

class UserInterface:
  def __init__(self, screen, colors, levelName, playerScore):
    self.screen = screen
    self.colors = colors
    self.levelName = levelName
    self.playerScore = playerScore
    self.coinIcon = Coin(screen, [], x=25, y=0)

  def drawLevelName(self):
    displayText(self.screen, text=self.levelName, x=100, y=10)

  def drawPlayerScore(self):
    self.coinIcon.drawCoin()
    displayText(self.screen, text="{:06d}".format(self.playerScore[0]), x=1030, y=10)

  def drawUI(self):
    self.drawLevelName()
    self.drawPlayerScore()