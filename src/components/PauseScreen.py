import pygame

from src.utils.drawText import drawText, drawTextCentered

class PauseScreen:
  def __init__(self, screen, colors, game_info, confirm_transition, quit_game):
    # Passed attributes
    self.screen = screen
    self.colors = colors
    self.game_info = game_info
    self.confirm_transition = confirm_transition
    self.quit_game = quit_game
    # Class attributes
    self.active_option = 0
    self.pause_surface = pygame.Surface((1280, 720), pygame.SRCALPHA)

  def checkInput(self):
    events = pygame.event.get()
    for event in events:
      if event.type == pygame.QUIT:
        self.confirm_transition()
        self.quit_game()
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE or event.key == pygame.K_p:
          self.game_info.update({ "pause": False })
        elif event.key == pygame.K_UP and self.active_option > 0:
          self.active_option -= 1
        elif event.key == pygame.K_DOWN and self.active_option < 1:
          self.active_option += 1
        elif event.key == pygame.K_RETURN:
          if self.active_option == 0:
            self.game_info.update({ "pause": False })
          elif self.active_option == 1:
            self.confirm_transition()
            self.quit_game()

  def drawBackground(self): # semi-transparent background
    self.pause_surface.fill((0, 0, 0, 200))

  def drawPauseMessage(self):
    drawTextCentered(self.pause_surface, text="PAUSED", y=200, font_size=96)

  def drawOptionDots(self, active_color, inactive_color):
    first_dot = pygame.Rect(500, 383, 20, 20)
    second_dot = pygame.Rect(500, 423, 20, 20)
    pygame.draw.rect(
      self.pause_surface, 
      active_color if self.active_option == 0 else inactive_color, 
      first_dot
    )
    pygame.draw.rect(
      self.pause_surface, 
      active_color if self.active_option == 1 else inactive_color, 
      second_dot
    )

  def drawOptions(self):
    inactive_color = self.colors["grey"]
    active_color = self.colors["white"]
    self.drawOptionDots(active_color, inactive_color)
    drawText(
      self.pause_surface, 
      text="RESUME", 
      x=560, 
      y=380, 
      color=active_color if self.active_option == 0 else inactive_color, 
      font_size=36
    )
    drawText(
      self.pause_surface, 
      text="EXIT", 
      x=560, 
      y=420, 
      color=active_color if self.active_option == 1 else inactive_color, 
      font_size=36
    ) 

  def draw(self):
    self.checkInput()
    self.drawBackground()
    self.drawPauseMessage()
    self.drawOptions()
    # Draw pause screen on the main screen
    self.screen.blit(self.pause_surface, (0, 0))
    