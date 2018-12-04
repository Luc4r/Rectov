import sys
import pygame

from src.utils.displayText import displayText, displayTextCentered

class Menu:
  def __init__(self, screen, colors):
    self.screen = screen
    self.colors = colors
    self.activeOption = 0
    self.isGameRunning = False

  def update(self):
    self.checkInput()
    self.drawMenuBackground()
    self.drawLogo()
    self.drawMenu()

  def drawMenuBackground(self):
    self.screen.fill((22, 22, 22))

  def drawLogo(self):
    displayTextCentered(self.screen, text="Rectov", y=120, fontSize=128)

  def drawMenuDots(self):
    firstDot = pygame.Rect(500, 383, 20, 20)
    secondDot = pygame.Rect(500, 423, 20, 20)
    if self.activeOption == 0:
      pygame.draw.rect(self.screen, self.colors["white"], firstDot)
      pygame.draw.rect(self.screen, self.colors["grey"], secondDot)
    elif self.activeOption == 1:
      pygame.draw.rect(self.screen, self.colors["grey"], firstDot)
      pygame.draw.rect(self.screen, self.colors["white"], secondDot)

  def drawMenu(self):
    self.drawMenuDots()
    displayText(self.screen, text="KAROL KAPLANEK", x=960, y=690)
    inactiveColor = self.colors["grey"]
    activeColor = self.colors["white"]

    if self.activeOption == 0:
      displayText(self.screen, text="START", x=560, y=380, color=activeColor, fontSize=36)
      displayText(self.screen, text="EXIT", x=560, y=420, color=inactiveColor, fontSize=36)
    elif self.activeOption == 1:
      displayText(self.screen, text="START", x=560, y=380, color=inactiveColor, fontSize=36)
      displayText(self.screen, text="EXIT", x=560, y=420, color=activeColor, fontSize=36)  

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
        elif event.key == pygame.K_UP and self.activeOption > 0:
          self.activeOption -= 1
        elif event.key == pygame.K_DOWN and self.activeOption < 1:
          self.activeOption += 1
        elif event.key == pygame.K_RETURN:
          if self.activeOption == 0:
            #START GAME
            self.isGameRunning = True
          elif self.activeOption == 1:
            pygame.quit()
            sys.exit()
    pygame.display.update()