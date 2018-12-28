import pygame

pygame.font.init()
fonts = {
  10: pygame.font.Font("src/font/Chintzy.ttf", 10),
  14: pygame.font.Font("src/font/Chintzy.ttf", 14),
  24: pygame.font.Font("src/font/Chintzy.ttf", 24),
  36: pygame.font.Font("src/font/Chintzy.ttf", 36),
  64: pygame.font.Font("src/font/Chintzy.ttf", 64),
  96: pygame.font.Font("src/font/Chintzy.ttf", 96),
  128: pygame.font.Font("src/font/Chintzy.ttf", 128)
}

def drawText(screen, text, x, y, color=[255, 255, 255], fontSize=24):
  textToDisplay = fonts[fontSize].render(text, 1, color)
  screen.blit(textToDisplay, (x, y))

def drawTextCentered(screen, text, y, color=[255, 255, 255], fontSize=24):
  textToDisplay = fonts[fontSize].render(text, 1, color)
  centerX = getCenterX(textToDisplay)
  screen.blit(textToDisplay, (centerX, y))

def getCenterX(text):
  screenWidth = 1280
  textWidth = text.get_width()
  centerX = screenWidth // 2 - textWidth // 2
  return centerX