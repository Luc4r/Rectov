import pygame

from src.components.Coin import Coin

from src.utils.drawText import drawTextCentered
from src.utils.saveDataToJSON import saveResultToJSON

class EndGameScreen:
  def __init__(
    self, screen, colors, player_information, 
    confirm_transition, back_to_main_menu, end_game_message
  ):
    # Passed attributes
    self.screen = screen
    self.colors = colors
    self.player_info = player_information
    self.confirm_transition = confirm_transition
    self.back_to_main_menu = back_to_main_menu
    self.end_game_message = end_game_message
    # Class attributes
    self.name = ""
    self.coins = [
      Coin(self.screen, 12, 11), 
      Coin(self.screen, 19, 11)
    ]

  def saveScore(self):
    new_result = { "name": self.name, "score": self.player_info["score"] }
    saveResultToJSON(new_result)

  def checkInput(self):
    min_name_length = 3
    max_name_length = 15
    events = pygame.event.get()
    for event in events:
      if event.type == pygame.KEYDOWN:
        if event.unicode.isalnum() and len(self.name) < max_name_length:
          self.name += event.unicode
        elif event.key == pygame.K_BACKSPACE:
          self.name = self.name[:-1]
        elif event.key == pygame.K_RETURN and len(self.name) >= min_name_length:
          self.saveScore()
          self.confirm_transition()
          self.back_to_main_menu()
      elif event.type == pygame.QUIT:
        self.confirm_transition()
        self.back_to_main_menu()

  def drawBackground(self):
    self.screen.fill(self.colors["background"])

  def drawEndMessage(self):
    drawTextCentered(
      self.screen, 
      text=self.end_game_message, 
      y=200, 
      font_size=96
    )

  def drawPlayerScore(self):
    for coin in self.coins:
      coin.draw()
      coin.updateColor()
    drawTextCentered(self.screen, text="Points:", y=400, font_size=36)
    drawTextCentered(
      self.screen, 
      text="{:06d}".format(self.player_info["score"]), 
      y=445, 
      font_size=36
    )

  def drawTextInput(self):
    min_name_length = 3
    drawTextCentered(
      self.screen, 
      text="Enter your name:", 
      y=540, 
      font_size=36
    )
    drawTextCentered(
      self.screen, 
      text="{}_".format(self.name), 
      y=580, 
      color=self.colors["red"] if len(self.name) < min_name_length else self.colors["white"],
      font_size=36
    )

  def draw(self):
    self.checkInput()
    self.drawBackground()
    self.drawEndMessage()
    self.drawPlayerScore()
    self.drawTextInput()