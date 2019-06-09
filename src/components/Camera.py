import pygame

class Camera:
  def __init__(self, player, level_end):
    # Get game window size
    screen_width = pygame.display.Info().current_w
    screen_height = pygame.display.Info().current_h
    # Passed attributes
    self.player = player
    self.level_end = level_end
    # Class attributes
    self.screen = pygame.Rect((0, 0, screen_width, screen_height))

  def update(self):
    # Horizontal position check
    if self.player.rect.x > self.screen.centerx:
      if self.screen.right < self.level_end[0]:
        dx = self.player.rect.x - self.screen.centerx
        self.screen.move_ip(dx, 0)
        if self.screen.right > self.level_end[0]:
          self.screen.right = self.level_end[0]
    elif self.player.rect.x < self.screen.centerx:
      if self.screen.left > 0:
        dx = self.player.rect.x - self.screen.centerx
        self.screen.move_ip(dx, 0)
        if self.screen.left < 0:
          self.screen.left = 0
    # Vertical position check
    if self.player.rect.y > self.screen.centery:
      if self.screen.bottom < self.level_end[1]:
        dy = self.player.rect.y - self.screen.centery
        self.screen.move_ip(0, dy)
        if self.screen.bottom > self.level_end[1]:
          self.screen.bottom = self.level_end[1]
    elif self.player.rect.y < self.screen.centery:
      if self.screen.top > 0:
        dy = self.player.rect.y - self.screen.centery   
        self.screen.move_ip(0, dy)
        if self.screen.top < 0:
          self.screen.top = 0