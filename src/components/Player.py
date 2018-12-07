import pygame

class Player:
  def __init__(self, screen, walls, colors):
    self.screen = screen
    self.walls = walls
    self.colors = colors

    self.rect = pygame.Rect(60, 640, 40, 40)
    self.color = colors["red"]
    self.isJumping = False
    self.isHoldingJumpKey = False
    self.velocityX = 6
    self.velocityY = 1
    self.mass = 0.5

  def handleJump(self):
    if self.isJumping:
      self.isHoldingJumpKey = True
    else:
      self.isJumping = True
      self.velocityY = 8

  def handleMoveRight(self):
    self.rect.x += self.velocityX
    self.checkCollision("right")

  def handleMoveLeft(self):
    self.rect.x -= self.velocityX
    self.checkCollision("left")

  def handleChangeColor(self, newColor):
    self.color = self.colors[newColor];

  def gravitySimulation(self):
    F = -(0.1 * self.mass * (self.velocityY ** 2))
    # Change position and velocity
    self.rect.y -= F
    self.velocityY += 0.5
    # On floor hit - set velocity to default value
    if self.checkCollision("down"):
      self.velocityY = 1

  def jumpSimulation(self):
    if self.velocityY > 0:
      F = (0.5 * self.mass * (self.velocityY ** 2))
    else:
      F = -(0.5 * self.mass * (self.velocityY ** 2))
    # Change position
    self.rect.y -= F
    # Change velocity (when user is holding jump button, player lose velocity slower)
    if self.isHoldingJumpKey:
      self.velocityY -= 0.25
      self.isHoldingJumpKey = False
    else:
      self.velocityY -= 0.45
    # If something is in a way, start falling
    if self.velocityY > 0 and self.checkCollision("up"):
      self.velocityY = 0
    # If ground is reached, reset variables
    if self.checkCollision("down"):
      self.isJumping = False
      self.velocityY = 1

  def update(self):
    self.checkInput()
    if self.isJumping:
      self.jumpSimulation()
    else:
      self.gravitySimulation()

  def checkInput(self):
    key = pygame.key.get_pressed()
    if key[pygame.K_UP]:
      self.handleJump()
    if key[pygame.K_LEFT]:
      self.handleMoveLeft()
    if key[pygame.K_RIGHT]:
      self.handleMoveRight()
    if key[pygame.K_1]:
      self.handleChangeColor("red")
    if key[pygame.K_2]:
      self.handleChangeColor("green")
    if key[pygame.K_3]:
      self.handleChangeColor("blue")

  def checkCollision(self, direction):
    for wall in self.walls:
      if self.rect.colliderect(wall.rect):
        # Hit the bottom side of the wall
        if direction == "up":
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
    return False

  def displayPlayer(self):
    pygame.draw.rect(self.screen, self.color, self.rect)