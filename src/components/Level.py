import pygame

from src.components.SpriteSheet import SpriteSheet
from src.components.Coin import Coin
from src.components.Enemy import Enemy
from src.components.Finish import Finish

from src.utils.getDataFromJSON import getDataFromJSON

class Level:
  def __init__(self, screen, colors, solidTiles, walls, platforms, coins, enemies, finish, player, playerInformation, levelName):
    # Passed attributes
    self.screen = screen
    self.solidTiles = solidTiles
    self.walls = walls
    self.platforms = platforms
    self.coins = coins
    self.enemies = enemies
    self.finish = finish
    self.player = player
    self.playerInformation = playerInformation
    self.colors = colors
    # Class attributes
    self.tilesSheet = SpriteSheet(self.screen, self.colors, fileName="tiles.png", scaledSpriteWidth=40, scaledSpriteHeight=40)
    self.levelData = getDataFromJSON("src/levels/{}.json".format(levelName))
    self.isTurorial = "tutorial" in levelName

  def buildSolidTiles(self):
    for solidTileData in self.levelData["solidTiles"]:
      for x in range(solidTileData["x"][0], solidTileData["x"][1] + 1):
        for y in range(solidTileData["y"][0], solidTileData["y"][1] + 1):
          self.solidTiles.append({ "rect": pygame.Rect(x * 40, y * 40, 40, 40) })

  def buildWalls(self):
    for wallData in self.levelData["walls"]:
      for y in range(wallData["y"][0], wallData["y"][1] + 1):
        x = wallData["x"]
        color = wallData["color"]
        wallObject = { 
          "rect": pygame.Rect(x * 40, y * 40, 40, 40), 
          "textureName": "wall", 
          "color": color
        }
        self.walls.append(wallObject)

  def buildPlatforms(self):
    for platformData in self.levelData["platforms"]:
      for x in range(platformData["x"][0], platformData["x"][1] + 1):
        y = platformData["y"]
        color = platformData["color"]
        platformObject = { 
          "rect": pygame.Rect(x * 40, y * 40, 40, 40), 
          "textureName": "platform", 
          "color": color
        }
        self.platforms.append(platformObject)

  def buildCoins(self):
    for coinData in self.levelData["coins"]:
      coin = Coin(self.screen, coinData["x"], coinData["y"])
      self.coins.append(coin)

  def buildEnemies(self):
    for enemyData in self.levelData["enemies"]:
      enemy = Enemy(self.screen, self.solidTiles, self.walls, self.platforms, self.player, self.playerInformation, self.colors, enemyData["x"], enemyData["y"])
      self.enemies.append(enemy)

  def buildFinishObject(self):
    x = self.levelData["finish"]["x"]
    y = self.levelData["finish"]["y"]
    width = self.levelData["finish"]["width"]
    height = self.levelData["finish"]["height"]
    finish = Finish(self.screen, self.colors, x, y, width, height)  
    self.finish.append(finish)  

  def build(self):
    if "solidTiles" in self.levelData:
      self.buildSolidTiles()
    if "walls" in self.levelData:
      self.buildWalls()
    if "platforms" in self.levelData:
      self.buildPlatforms()
    if "coins" in self.levelData:
      self.buildCoins()
    if "enemies" in self.levelData:
      self.buildEnemies()
    if "finish" in self.levelData:
      self.buildFinishObject()

  def update(self):
    for enemy in self.enemies:
      enemy.update()

  def draw(self):
    for solidTile in self.solidTiles:
      pygame.draw.rect(self.screen, self.colors["white"], solidTile["rect"])
    for wall in self.walls:
      self.tilesSheet.drawTextureOnRect(textureName=wall["textureName"], rect=wall["rect"], rectColor=wall["color"])
    for platform in self.platforms:
      self.tilesSheet.drawTextureOnRect(textureName=platform["textureName"], rect=platform["rect"], rectColor=platform["color"])
    for coin in self.coins:
      coin.draw()
    for enemy in self.enemies:
      enemy.draw()
    for finish in self.finish:
      finish.draw()