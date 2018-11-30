import pygame

pygame.font.init()
fonts = {
  10: pygame.font.Font("src/font/Chintzy.ttf", 10),
  14: pygame.font.Font("src/font/Chintzy.ttf", 14),
  24: pygame.font.Font("src/font/Chintzy.ttf", 24),
  36: pygame.font.Font("src/font/Chintzy.ttf", 36),
  96: pygame.font.Font("src/font/Chintzy.ttf", 96),
  128: pygame.font.Font("src/font/Chintzy.ttf", 128)
}

def displayText(screen, text, x, y, color=(255, 255, 255), fontSize=14):
  textToDisplay = fonts[fontSize].render(text, 1, color)
  screen.blit(textToDisplay, (x, y))