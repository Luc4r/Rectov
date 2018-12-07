import pygame

def fadeIn(screen, transitionScreen, backgroundFunction):
  alpha = 255
  transitionScreen.set_alpha(alpha)
  while alpha > 0:
    # Display background
    backgroundFunction()
    # Change alpha of the transition surface
    alpha -= 2
    transitionScreen.set_alpha(alpha)
    # Draw updated transition surface on screen
    screen.blit(transitionScreen, (0, 0))
    pygame.display.update()

def fadeOut(screen, transitionScreen, backgroundFunction):
  alpha = 0
  transitionScreen.set_alpha(alpha)
  while alpha < 255:
    # Display background
    backgroundFunction()
    # Change alpha of the transition surface
    alpha += 2
    transitionScreen.set_alpha(alpha)
    # Draw updated transition surface on screen
    screen.blit(transitionScreen, (0, 0))
    pygame.display.update()