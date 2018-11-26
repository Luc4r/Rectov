import sys
import pygame

class Menu:
  def __init__(self, screen):
    self.screen = screen
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
    print("Rectov")
    # displayText "Rectov"

  def drawMenuDots(self):
    firstDot = pygame.Rect(270, 380, 20, 20)
    secondDot = pygame.Rect(270, 420, 20, 20)
    if self.activeOption == 0:
      pygame.draw.rect(self.screen, (255, 255, 255), firstDot)
      pygame.draw.rect(self.screen, (80, 80, 80), secondDot)
    elif self.activeOption == 1:
      pygame.draw.rect(self.screen, (80, 80, 80), firstDot)
      pygame.draw.rect(self.screen, (255, 255, 255), secondDot)

  def drawMenu(self):
    self.drawMenuDots()
    # displayText "KAROL KAPLANEK"

    if self.activeOption == 0:
      print("START active")
      # displayText "START THE GAME" (ACTIVE - white color)
      # displayText "EXIT" (grey color)
    elif self.activeOption == 1:
      print("EXIT active")
      # displayText "START THE GAME" (grey color)
      # displayText "EXIT" (ACTIVE - white color)

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