import pygame

from src.components.Coin import Coin

from src.utils.drawText import drawText

class UserInterface:
  def __init__(self, screen, colors, level_name, player_info):
    # Passed attributes
    self.screen = screen
    self.colors = colors
    self.level_name = level_name
    self.player_info = player_info
    # Class attributes
    self.coin = Coin(screen, x=25, y=0)

  def drawLevelName(self):
    drawText(
      self.screen, 
      text=self.level_name, 
      x=100, 
      y=10, 
      color=self.colors["black"]
    )

  def drawPlayerScore(self):
    self.coin.draw()
    self.coin.updateColor()
    drawText(
      self.screen, 
      text="{:06d}".format(self.player_info["score"]), 
      x=1030, 
      y=10, 
      color=self.colors["black"]
    )

  def draw(self):
    self.drawLevelName()
    self.drawPlayerScore()