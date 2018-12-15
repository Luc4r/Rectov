import pygame

class TransitionSurface:
  def __init__(self, screen, fillColor):
    self.screen = screen
    self.transitionScreen = pygame.Surface((1280, 720))
    self.transitionScreen.fill(fillColor)

  def fadeIn(self, backgroundFunction):
    alpha = 255
    self.transitionScreen.set_alpha(alpha)
    while alpha > 0:
      # Draw background
      backgroundFunction()
      # Change alpha of the transition surface
      alpha -= 2
      self.transitionScreen.set_alpha(alpha)
      # Draw updated transition surface on screen
      self.screen.blit(self.transitionScreen, (0, 0))
      pygame.display.update()

  def fadeOut(self, backgroundFunction):
    alpha = 0
    self.transitionScreen.set_alpha(alpha)
    while alpha < 255:
      # Draw background
      backgroundFunction()
      # Change alpha of the transition surface
      alpha += 2
      self.transitionScreen.set_alpha(alpha)
      # Draw updated transition surface on screen
      self.screen.blit(self.transitionScreen, (0, 0))
      pygame.display.update()