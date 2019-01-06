import os
import pygame

def displayImage(screen, image, x=0, y=0, width=None, height=None):
  img = pygame.image.load(os.path.join("img", image))
  if width is not None and height is not None:
    img = pygame.transform.scale(img, (width, height))
  screen.blit(img, (x, y))
