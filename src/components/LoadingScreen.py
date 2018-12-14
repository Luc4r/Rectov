import pygame

from src.components.Coin import Coin

from src.utils.displayText import displayText, displayTextCentered

class LoadingScreen:
  def __init__(self, screen, colors, levelName, playerScore):
    self.screen = screen
    self.colors = colors
    self.levelName = levelName
    self.playerScore = playerScore

    self.coinObject = []
    Coin(self.screen, self.coinObject, 13, 16)

  def drawLevelName(self):
    displayTextCentered(self.screen, text=self.levelName, y=200, fontSize=96)

  def drawPlayerScore(self):
    self.coinObject[0].drawCoin()
    displayText(self.screen, text="{:06d}".format(self.playerScore[0]), x=550, y=650)

  def drawLoadingScreen(self):
    self.screen.fill((22, 22, 22))
    self.drawLevelName()
    self.drawPlayerScore()