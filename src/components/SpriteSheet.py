import os
import pygame

from src.utils.getDataFromJSON import getDataFromJSON

texturesData = getDataFromJSON("src/config/texturesData.json")

class SpriteSheet:
  def __init__(self, screen, colors, fileName, scaledSpriteWidth=None, scaledSpriteHeight=None):
    # Passed attributes
    self.screen = screen
    self.colors = colors
    self.fileName = fileName.split(".")[0]
    self.spriteWidth = scaledSpriteWidth if scaledSpriteWidth else texturesData[self.fileName]["width"]
    self.spriteHeight = scaledSpriteHeight if scaledSpriteHeight else texturesData[self.fileName]["height"]
    # Variables used to calculate sprites data
    columns = texturesData[self.fileName]["columns"]
    rows = texturesData[self.fileName]["rows"]
    totalSprites = columns * rows
    # Class attributes
    self.sheet = pygame.transform.scale(
      pygame.image.load(os.path.join("src", "img", fileName)).convert_alpha(), 
      (columns * self.spriteWidth, rows * self.spriteHeight)
    )
    self.sprites = list([
      (i % columns * self.spriteWidth, int(i / columns) * self.spriteHeight, self.spriteWidth, self.spriteHeight)
      for i in range(totalSprites)
    ])

  def getTexture(self, textureName):
    spriteIndex = texturesData[self.fileName]["indexes"][textureName]
    rectProperties = self.sprites[spriteIndex]
    return self.sheet.subsurface(pygame.Rect(rectProperties))

  def drawTexture(self, textureName, x, y):
    spriteIndex = texturesData[self.fileName]["indexes"][textureName]
    self.screen.blit(self.sheet, (x, y), self.sprites[spriteIndex])

  def drawTextureOnRect(self, textureName, rect, rectColor):
    pygame.draw.rect(self.screen, self.colors[rectColor], rect)
    self.drawTexture(textureName, rect.x, rect.y)