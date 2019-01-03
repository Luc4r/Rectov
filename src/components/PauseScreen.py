import pygame

from src.utils.drawText import drawText, drawTextCentered

class PauseScreen:
  def __init__(self, screen, colors, gameInformation, confirmTransition, backToMainMenu):
    # Passed attributes
    self.screen = screen
    self.colors = colors
    self.gameInformation = gameInformation
    self.confirmTransition = confirmTransition
    self.backToMainMenu = backToMainMenu
    # Class attributes
    self.activeOption = 0
    self.pauseSurface = pygame.Surface((1280, 720), pygame.SRCALPHA)

  def checkInput(self):
    events = pygame.event.get()
    for event in events:
      if event.type == pygame.QUIT:
        self.confirmTransition()
        self.backToMainMenu()
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE or event.key == pygame.K_p:
          self.gameInformation.update({ "pause": False })
        elif event.key == pygame.K_UP and self.activeOption > 0:
          self.activeOption -= 1
        elif event.key == pygame.K_DOWN and self.activeOption < 1:
          self.activeOption += 1
        elif event.key == pygame.K_RETURN:
          if self.activeOption == 0:
            self.gameInformation.update({ "pause": False })
          elif self.activeOption == 1:
            self.confirmTransition()
            self.backToMainMenu()

  def drawBackground(self):
    self.pauseSurface.fill((0, 0, 0, 200))

  def drawPauseMessage(self):
    drawTextCentered(self.pauseSurface, text="PAUSED", y=200, fontSize=96)

  def drawOptionDots(self):
    firstDot = pygame.Rect(500, 383, 20, 20)
    secondDot = pygame.Rect(500, 423, 20, 20)
    if self.activeOption == 0:
      pygame.draw.rect(self.pauseSurface, self.colors["white"], firstDot)
      pygame.draw.rect(self.pauseSurface, self.colors["grey"], secondDot)
    elif self.activeOption == 1:
      pygame.draw.rect(self.pauseSurface, self.colors["grey"], firstDot)
      pygame.draw.rect(self.pauseSurface, self.colors["white"], secondDot)

  def drawOptions(self):
    self.drawOptionDots()
    inactiveColor = self.colors["grey"]
    activeColor = self.colors["white"]

    if self.activeOption == 0:
      drawText(self.pauseSurface, text="RESUME", x=560, y=380, color=activeColor, fontSize=36)
      drawText(self.pauseSurface, text="EXIT", x=560, y=420, color=inactiveColor, fontSize=36)
    elif self.activeOption == 1:
      drawText(self.pauseSurface, text="RESUME", x=560, y=380, color=inactiveColor, fontSize=36)
      drawText(self.pauseSurface, text="EXIT", x=560, y=420, color=activeColor, fontSize=36)  

  def draw(self):
    self.checkInput()
    self.drawBackground()
    self.drawPauseMessage()
    self.drawOptions()
    # Draw pause screen on the screen
    self.screen.blit(self.pauseSurface, (0, 0))
    