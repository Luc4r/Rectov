import pygame

from src.utils.collisions import correctRectPositionOnCollision, isRectCollisionDetected, isRectCircleCollisionDetected

class Player:
  def __init__(self, screen, colors, walls, platforms, coins, finish, playerInformation):
    # Passed attributes
    self.screen = screen
    self.walls = walls
    self.platforms = platforms
    self.coins = coins
    self.finish = finish
    self.colors = colors
    self.playerInformation = playerInformation
    # Class attributes
    self.rect = pygame.Rect(60, 640, 30, 30)
    self.color = colors["red"]
    self.isFalling = False
    self.isJumping = False
    self.isHoldingJumpKey = False
    self.velocityX = 5
    self.velocityY = 5
    self.mass = 0.35
    self.hasFinished = False
    self.finishAnimationEnded = False

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
    collisionObjects = self.walls + self.platforms
    if not isRectCollisionDetected(self.rect, collisionObjects):
      self.color = self.colors[newColor]

  def gravitySimulation(self):
    F = 0.1 * self.mass * (self.velocityY ** 2)
    # Change position and velocity
    self.rect.y += F
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

  def checkCollision(self, moveDirection):
    for wall in self.walls:
      if self.rect.colliderect(wall.rect) and (self.color == wall.color or wall.color == self.colors["white"]):
        self.rect = correctRectPositionOnCollision(self.rect, wall.rect, moveDirection)
        return True
    for platform in self.platforms:
      if self.rect.colliderect(platform.rect) and (self.color != platform.color or platform.color == self.colors["white"]):
        self.rect = correctRectPositionOnCollision(self.rect, platform.rect, moveDirection)
        return True
    return False

  def checkCoinPickup(self):
    for coin in self.coins:
      if isRectCircleCollisionDetected(self.rect, coin.position, coin.radius):
        indexOfPickedCoin = self.coins.index(coin)
        self.coins.pop(indexOfPickedCoin)
        self.playerInformation.update({ "score": self.playerInformation["score"] + 100 })

  def checkFinishCollision(self):
    if self.rect.colliderect(self.finish[0]):
      # Start finish level animation
      self.hasFinished = True
      self.rect.right = self.finish[0].rect.left

  def checkBorderCollision(self):
    borderX = [0, 1280]
    borderY = [0, 720]
    if self.rect.left < borderX[0] or self.rect.right > borderX[1]:
      self.playerInformation.update({ "alive": False })
    if self.rect.top < borderY[0] or self.rect.bottom > borderY[1]:
      self.playerInformation.update({ "alive": False })

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

  def animationFinish(self):
    halfOfWidthDifference = round((self.finish[0].rect.width - self.rect.width) / 2)
    finishCenterY = round(self.finish[0].rect.top + self.finish[0].rect.height / 2)
    playerCenterY = round(self.rect.top + (self.rect.height / 2))
    # Make sure that player is on the ground
    if self.rect.bottom < self.finish[0].rect.bottom and self.rect.right <= self.finish[0].rect.left:
      self.gravitySimulation()
    # Horizontal animation
    elif self.rect.left - self.finish[0].rect.left < halfOfWidthDifference:
      self.rect.left += 2
    # Vertical animation and size change
    elif playerCenterY > finishCenterY:
      self.rect.top -= 1
      if self.rect.width > 2 and self.rect.top % 5 == 0:
        self.rect.width -= 2
        self.rect.height -= 2
        self.rect.left += 1
    # Animations are done
    else:
      self.finishAnimationEnded = True

  def draw(self):
    colorRect = pygame.Rect(self.rect.left + 2, self.rect.top + 2, self.rect.width - 4, self.rect.height - 4)
    borderColor = [200 if value == 255 else 0 for value in self.color]
    pygame.draw.rect(self.screen, borderColor, self.rect)
    pygame.draw.rect(self.screen, self.color, colorRect)

  def update(self):
    if not self.hasFinished:
      self.checkInput()
      if self.isJumping:
        self.jumpSimulation()
      else:
        self.gravitySimulation()
      self.checkCoinPickup()
      self.checkBorderCollision()
      self.checkFinishCollision()
    else:
      self.animationFinish()
      