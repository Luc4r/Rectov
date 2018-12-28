import pygame

from src.components.Wall import Wall
from src.components.Coin import Coin
from src.components.Finish import Finish

from src.utils.getDataFromJSON import getDataFromJSON

class Level:
  def __init__(self, screen, walls, platforms, coins, finish, colors, levelName):
    self.screen = screen
    self.walls = walls
    self.platforms = platforms
    self.coins = coins
    self.finish = finish
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

  def buildFinishObject(self):
    x = self.levelData["finish"]["x"]
    y = self.levelData["finish"]["y"]
    width = self.levelData["finish"]["width"]
    height = self.levelData["finish"]["height"]
    Finish(self.screen, self.colors, self.finish, x, y, width, height)    

  def buildLevel(self):
    self.buildWalls()
    self.buildPlatforms()
    self.buildCoins()
    self.buildFinishObject()

  def drawLevel(self):
    for wall in self.walls:
      wall.drawWall()
    for platform in self.platforms:
      platform.drawWall()
    for coin in self.coins:
      coin.drawCoin()
    self.finish[0].drawFinish()