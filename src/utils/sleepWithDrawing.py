import time
import pygame

clock = pygame.time.Clock()

def sleepWithDrawing(sleepTime, drawingFunction = None):
  timeEnd = time.time() + sleepTime
  while time.time() < timeEnd:
    # Max fps
    clock.tick(60)
    # Skip animation when any key is pressed or quit button pressed
    events = pygame.event.get()
    for event in events:
      if event.type == pygame.KEYDOWN or event.type == pygame.QUIT:
        return
    # Drawing function
    drawingFunction()
    # Update screen
    pygame.display.update()