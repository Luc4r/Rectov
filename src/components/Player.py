import pygame

class Player:
  def __init__(self, screen, walls, colors):
    self.screen = screen
    self.walls = walls
    self.colors = colors

    self.rect = pygame.Rect(60, 640, 40, 40)
    self.isJumping = False
    self.isHoldingJumpKey = False
    self.velocityX = 6
    self.velocityY = 1
    self.mass = 0.5

  def moveUp(self):
    self.rect.y -= self.velocityY

  def moveDown(self):
    self.rect.y += self.velocityY

  def moveRight(self):
    self.rect.x += self.velocityX

  def moveLeft(self):
    self.rect.x -= self.velocityX

  def jump(self):
    if self.isJumping:
      self.isHoldingJumpKey = True
    else:
      self.isJumping = True
      self.velocityY = 8

  def gravitySimulation(self):
    F = -(0.1 * self.mass * (self.velocityY ** 2))

    self.rect.y = self.rect.y - F
    self.velocityY = self.velocityY + 0.5

    if self.checkCollision("down"):
      self.velocityY = 1

  def jumpSimulation(self):
    if self.velocityY > 0:
      F = (0.5 * self.mass * (self.velocityY ** 2))
    else:
      F = -(0.5 * self.mass * (self.velocityY ** 2))

    # Change position
    self.rect.y = self.rect.y - F

    # Change velocity (when user is holding jump button, player lose velocity slower)
    if self.isHoldingJumpKey:
      self.velocityY = self.velocityY - 0.3
      self.isHoldingJumpKey = False
    else:
      self.velocityY = self.velocityY - 0.5

    # If something is in a way, start falling
    if self.velocityY > 0 and self.checkCollision("up"):
      self.velocityY = 0

    # If ground is reached, reset variables
    if self.checkCollision("down"):
      self.isJumping = False
      self.velocityY = 1

  def checkCollision(self, direction):
    floorLevel = 680
    for wall in self.walls:
      if self.rect.colliderect(wall.rect):
        # Hit the bottom side of the wall + ignore when floor
        if direction == "up" and wall.rect.top < floorLevel:
          self.rect.top = wall.rect.bottom
        # Hit the left side of the wall
        if direction == "right":
          self.rect.right = wall.rect.left
        # Hit the upper side of the wall
        if direction == "down":
          self.rect.bottom = wall.rect.top
        # Hit the right side of the wall
        if direction == "left":
          self.rect.left = wall.rect.right
        return True

  def update(self):
    self.checkInput()
    if self.isJumping:
      self.jumpSimulation()
    else:
      self.gravitySimulation()

  def checkInput(self):
    key = pygame.key.get_pressed()
    if key[pygame.K_UP]:
      self.jump()
    if key[pygame.K_DOWN]:
      self.moveDown()
    if key[pygame.K_LEFT]:
      self.moveLeft()
    if key[pygame.K_RIGHT]:
      self.moveRight()

  def displayPlayer(self):
    pygame.draw.rect(self.screen, self.colors["red"], self.rect)