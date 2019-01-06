import os
import pygame

from src.utils.getDataFromJSON import getDataFromJSON

texturesData = getDataFromJSON("src/config/texturesData.json")

class SpriteSheet:
  def __init__(self, screen, fileName):
    self.screen = screen
    self.sheet = pygame.image.load(os.path.join("src", "img", fileName)).convert_alpha()
    self.fileName = fileName.split(".")[0]

    self.width = texturesData[self.fileName]["width"]
    self.height = texturesData[self.fileName]["height"]
    columns = texturesData[self.fileName]["columns"]
    rows = texturesData[self.fileName]["rows"]

    totalSprites = columns * rows

    self.sprites = list([
      (i % columns * self.width, int(i / columns) * self.height, self.width, self.height)
      for i in range(totalSprites)
    ])

  def getTexture(self, textureName):
    spriteIndex = texturesData[self.fileName]["indexes"][textureName]
    rectProperties = self.sprites[spriteIndex]
    return self.sheet.subsurface(pygame.Rect(rectProperties))

  def drawTexture(self, textureName, x, y):
    spriteIndex = texturesData[self.fileName]["indexes"][textureName]
    self.screen.blit(self.sheet, (x, y), self.sprites[spriteIndex])