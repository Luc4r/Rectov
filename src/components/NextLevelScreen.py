import pygame

from src.components.Coin import Coin

from src.utils.drawText import drawTextCentered

class NextLevelScreen:
  def __init__(self, screen, colors, playerInformation, confirmTransition, backToMainMenu, nextLevel, currentLevelName):
    # Passed attributes
    self.screen = screen
    self.colors = colors
    self.playerInformation = playerInformation
    self.confirmTransition = confirmTransition
    self.backToMainMenu = backToMainMenu
    self.nextLevel = nextLevel
    self.currentLevelName = currentLevelName
    # Class attributes
    self.coins = [
      Coin(self.screen, 12, 11), 
      Coin(self.screen, 19, 11)
    ]

  def checkInput(self):
    for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
        self.confirmTransition()
        self.nextLevel()
      elif event.type == pygame.QUIT:
        self.confirmTransition()
        self.backToMainMenu()

  def drawBackground(self):
    self.screen.fill(self.colors["background"])

  def drawBeatedLevelName(self):
    drawTextCentered(self.screen, text=self.currentLevelName, y=200, fontSize=96)

  def drawPlayerScore(self):
    for coin in self.coins:
      coin.draw()
    drawTextCentered(self.screen, text="Points:", y=400, fontSize=36)
    drawTextCentered(self.screen, text="{:06d}".format(self.playerInformation["score"]), y=445, fontSize=36)

  def draw(self):
    self.checkInput()
    self.drawBackground()
    self.drawBeatedLevelName()
    self.drawPlayerScore()