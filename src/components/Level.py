import pygame

from src.components.Tile import Tile
from src.components.Coin import Coin
from src.components.Enemy import Enemy
from src.components.Finish import Finish

from src.utils.getDataFromJSON import getDataFromJSON

class Level:
  def __init__(self, screen, colors, walls, platforms, coins, enemies, finish, player, playerInformation, levelName):
    # Passed attributes
    self.screen = screen
    self.walls = walls
    self.platforms = platforms
    self.coins = coins
    self.enemies = enemies
    self.finish = finish
    self.player = player
    self.playerInformation = playerInformation
    self.colors = colors
    # Class attributes
    self.levelData = getDataFromJSON("src/levels/{}.json".format(levelName))
    self.isTurorial = "tutorial" in levelName

  def buildWalls(self):
    for wallData in self.levelData["walls"]:
      for y in range(wallData["y"][0], wallData["y"][1] + 1):
        wall = Tile(self.screen, wallData["x"], y, self.colors[wallData["color"]])
        self.walls.append(wall)

  def buildPlatforms(self):
    for platformData in self.levelData["platforms"]:
      for x in range(platformData["x"][0], platformData["x"][1] + 1):
        platform = Tile(self.screen, x, platformData["y"], self.colors[platformData["color"]])
        self.platforms.append(platform)

  def buildCoins(self):
    if "coins" in self.levelData:
      for coinData in self.levelData["coins"]:
        coin = Coin(self.screen, coinData["x"], coinData["y"])
        self.coins.append(coin)

  def buildEnemies(self):
    if "enemies" in self.levelData:
      for enemyData in self.levelData["enemies"]:
        enemy = Enemy(self.screen, self.walls, self.platforms, self.player, self.playerInformation, self.colors, enemyData["x"], enemyData["y"])
        self.enemies.append(enemy)

  def buildFinishObject(self):
    if "finish" in self.levelData:
      x = self.levelData["finish"]["x"]
      y = self.levelData["finish"]["y"]
      width = self.levelData["finish"]["width"]
      height = self.levelData["finish"]["height"]
      finish = Finish(self.screen, self.colors, x, y, width, height)  
      self.finish.append(finish)  

  def buildFinishBlockade(self):
    if "finish" in self.levelData:
      finishX = self.levelData["finish"]["x"]
      finishY = self.levelData["finish"]["y"]
      finishWidth = self.levelData["finish"]["width"]
      finishHeight = self.levelData["finish"]["height"]
      for x in range(finishX - 1, finishX + finishWidth + 1):
        for y in range(finishY - 1, finishY + finishHeight + 1):
          wall = Tile(self.screen, x, y, self.colors["white"])
          self.walls.append(wall)

  def build(self):
    self.buildWalls()
    self.buildPlatforms()
    self.buildCoins()
    self.buildEnemies()
    self.buildFinishObject()

  def update(self):
    for enemy in self.enemies:
      enemy.update()

  def draw(self):
    for wall in self.walls:
      wall.draw()
    for platform in self.platforms:
      platform.draw()
    for coin in self.coins:
      coin.draw()
    for enemy in self.enemies:
      enemy.draw()
    for finish in self.finish:
      finish.draw()