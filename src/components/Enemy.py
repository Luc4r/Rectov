import pygame

from src.utils.collideRectCircle import collideRectCircle

class Enemy:
  def __init__(self, screen, walls, platforms, player, colors, isGameRunning):
    self.screen = screen
    self.walls = walls
    self.platforms = platforms
    self.player = player
    self.colors = colors
    self.deathHandler = isGameRunning

    self.transparentSurface = pygame.Surface((1280, 720)).convert_alpha()
    self.rect = pygame.Rect(25 * 40, 14 * 40, 40, 40)
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
    if self.checkCollision("down"):
      self.isFalling = False
      self.velocityY = 0
    else:
      self.isFalling = True

  def positionCheckOnCollision(self, collisionRect, moveDirection):
    if moveDirection == "up":     # Hit the right side of object
      self.rect.top = collisionRect.bottom
    if moveDirection == "right":  # Hit the right side of object
      self.rect.right = collisionRect.left
    if moveDirection == "down":   # Hit the right side of object
      self.rect.bottom = collisionRect.top
    if moveDirection == "left":   # Hit the right side of object
      self.rect.left = collisionRect.right

  def checkCollision(self, moveDirection):
    for wall in self.walls:
      if self.rect.colliderect(wall.rect):
        self.positionCheckOnCollision(wall.rect, moveDirection)
        return True
    for platform in self.platforms:
      if self.rect.colliderect(platform.rect):
        self.positionCheckOnCollision(platform.rect, moveDirection)
        return True
    return False

  def isPlayerInRange(self):
    rangeColor = self.rangeColor
    maxColorAlpha = 200
    minColorAlpha = 50
    if collideRectCircle(self.player.rect, (self.rect.left + 20, self.rect.top + 20), self.rangeRadius):
      if rangeColor[3] + 2 < maxColorAlpha:
        self.rangeColor[3] += 4
      else:
        self.deathHandler[0] = False
    elif rangeColor[3] - 2 > minColorAlpha:
      self.rangeColor[3] -= 2

  def drawEnemy(self):
    # RANGE:
    self.transparentSurface.fill((0, 0, 0, 0))
    pygame.draw.circle(self.transparentSurface, self.rangeColor, (self.rect.left + 20, self.rect.top + 20), self.rangeRadius)
    self.screen.blit(self.transparentSurface, (0, 0))
    # ENEMY:
    pygame.draw.rect(self.screen, self.colors["red"], self.rect)

  def update(self):
    self.gravitySimulation()
    self.isPlayerInRange()