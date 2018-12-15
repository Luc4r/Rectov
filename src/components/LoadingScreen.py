import pygame

from src.components.Coin import Coin

from src.utils.drawText import drawText, drawTextCentered

class LoadingScreen:
  def __init__(self, screen, colors, levelName, playerScore):
    self.screen = screen
    self.colors = colors
    self.levelName = levelName
    self.playerScore = playerScore

    self.coinObject = []
    Coin(self.screen, self.coinObject, 13, 16)

  def drawMenuBackground(self):
    self.screen.fill(self.colors["background"])

  def drawLevelName(self):
    drawTextCentered(self.screen, text=self.levelName, y=200, fontSize=96)

  def drawPlayerScore(self):
    self.coinObject[0].drawCoin()
    drawText(self.screen, text="{:06d}".format(self.playerScore[0]), x=550, y=650)

  def drawLoadingScreen(self):
    self.drawMenuBackground()
    self.drawLevelName()
    self.drawPlayerScore()