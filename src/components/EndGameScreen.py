import pygame

from src.components.Coin import Coin

from src.utils.drawText import drawTextCentered
from src.utils.saveDataToJSON import saveResultToJSON

class EndGameScreen:
  def __init__(self, screen, colors, playerInformation, confirmTransition, backToMainMenu, endGameMessage):
    # Passed attributes
    self.screen = screen
    self.colors = colors
    self.playerInformation = playerInformation
    self.confirmTransition = confirmTransition
    self.backToMainMenu = backToMainMenu
    self.endGameMessage = endGameMessage
    # Class attributes
    self.name = ""
    self.coins = [
      Coin(self.screen, 12, 11), 
      Coin(self.screen, 19, 11)
    ]

  def saveScore(self):
    newResult = { "name": self.name, "score": self.playerInformation["score"] }
    saveResultToJSON(newResult)

  def checkInput(self):
    minPlayerNameLength = 3
    maxPlayerNameLength = 15

    for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
        if event.unicode.isalnum() and len(self.name) < maxPlayerNameLength:
          self.name += event.unicode
        elif event.key == pygame.K_BACKSPACE:
          self.name = self.name[:-1]
        elif event.key == pygame.K_RETURN and len(self.name) >= minPlayerNameLength:
          self.saveScore()
          self.confirmTransition()
          self.backToMainMenu()
      elif event.type == pygame.QUIT:
        self.confirmTransition()
        self.backToMainMenu()

  def drawBackground(self):
    self.screen.fill(self.colors["background"])

  def drawEndMessage(self):
    drawTextCentered(self.screen, text=self.endGameMessage, y=200, fontSize=96)

  def drawPlayerScore(self):
    for coin in self.coins:
      coin.draw()
    drawTextCentered(self.screen, text="Points:", y=400, fontSize=36)
    drawTextCentered(self.screen, text="{:06d}".format(self.playerInformation["score"]), y=445, fontSize=36)

  def drawTextInput(self):
    drawTextCentered(self.screen, text="Enter your name:", y=540, fontSize=36)
    drawTextCentered(self.screen, text="{}_".format(self.name), y=580, fontSize=36)

  def draw(self):
    self.checkInput()
    self.drawBackground()
    self.drawEndMessage()
    self.drawPlayerScore()
    self.drawTextInput()