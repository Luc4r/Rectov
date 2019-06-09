import pygame

from src.utils.collisions import (getNewRectProperties, 
                                  isRectCollisionDetected, 
                                  isRectCircleCollisionDetected)

class Enemy:
  def __init__(
    self, screen, solid_tiles, walls, platforms, 
    player, player_information, colors, x, y
  ):
    # Passed attributes
    self.screen = screen
    self.solid_tiles = solid_tiles
    self.walls = walls
    self.platforms = platforms
    self.player = player
    self.player_info = player_information
    self.colors = colors
    # Class attributes
    self.transparent_surface = pygame.Surface((1280, 720)).convert_alpha()
    self.rect = pygame.Rect(x * 40, y * 40, 40, 40)
    self.range_color = [155, 100, 155, 50]
    self.range_radius = 160
    self.is_falling = False
    self.velocity_y = 0
    self.mass = 1

  def gravitySimulation(self):
    # Change position and velocity
    F = 0.1 * self.mass * (self.velocity_y ** 2)
    self.rect.y += F
    self.velocity_y += 0.5
    # On floor hit - set velocity to default value
    collision_objects = self.walls + self.platforms + self.solid_tiles
    if isRectCollisionDetected(self.rect, collision_objects):
      self.rect = getNewRectProperties(self.rect, collision_objects, "down")
      self.is_falling = False
      self.velocity_y = 0
    else:
      self.is_falling = True

  def isPlayerInRange(self):
    min_alpha = 50
    max_alpha = 200
    alpha_change_value = 3
    if isRectCircleCollisionDetected(
      self.player.rect, 
      (self.rect.left + 20, self.rect.top + 20), 
      self.range_radius
    ):
      if self.range_color[3] + alpha_change_value < max_alpha:
        self.range_color[3] += alpha_change_value
      else:
        self.player_info["alive"] = False
    elif self.range_color[3] - alpha_change_value > min_alpha:
      self.range_color[3] -= alpha_change_value

  def draw(self, camera):
    rect_to_display = pygame.Rect(
      self.rect.x - camera.screen.x, 
      self.rect.y - camera.screen.y, 
      self.rect.width, 
      self.rect.height
    )
    # Reset transparent surface
    self.transparent_surface.fill((0, 0, 0, 0))
    # Draw range
    pygame.draw.circle(
      self.transparent_surface, 
      self.range_color, 
      (rect_to_display.x + 20, rect_to_display.y + 20), 
      self.range_radius
    )
    self.screen.blit(self.transparent_surface, (0, 0))
    # Draw enemy object
    pygame.draw.rect(self.screen, self.colors["red"], rect_to_display)

  def update(self):
    self.gravitySimulation()
    self.isPlayerInRange()