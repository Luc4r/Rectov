import pygame

pygame.font.init()
fonts = {
  10: pygame.font.Font("src/font/Chintzy.ttf", 10),
  14: pygame.font.Font("src/font/Chintzy.ttf", 14),
  24: pygame.font.Font("src/font/Chintzy.ttf", 24),
  36: pygame.font.Font("src/font/Chintzy.ttf", 36),
  64: pygame.font.Font("src/font/Chintzy.ttf", 64),
  96: pygame.font.Font("src/font/Chintzy.ttf", 96),
  128: pygame.font.Font("src/font/Chintzy.ttf", 128),
  256: pygame.font.Font("src/font/Chintzy.ttf", 256)
}

def drawText(screen, text, x, y, color=[255, 255, 255], font_size=24):
  text_to_display = fonts[font_size].render(text, 1, color)
  screen.blit(text_to_display, (x, y))

def drawTextCentered(screen, text, y, color=[255, 255, 255], font_size=24):
  text_to_display = fonts[font_size].render(text, 1, color)
  center_x = getCenterX(text_to_display)
  screen.blit(text_to_display, (center_x, y))

def getCenterX(text):
  screen_width = pygame.display.Info().current_w
  text_width = text.get_width()
  center_x = screen_width // 2 - text_width // 2
  return center_x