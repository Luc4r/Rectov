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
    self.isTutorialRunning = False

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
        elif event.key == pygame.K_DOWN and self.activeOption < 2:
          self.activeOption += 1
        elif event.key == pygame.K_RETURN:
          # Start tutorial
          if self.activeOption == 0:
            self.isTutorialRunning = True
          # Start game
          elif self.activeOption == 1:
            self.isGameRunning = True
          # Quit
          elif self.activeOption == 2:
            pygame.quit()
            sys.exit()

  def drawBackground(self):
    self.screen.fill(self.colors["background"])

  def drawLogo(self):
    drawTextCentered(self.screen, text="Rectov", y=120, fontSize=128)

  def drawAuthor(self):
    drawText(self.screen, text="KAROL KAPLANEK", x=960, y=690)

  def drawHighestScore(self):
    drawTextCentered(self.screen, text="Highest score:", y=600)
    drawTextCentered(self.screen, text="{:06d} - {}".format(self.scores[0]["score"], self.scores[0]["name"]) if self.scores else "{:06d}".format(0), y=630) 

  def drawOptionDots(self, activeColor, inactiveColor):
    firstDot = pygame.Rect(470, 383, 20, 20)
    secondDot = pygame.Rect(520, 423, 20, 20)
    thirdDot = pygame.Rect(530, 463, 20, 20)

    pygame.draw.rect(self.screen, activeColor if self.activeOption == 0 else inactiveColor, firstDot)
    pygame.draw.rect(self.screen, activeColor if self.activeOption == 1 else inactiveColor, secondDot)
    pygame.draw.rect(self.screen, activeColor if self.activeOption == 2 else inactiveColor, thirdDot)

  def drawOptions(self):
    inactiveColor = self.colors["grey"]
    activeColor = self.colors["white"]
    self.drawOptionDots(activeColor, inactiveColor)

    drawTextCentered(self.screen, text="TUTORIAL", y=380, color=activeColor if self.activeOption == 0 else inactiveColor, fontSize=36)
    drawTextCentered(self.screen, text="PLAY", y=420, color=activeColor if self.activeOption == 1 else inactiveColor, fontSize=36) 
    drawTextCentered(self.screen, text="EXIT", y=460, color=activeColor if self.activeOption == 2 else inactiveColor, fontSize=36) 

  def draw(self):
    self.checkInput()
    self.drawBackground()
    self.drawLogo()
    self.drawAuthor()
    self.drawHighestScore()
    self.drawOptions()