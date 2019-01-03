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
    self.activeOption = 0
    self.isGameRunning = False

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

  def drawBackground(self):
    self.screen.fill(self.colors["background"])

  def drawLogo(self):
    drawTextCentered(self.screen, text="Rectov", y=120, fontSize=128)

  def drawAuthor(self):
    drawText(self.screen, text="KAROL KAPLANEK", x=960, y=690)

  def drawHighestScore(self):
    if self.scores:
      drawTextCentered(self.screen, text="Highest score:", y=600)
      drawTextCentered(self.screen, text="{:06d} - {}".format(self.scores[0]["score"], self.scores[0]["name"]), y=630) 
    else:
      drawTextCentered(self.screen, text="Highest score:", y=600)
      drawTextCentered(self.screen, text="{:06d}".format(0), y=630) 

  def drawOptionDots(self):
    firstDot = pygame.Rect(530, 383, 20, 20)
    secondDot = pygame.Rect(530, 423, 20, 20)
    if self.activeOption == 0:
      pygame.draw.rect(self.screen, self.colors["white"], firstDot)
      pygame.draw.rect(self.screen, self.colors["grey"], secondDot)
    elif self.activeOption == 1:
      pygame.draw.rect(self.screen, self.colors["grey"], firstDot)
      pygame.draw.rect(self.screen, self.colors["white"], secondDot)

  def drawOptions(self):
    self.drawOptionDots()
    inactiveColor = self.colors["grey"]
    activeColor = self.colors["white"]

    if self.activeOption == 0:
      drawText(self.screen, text="START", x=580, y=380, color=activeColor, fontSize=36)
      drawText(self.screen, text="EXIT", x=580, y=420, color=inactiveColor, fontSize=36)
    elif self.activeOption == 1:
      drawText(self.screen, text="START", x=580, y=380, color=inactiveColor, fontSize=36)
      drawText(self.screen, text="EXIT", x=580, y=420, color=activeColor, fontSize=36)  

  def draw(self):
    self.checkInput()
    self.drawBackground()
    self.drawLogo()
    self.drawAuthor()
    self.drawHighestScore()
    self.drawOptions()