import pygame

from src.components.Wall import Wall
from src.components.Coin import Coin

from src.utils.getDataFromJSON import getDataFromJSON

class Level:
  def __init__(self, screen, walls, platforms, coins, colors, levelName):
    self.screen = screen
    self.walls = walls
    self.platforms = platforms
    self.coins = coins
    self.colors = colors

    self.levelData = getDataFromJSON("src/levels/{}.json".format(levelName))

  def buildWalls(self):
    for wallData in self.levelData["walls"]:
      for y in range(wallData["y"][0], wallData["y"][1] + 1):
        Wall(self.screen, self.walls, wallData["x"], y, self.colors[wallData["color"]])

  def buildPlatforms(self):
    for platformData in self.levelData["platforms"]:
      for x in range(platformData["x"][0], platformData["x"][1] + 1):
        Wall(self.screen, self.platforms, x, platformData["y"], self.colors[platformData["color"]])

  def buildCoins(self):
    for coinData in self.levelData["coins"]:
      Coin(self.screen, self.coins, coinData["x"], coinData["y"])

  def drawLevel(self):
    for wall in self.walls:
      wall.displayWall()
    for platform in self.platforms:
      platform.displayWall()
    for coin in self.coins:
      coin.drawCoin()