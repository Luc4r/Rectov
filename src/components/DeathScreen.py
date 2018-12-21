import pygame

from src.components.Coin import Coin

from src.utils.drawText import drawTextCentered

class DeathScreen:
  def __init__(self, screen, colors, playerScore, confirmTransition, backToMainMenu):
    self.screen = screen
    self.colors = colors
    self.playerScore = playerScore
    self.confirmTransition = confirmTransition
    self.backToMainMenu = backToMainMenu

    self.name = ""
    self.coinObjects = []

    Coin(self.screen, self.coinObjects, 12, 11)
    Coin(self.screen, self.coinObjects, 19, 11)

  def drawBackground(self):
    self.screen.fill(self.colors["background"])

  def drawDeathMessage(self):
    drawTextCentered(self.screen, text="RECTED", y=200, fontSize=96)

  def drawPlayerScore(self):
    for coin in self.coinObjects:
      coin.drawCoin()
    drawTextCentered(self.screen, text="Points:", y=400, fontSize=36)
    drawTextCentered(self.screen, text="{:06d}".format(self.playerScore[0]), y=445, fontSize=36)

  def drawTextInput(self):
    drawTextCentered(self.screen, text="Enter your name:", y=540, fontSize=36)
    drawTextCentered(self.screen, text="{}_".format(self.name), y=580, fontSize=36)

  def checkInput(self):
    for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
        if event.unicode.isalnum():
          self.name += event.unicode
        elif event.key == pygame.K_BACKSPACE:
          self.name = self.name[:-1]
        elif event.key == pygame.K_RETURN:
          self.confirmTransition()
          self.backToMainMenu()
      elif event.type == pygame.QUIT:
        self.confirmTransition()
        self.backToMainMenu()

  def drawDeathScreen(self):
    self.checkInput()
    self.drawBackground()
    self.drawDeathMessage()
    self.drawPlayerScore()
    self.drawTextInput()