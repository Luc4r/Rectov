import pygame

from src.components.Coin import Coin

from src.utils.drawText import drawText, drawTextCentered

class LoadingScreen:
  def __init__(self, screen, colors, level_name, player_score):
    # Passed attributes
    self.screen = screen
    self.colors = colors
    self.level_name = level_name
    self.player_score = player_score
    # Class attributes
    self.coin = Coin(self.screen, 13, 16)

  def drawMenuBackground(self):
    self.screen.fill(self.colors["background"])

  def drawLevelName(self):
    drawTextCentered(self.screen, text=self.level_name, y=200, font_size=96)

  def drawPlayerScore(self):
    self.coin.draw()
    self.coin.updateColor()
    drawText(self.screen, text="{:06d}".format(self.player_score), x=550, y=650)

  def draw(self):
    self.drawMenuBackground()
    self.drawLevelName()
    self.drawPlayerScore()