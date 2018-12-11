import pygame

class Player:
  def __init__(self, screen, walls, platforms, coins, colors, playerScore):
    self.screen = screen
    self.walls = walls
    self.platforms = platforms
    self.coins = coins
    self.colors = colors
    self.playerScore = playerScore

    self.rect = pygame.Rect(60, 640, 30, 30)
    self.color = colors["red"]
    self.isFalling = False
    self.isJumping = False
    self.isHoldingJumpKey = False
    self.velocityX = 5
    self.velocityY = 5
    self.mass = 0.5

  def handleJump(self):
    if self.isJumping:
      self.isHoldingJumpKey = True
    elif not self.isFalling:
      self.isJumping = True
      self.velocityY = 8

  def handleMoveRight(self):
    self.rect.x += self.velocityX
    self.checkCollision("right")

  def handleMoveLeft(self):
    self.rect.x -= self.velocityX
    self.checkCollision("left")

  def handleChangeColor(self, newColor):
    if not self.isCollisionDetected():
      self.color = self.colors[newColor]

  def gravitySimulation(self):
    F = -(0.1 * self.mass * (self.velocityY ** 2))
    # Change position and velocity
    self.rect.y -= F
    self.velocityY += 0.5
    # On floor hit - set velocity to default value
    if self.checkCollision("down"):
      self.velocityY = 5
      self.isFalling = False
    else:
      self.isFalling = True

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
      self.velocityY = 5

  def update(self):
    self.checkInput()
    if self.isJumping:
      self.jumpSimulation()
    else:
      self.gravitySimulation()
    self.checkCoinPickup()

  def checkInput(self):
    key = pygame.key.get_pressed()
    if key[pygame.K_UP] or key[pygame.K_w] or key[pygame.K_SPACE]:
      self.handleJump()
    if key[pygame.K_LEFT] or key[pygame.K_a]:
      self.handleMoveLeft()
    if key[pygame.K_RIGHT] or key[pygame.K_d]:
      self.handleMoveRight()
    if key[pygame.K_1]:
      self.handleChangeColor("red")
    if key[pygame.K_2]:
      self.handleChangeColor("green")
    if key[pygame.K_3]:
      self.handleChangeColor("blue")

  def positionCheckOnCollision(self, collisionRect, moveDirection):
    if moveDirection == "up":     # Hit the right side of object
      self.rect.top = collisionRect.bottom
    if moveDirection == "right":  # Hit the right side of object
      self.rect.right = collisionRect.left
    if moveDirection == "down":   # Hit the right side of object
      self.rect.bottom = collisionRect.top
    if moveDirection == "left":   # Hit the right side of object
      self.rect.left = collisionRect.right

  def isCollisionDetected(self):
    for wall in self.walls:
      if self.rect.colliderect(wall.rect):
        return True
    for platform in self.platforms:
      if self.rect.colliderect(platform.rect):
        return True
    return False

  def checkCollision(self, moveDirection):
    for wall in self.walls:
      if self.rect.colliderect(wall.rect) and (self.color == wall.color or wall.color == self.colors["white"]):
        self.positionCheckOnCollision(wall.rect, moveDirection)
        return True
    for platform in self.platforms:
      if self.rect.colliderect(platform.rect) and (self.color != platform.color or platform.color == self.colors["white"]):
        self.positionCheckOnCollision(platform.rect, moveDirection)
        return True
    return False

  def checkCoinPickup(self):
    for coin in self.coins:
      if self.rect.colliderect(coin.rect):
        indexOfPickedCoin = self.coins.index(coin)
        self.coins.pop(indexOfPickedCoin)
        self.playerScore[0] += 100

  def displayPlayer(self):
    colorRect = pygame.Rect(self.rect.left + 1, self.rect.top + 1, 28, 28)
    borderColor = [200 if value == 255 else 0 for value in self.color]
    pygame.draw.rect(self.screen, borderColor, self.rect)
    pygame.draw.rect(self.screen, self.color, colorRect)