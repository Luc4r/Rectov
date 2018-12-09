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
    self.isJumping = False
    self.isHoldingJumpKey = False
    self.velocityX = 5
    self.velocityY = 5
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
    self.color = self.colors[newColor]

  def gravitySimulation(self):
    F = -(0.1 * self.mass * (self.velocityY ** 2))
    # Change position and velocity
    self.rect.y -= F
    self.velocityY += 0.5
    # On floor hit - set velocity to default value
    if self.checkCollision("down"):
      self.velocityY = 5

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

  def checkCollision(self, direction):
    for wall in self.walls:
      if self.rect.colliderect(wall.rect) and (self.color == wall.color or wall.color == self.colors["white"]):
        if direction == "up":     # Hit the bottom side of the wall
          self.rect.top = wall.rect.bottom
        if direction == "right":  # Hit the left side of the wall
          self.rect.right = wall.rect.left
        if direction == "down":   # Hit the upper side of the wall
          self.rect.bottom = wall.rect.top
        if direction == "left":   # Hit the right side of the wall
          self.rect.left = wall.rect.right
        return True
    for platform in self.platforms:
      if self.rect.colliderect(platform.rect) and (self.color != platform.color or platform.color == self.colors["white"]):
        if direction == "up":     # Hit the bottom side of the platform
          self.rect.top = platform.rect.bottom
        if direction == "right":  # Hit the left side of the platform
          self.rect.right = platform.rect.left
        if direction == "down":   # Hit the upper side of the platform
          self.rect.bottom = platform.rect.top
        if direction == "left":   # Hit the right side of the platform
          self.rect.left = platform.rect.right
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
    pygame.draw.rect(self.screen, self.colors["black"], self.rect)
    pygame.draw.rect(self.screen, self.color, colorRect)