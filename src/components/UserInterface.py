import pygame

from src.components.Coin import Coin

from src.utils.drawText import drawText

class UserInterface:
  def __init__(self, screen, colors, levelName, playerInformation):
    # Passed attributes
    self.screen = screen
    self.colors = colors
    self.levelName = levelName
    self.playerInformation = playerInformation
    # Class attributes
    self.coinIcon = Coin(screen, x=25, y=0)

  def drawLevelName(self):
    drawText(self.screen, text=self.levelName, x=100, y=10, color=self.colors["black"])

  def drawPlayerScore(self):
    self.coinIcon.draw()
    drawText(self.screen, text="{:06d}".format(self.playerInformation["score"]), x=1030, y=10, color=self.colors["black"])

  def draw(self):
    self.drawLevelName()
    self.drawPlayerScore()