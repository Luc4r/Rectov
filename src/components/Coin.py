import pygame

class Coin:
  def __init__(self, screen, x, y):
    # Passed attributes
    self.screen = screen
    # Class attributes
    self.position = [(x * 40) + 20, (y * 40) + 20]
    self.radius = 6
    self.color = [255, 0, 0]
    self.next_color = [0, 255, 0]

  def simpleRGBAnimation(self):
    color_change_value = 5
    max_color_value = 255
    if self.color != self.next_color:
      index_of_increment = self.next_color.index(max_color_value)
      index_of_decrement = index_of_increment - 1 if index_of_increment != 0 else 2
      self.color[index_of_decrement] -= color_change_value
      self.color[index_of_increment] += color_change_value
    else:
      index_of_max = self.color.index(max_color_value)
      index_of_next_max = index_of_max + 1 if index_of_max < 2 else 0
      self.next_color[index_of_next_max] = max_color_value
      self.next_color[index_of_max] = 0

  def draw(self, camera=None):
    if camera is not None:
      pygame.draw.circle(
        self.screen, 
        self.color, 
        (self.position[0] - camera.screen.x, self.position[1] - camera.screen.y), 
        self.radius
      )
    else:
      pygame.draw.circle(self.screen, self.color, self.position, self.radius)

  def updateColor(self):
    self.simpleRGBAnimation()