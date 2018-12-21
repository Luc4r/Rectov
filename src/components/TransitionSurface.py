import pygame

class TransitionSurface:
  def __init__(self, screen, clock, fillColor):
    self.screen = screen
    self.clock = clock
    self.transitionScreen = pygame.Surface((1280, 720))
    self.transitionScreen.fill(fillColor)

  def fadeIn(self, backgroundFunction = None):
    alpha = 255
    self.transitionScreen.set_alpha(alpha)
    while alpha > 0:
      # Max fps
      self.clock.tick(60)
      # Skip animation when any key is pressed or quit button pressed
      events = pygame.event.get()
      for event in events:
        if event.type == pygame.KEYDOWN or event.type == pygame.QUIT:
          return
      # Draw background
      if backgroundFunction is not None:
        backgroundFunction()
      # Change alpha of the transition surface
      alpha -= 4
      self.transitionScreen.set_alpha(alpha)
      # Draw updated transition surface on screen
      self.screen.blit(self.transitionScreen, (0, 0))
      pygame.display.update()

  def fadeOut(self, backgroundFunction = None):
    alpha = 0
    self.transitionScreen.set_alpha(alpha)
    while alpha < (255 if backgroundFunction is not None else 80):
      # Max fps
      self.clock.tick(60)
      # Skip animation when any key is pressed or quit button pressed
      events = pygame.event.get()
      for event in events:
        if event.type == pygame.KEYDOWN or event.type == pygame.QUIT:
          return
      # Draw background
      if backgroundFunction is not None:
        backgroundFunction()
      # Change alpha of the transition surface
      alpha += (4 if backgroundFunction is not None else 1)
      self.transitionScreen.set_alpha(alpha)
      # Draw updated transition surface on screen
      self.screen.blit(self.transitionScreen, (0, 0))
      pygame.display.update()