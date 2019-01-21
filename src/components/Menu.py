import sys
import pygame

from src.utils.drawText import drawText, drawTextCentered

class Menu:
  def __init__(self, screen, colors, scores):
    # Passed attributes
    self.screen = screen
    self.colors = colors
    self.scores = scores
    # Class attributes
    self.active_option = 0
    self.is_game_running = False
    self.is_tutorial_running = False

  def checkInput(self):
    events = pygame.event.get()
    for event in events:
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
          pygame.quit()
          sys.exit()
        elif event.key == pygame.K_UP and self.active_option > 0:
          self.active_option -= 1
        elif event.key == pygame.K_DOWN and self.active_option < 2:
          self.active_option += 1
        elif event.key == pygame.K_RETURN:
          # Start tutorial
          if self.active_option == 0:
            self.is_tutorial_running = True
          # Start game
          elif self.active_option == 1:
            self.is_game_running = True
          # Quit
          elif self.active_option == 2:
            pygame.quit()
            sys.exit()

  def drawBackground(self):
    self.screen.fill(self.colors["background"])

  def drawLogo(self):
    drawTextCentered(self.screen, text="Rectov", y=100, font_size=256)

  def drawAuthor(self):
    drawText(self.screen, text='KAROL "Luc4r" KAPLANEK', x=900, y=690)

  def drawHighestScore(self):
    drawTextCentered(self.screen, text="Highest score:", y=600)
    drawTextCentered(
      self.screen, 
      text=("{:06d} - {}".format(self.scores[0]["score"], self.scores[0]["name"]) 
            if self.scores 
            else "{:06d}".format(0)), 
      y=630
    ) 

  def drawOptionDots(self, active_color, inactive_color):
    first_dot = pygame.Rect(430, 395, 20, 20)
    second_dot = pygame.Rect(500, 455, 20, 20)
    third_dot = pygame.Rect(510, 515, 20, 20)
    pygame.draw.rect(
      self.screen, 
      active_color if self.active_option == 0 else inactive_color, 
      first_dot
    )
    pygame.draw.rect(
      self.screen, 
      active_color if self.active_option == 1 else inactive_color, 
      second_dot
    )
    pygame.draw.rect(
      self.screen, 
      active_color if self.active_option == 2 else inactive_color, 
      third_dot
    )

  def drawOptions(self):
    inactive_color = self.colors["grey"]
    active_color = self.colors["white"]
    self.drawOptionDots(active_color, inactive_color)
    drawTextCentered(
      self.screen, 
      text="TUTORIAL", 
      y=380, 
      color=active_color if self.active_option == 0 else inactive_color, 
      font_size=64
    )
    drawTextCentered(
      self.screen, 
      text="PLAY", 
      y=440, 
      color=active_color if self.active_option == 1 else inactive_color, 
      font_size=64
    ) 
    drawTextCentered(
      self.screen, 
      text="EXIT", 
      y=500, 
      color=active_color if self.active_option == 2 else inactive_color, 
      font_size=64
    ) 

  def draw(self):
    self.checkInput()
    self.drawBackground()
    self.drawLogo()
    self.drawAuthor()
    self.drawHighestScore()
    self.drawOptions()