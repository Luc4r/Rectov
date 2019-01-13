import pygame

class Camera:
  def __init__(self, player, levelEndX, levelEndY):
    # Get game window size
    screenWidth, screenHeight = pygame.display.Info().current_w, pygame.display.Info().current_h
    # Passed attributes
    self.player = player
    self.levelEndX = levelEndX
    self.levelEndY = levelEndY
    # Class attributes
    self.screen = pygame.Rect((0, 0, screenWidth, screenHeight))

  def update(self):
    # Horizontal position check
    if self.player.rect.x > self.screen.centerx:
      if self.screen.right < self.levelEndX:
        dx = self.player.rect.x - self.screen.centerx
        self.screen.move_ip(dx, 0)
        if self.screen.right > self.levelEndX:
          self.screen.right = self.levelEndX
    elif self.player.rect.x < self.screen.centerx:
      if self.screen.left > 0:
        dx = self.player.rect.x - self.screen.centerx
        self.screen.move_ip(dx, 0)
        if self.screen.left < 0:
          self.screen.left = 0
    # Vertical position check
    if self.player.rect.y > self.screen.centery:
      if self.screen.bottom < self.levelEndY:
        dy = self.player.rect.y - self.screen.centery
        self.screen.move_ip(0, dy)
        if self.screen.bottom > self.levelEndY:
          self.screen.bottom = self.levelEndY
    elif self.player.rect.y < self.screen.centery:
      if self.screen.top > 0:
        dy = self.player.rect.y - self.screen.centery
        self.screen.move_ip(0, dy)
        if self.screen.top < 0:
          self.screen.top = 0