import pygame

from src.utils.collisions import getNewRectPropertiesOnCollision, isRectCollisionDetected, isRectCircleCollisionDetected

class Enemy:
  def __init__(self, screen, walls, platforms, player, playerInformation, colors, x, y):
    # Passed attributes
    self.screen = screen
    self.walls = walls
    self.platforms = platforms
    self.player = player
    self.playerInformation = playerInformation
    self.colors = colors
    # Class attributes
    self.transparentSurface = pygame.Surface((1280, 720)).convert_alpha()
    self.rect = pygame.Rect(x * 40, y * 40, 40, 40)
    self.rangeColor = [155, 100, 155, 50]
    self.rangeRadius = 160
    self.isFalling = False
    self.velocityY = 0
    self.mass = 1

  def gravitySimulation(self):
    F = -(0.1 * self.mass * (self.velocityY ** 2))
    # Change position and velocity
    self.rect.y -= F
    self.velocityY += 0.5
    # On floor hit - set velocity to default value
    collisionObjects = self.walls + self.platforms
    if isRectCollisionDetected(self.rect, collisionObjects):
      self.rect = getNewRectPropertiesOnCollision(self.rect, collisionObjects, "down")
      self.isFalling = False
      self.velocityY = 0
    else:
      self.isFalling = True

  def isPlayerInRange(self):
    rangeColor = self.rangeColor
    maxColorAlpha = 200
    minColorAlpha = 50
    if isRectCircleCollisionDetected(self.player.rect, (self.rect.left + 20, self.rect.top + 20), self.rangeRadius):
      if rangeColor[3] + 2 < maxColorAlpha:
        self.rangeColor[3] += 4
      else:
        self.playerInformation["alive"] = False
    elif rangeColor[3] - 2 > minColorAlpha:
      self.rangeColor[3] -= 2

  def draw(self):
    self.transparentSurface.fill((0, 0, 0, 0))
    # RANGE:
    pygame.draw.circle(self.transparentSurface, self.rangeColor, (self.rect.left + 20, self.rect.top + 20), self.rangeRadius)
    self.screen.blit(self.transparentSurface, (0, 0))
    # ENEMY:
    pygame.draw.rect(self.screen, self.colors["red"], self.rect)

  def update(self):
    self.gravitySimulation()
    self.isPlayerInRange()