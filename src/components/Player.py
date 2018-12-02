import pygame

class Player:
  def __init__(self, screen, colors):
    self.screen = screen
    self.colors = colors

    self.rect = pygame.Rect(60, 640, 40, 40)
    self.velocity = 6

  def moveUp(self):
    self.rect.y -= self.velocity

  def moveDown(self):
    self.rect.y += self.velocity

  def moveRight(self):
    self.rect.x += self.velocity

  def moveLeft(self):
    self.rect.x -= self.velocity

  def update(self):
    self.checkInput()

  def checkInput(self):
    key = pygame.key.get_pressed()
    if key[pygame.K_UP]:
      self.moveUp()
    if key[pygame.K_DOWN]:
      self.moveDown()
    if key[pygame.K_LEFT]:
      self.moveLeft()
    if key[pygame.K_RIGHT]:
      self.moveRight()

  def displayPlayer(self):
    pygame.draw.rect(self.screen, self.colors["red"], self.rect)