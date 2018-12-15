import pygame

class Coin:
  def __init__(self, screen, coins, x, y):
    self.screen = screen

    self.position = ((x * 40) + 20, (y * 40) + 20)
    self.radius = 6
    self.color = [255, 0, 0]
    self.nextColor = [0, 255, 0]
    coins.append(self)

  def simpleRGBAnimation(self):
    if self.color != self.nextColor:
      positionToIncrement = self.nextColor.index(255)
      positionToDecrement = positionToIncrement - 1
      if positionToDecrement == -1:
        positionToDecrement = 2

      self.color[positionToDecrement] -= 5
      self.color[positionToIncrement] += 5
    else:
      positionOfMaxValue = self.color.index(255)
      positionOfNextMaxValue = positionOfMaxValue + 1
      if positionOfNextMaxValue == 3:
        positionOfNextMaxValue = 0

      self.nextColor[positionOfNextMaxValue] = 255
      self.nextColor[positionOfMaxValue] = 0

  def drawCoin(self):
    pygame.draw.circle(self.screen, self.color, self.position, self.radius)
    self.simpleRGBAnimation()