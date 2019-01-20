import os
import pygame

from src.utils.getDataFromJSON import getDataFromJSON

textures_data = getDataFromJSON("src/config/texturesData.json")

class SpriteSheet:
  def __init__(
    self, screen, colors, file_name, 
    scaled_sprite_width=None, scaled_sprite_height=None
  ):
    # Passed attributes
    self.screen = screen
    self.colors = colors
    self.file_name = file_name.split(".")[0]
    self.sprite_width = (scaled_sprite_width 
                        if scaled_sprite_width 
                        else textures_data[self.file_name]["width"])
    self.sprite_height = (scaled_sprite_height 
                          if scaled_sprite_height 
                          else textures_data[self.file_name]["height"])
    # Variables used to calculate sprites data
    columns = textures_data[self.file_name]["columns"]
    rows = textures_data[self.file_name]["rows"]
    total_sprites = columns * rows
    # Class attributes
    self.sheet = pygame.transform.scale(
      pygame.image.load(os.path.join("src", "img", file_name)).convert_alpha(), 
      (columns * self.sprite_width, rows * self.sprite_height)
    )
    self.sprites = list([
      (
        i % columns * self.sprite_width, 
        int(i / columns) * self.sprite_height, 
        self.sprite_width, 
        self.sprite_height
      ) for i in range(total_sprites)
    ])

  def getTexture(self, texture_name):
    sprite_index = textures_data[self.file_name]["indexes"][texture_name]
    rect_properties = self.sprites[sprite_index]
    return self.sheet.subsurface(pygame.Rect(rect_properties))

  def drawTexture(self, texture_name, x, y, camera):
    sprite_index = textures_data[self.file_name]["indexes"][texture_name]
    # Blit only when is in view range
    if (x + self.sprite_width >= camera.screen.left 
        and x <= camera.screen.right 
        and y + self.sprite_height >= camera.screen.top 
        and y <= camera.screen.bottom
    ):
      self.screen.blit(
        self.sheet, 
        (x - camera.screen.x, y - camera.screen.y), 
        self.sprites[sprite_index]
      )

  def drawTextureOnRect(self, texture_name, rect, rect_color, camera):
    # Blit only when is in view range
    if (rect.x + self.sprite_width >= camera.screen.left 
        and rect.x <= camera.screen.right 
        and rect.y + self.sprite_height >= camera.screen.top 
        and rect.y <= camera.screen.bottom
    ):
      rect_to_display = pygame.Rect(
        rect.x - camera.screen.x, 
        rect.y - camera.screen.y, 
        rect.width, 
        rect.height
      )
      pygame.draw.rect(self.screen, self.colors[rect_color], rect_to_display)
      self.drawTexture(texture_name, rect.x, rect.y, camera)