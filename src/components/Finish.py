import pygame

class Finish:
  def __init__(self, screen, colors, x, y, width, height):
  	# Passed attributes
    self.screen = screen
    self.colors = colors
    # Class attributes
    self.rect = pygame.Rect(x * 40, y * 40, width * 40, height * 40)
    
  def draw(self):
    pygame.draw.rect(self.screen, self.colors["black"], self.rect)