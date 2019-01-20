import time
import pygame

clock = pygame.time.Clock()

def sleepWithDrawing(sleep_time, drawing_function = None):
  time_end = time.time() + sleep_time
  while time.time() < time_end:
    # Max fps
    clock.tick(60)
    # Skip animation when any key is pressed or quit button pressed
    events = pygame.event.get()
    for event in events:
      if event.type == pygame.KEYDOWN or event.type == pygame.QUIT:
        return
    # Drawing function
    drawing_function()
    # Update screen
    pygame.display.update()