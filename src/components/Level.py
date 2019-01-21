import pygame

from src.components.SpriteSheet import SpriteSheet
from src.components.Coin import Coin
from src.components.Enemy import Enemy
from src.components.Finish import Finish

from src.utils.getDataFromJSON import getDataFromJSON

class Level:
  def __init__(
    self, screen, colors, camera, solid_tiles, walls, platforms, 
    coins, enemies, finish, player, player_info, level_name
  ):
    # Passed attributes
    self.screen = screen
    self.colors = colors
    self.camera = camera
    self.solid_tiles = solid_tiles
    self.walls = walls
    self.platforms = platforms
    self.coins = coins
    self.enemies = enemies
    self.finish = finish
    self.player = player
    self.player_info = player_info
    # Class attributes
    self.tiles_sheet = SpriteSheet(
      self.screen, 
      self.colors, 
      file_name="tiles.png", 
      scaled_sprite_width=40, 
      scaled_sprite_height=40
    )
    self.level_data = getDataFromJSON("src/levels/{}.json".format(level_name))
    self.is_tutorial = "tutorial" in level_name

  def buildSolidTiles(self):
    for solid_tile_data in self.level_data["solidTiles"]:
      for x in range(solid_tile_data["x"][0], solid_tile_data["x"][1] + 1):
        for y in range(solid_tile_data["y"][0], solid_tile_data["y"][1] + 1):
          self.solid_tiles.append({ "rect": pygame.Rect(x * 40, y * 40, 40, 40) })

  def buildWalls(self):
    for wall_data in self.level_data["walls"]:
      for y in range(wall_data["y"][0], wall_data["y"][1] + 1):
        x = wall_data["x"]
        color = wall_data["color"]
        wall_object = { 
          "rect": pygame.Rect(x * 40, y * 40, 40, 40), 
          "textureName": "wall", 
          "color": color
        }
        self.walls.append(wall_object)

  def buildPlatforms(self):
    for platform_data in self.level_data["platforms"]:
      for x in range(platform_data["x"][0], platform_data["x"][1] + 1):
        y = platform_data["y"]
        color = platform_data["color"]
        platform_object = { 
          "rect": pygame.Rect(x * 40, y * 40, 40, 40), 
          "textureName": "platform", 
          "color": color
        }
        self.platforms.append(platform_object)

  def buildCoins(self):
    for coin_data in self.level_data["coins"]:
      coin = Coin(self.screen, coin_data["x"], coin_data["y"])
      self.coins.append(coin)

  def buildEnemies(self):
    for enemy_data in self.level_data["enemies"]:
      enemy = Enemy(
        self.screen, 
        self.solid_tiles, 
        self.walls, 
        self.platforms, 
        self.player, 
        self.player_info, 
        self.colors, 
        enemy_data["x"], 
        enemy_data["y"]
      )
      self.enemies.append(enemy)

  def buildFinishObject(self):
    width = self.level_data["finish"]["width"]
    height = self.level_data["finish"]["height"]
    x = self.level_data["finish"]["x"] * 40
    y = self.level_data["finish"]["y"] * 40
    finish_object = {
      "x": x,
      "y": y,
      "width": width,
      "height": height,
      "rect": pygame.Rect(x, y, width * 40, height * 40)
    }
    self.finish.append(finish_object)  

  def build(self):
    if "solidTiles" in self.level_data:
      self.buildSolidTiles()
    if "walls" in self.level_data:
      self.buildWalls()
    if "platforms" in self.level_data:
      self.buildPlatforms()
    if "coins" in self.level_data:
      self.buildCoins()
    if "enemies" in self.level_data:
      self.buildEnemies()
    if "finish" in self.level_data:
      self.buildFinishObject()

  def update(self):
    for coin in self.coins:
      coin.updateColor()
    for enemy in self.enemies:
      enemy.update()

  def draw(self):
    for wall in self.walls:
      self.tiles_sheet.drawTextureOnRect(
        texture_name=wall["textureName"], 
        rect=wall["rect"], 
        rect_color=wall["color"], 
        camera=self.camera
      )
    for platform in self.platforms:
      self.tiles_sheet.drawTextureOnRect(
        texture_name=platform["textureName"], 
        rect=platform["rect"], 
        rect_color=platform["color"], 
        camera=self.camera
      )
    for finish in self.finish:
      for w in range(finish["width"]):
        for h in range(finish["height"]):
          self.tiles_sheet.drawTexture(
            texture_name="finish", 
            x=finish["x"] + w * 40,
            y=finish["y"] + h * 40,
            camera=self.camera
          )
    for coin in self.coins:
      coin.draw(self.camera)
    for enemy in self.enemies:
      enemy.draw(self.camera)
    for solid_tile in self.solid_tiles:
      rect_to_display = pygame.Rect(
        solid_tile["rect"].x - self.camera.screen.x, 
        solid_tile["rect"].y - self.camera.screen.y, 
        solid_tile["rect"].width, 
        solid_tile["rect"].height
      )
      pygame.draw.rect(self.screen, self.colors["white"], rect_to_display)
