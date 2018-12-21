import pygame

from src.utils.collideRectCircle import collideRectCircle

class Enemy:
  def __init__(self, screen, walls, platforms, player, colors, playerScore):
    self.screen = screen
    self.walls = walls
    self.platforms = platforms
    self.player = player
    self.colors = colors
    self.playerScore = playerScore

    self.transparentSurface = pygame.Surface((1280, 720)).convert_alpha()
    self.rect = pygame.Rect(760, 40, 40, 40)
    self.rangeColor = [155, 100, 155, 50]
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
    if collideRectCircle(self.player.rect, (self.rect.left + 20, self.rect.top + 20), 160):
      if rangeColor[3] < 200:
        self.rangeColor[3] += 2
      else:
        print("DONE")

  def drawEnemy(self):
    # RANGE:
    self.transparentSurface.fill((0, 0, 0, 0))
    pygame.draw.circle(self.transparentSurface, self.rangeColor, (self.rect.left + 20, self.rect.top + 20), 160)
    self.screen.blit(self.transparentSurface, (0, 0))
    # ENEMY:
    pygame.draw.rect(self.screen, self.colors["red"], self.rect)

  def update(self):
    self.gravitySimulation()
    self.drawEnemy()
    self.isPlayerInRange()