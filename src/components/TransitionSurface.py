import pygame

clock = pygame.time.Clock()

class TransitionSurface:
  def __init__(self, screen, colors):
    # Passed attributes
    self.screen = screen
    self.colors = colors
    # Class attributes
    self.transition_screen = pygame.Surface((1280, 720))
    # Fill transition screen
    self.transition_screen.fill(self.colors["background"])

  def fadeIn(self, background_function = None):
    alpha = 255
    self.transition_screen.set_alpha(alpha)
    while alpha > 0:
      # Max fps
      clock.tick(60)
      # Skip animation when any key is pressed or quit button pressed
      events = pygame.event.get()
      for event in events:
        if event.type == pygame.KEYDOWN or event.type == pygame.QUIT:
          return
      # Draw background
      if background_function is not None:
        background_function()
      # Change alpha of the transition surface
      alpha -= 4
      self.transition_screen.set_alpha(alpha)
      # Draw updated transition surface on screen
      self.screen.blit(self.transition_screen, (0, 0))
      pygame.display.update()

  def fadeOut(self, background_function = None):
    alpha = 0
    self.transition_screen.set_alpha(alpha)
    while alpha < (255 if background_function is not None else 80):
      # Max fps
      clock.tick(60)
      # Skip animation when any key is pressed or quit button pressed
      events = pygame.event.get()
      for event in events:
        if event.type == pygame.KEYDOWN or event.type == pygame.QUIT:
          return
      # Draw background
      if background_function is not None:
        background_function()
      # Change alpha of the transition surface
      alpha += (4 if background_function is not None else 1)
      self.transition_screen.set_alpha(alpha)
      # Draw updated transition surface on screen
      self.screen.blit(self.transition_screen, (0, 0))
      pygame.display.update()