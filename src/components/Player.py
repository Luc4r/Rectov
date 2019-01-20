import pygame

from src.utils.collisions import (correctRectPosition, 
                                  isRectCollisionDetected, 
                                  isRectCircleCollisionDetected)

class Player:
  def __init__(
    self, screen, colors, solid_tiles, walls, platforms, 
    coins, finish, player_information, level_end
  ):
    # Passed attributes
    self.screen = screen
    self.colors = colors
    self.solid_tiles = solid_tiles
    self.walls = walls
    self.platforms = platforms
    self.coins = coins
    self.finish = finish
    self.player_info = player_information
    self.level_end = level_end
    # Class attributes
    self.rect = pygame.Rect(60, 640, 30, 30)
    self.color = colors["red"]
    self.is_falling = False
    self.is_jumping = False
    self.is_holding_jump_key = False
    self.velocity = [5, 5]
    self.mass = 0.35
    self.has_finished = False
    self.finish_animation_ended = False

  def handleJump(self):
    if self.is_jumping:
      self.is_holding_jump_key = True
    elif not self.is_falling:
      self.is_jumping = True
      self.velocity[1] = 8

  def handleMoveRight(self):
    self.rect.x += self.velocity[0]
    self.checkCollision("right")

  def handleMoveLeft(self):
    self.rect.x -= self.velocity[0]
    self.checkCollision("left")

  def handleChangeColor(self, new_color):
    collision_objects = self.walls + self.platforms
    if not isRectCollisionDetected(self.rect, collision_objects):
      self.color = self.colors[new_color]

  def gravitySimulation(self):
    F = 0.1 * self.mass * (self.velocity[1] ** 2)
    # Change position and velocity
    self.rect.y += F
    self.velocity[1] += 0.5
    # On floor hit - set velocity to default value
    if self.checkCollision("down"):
      self.velocity[1] = 5
      self.is_falling = False
    else:
      self.is_falling = True

  def jumpSimulation(self):
    if self.velocity[1] > 0:
      F = (0.5 * self.mass * (self.velocity[1] ** 2))
    else:
      F = -(0.5 * self.mass * (self.velocity[1] ** 2))
    # Change position
    self.rect.y -= F
    # Change velocity (when user is holding jump button, player lose velocity slower)
    if self.is_holding_jump_key:
      self.velocity[1] -= 0.25
      self.is_holding_jump_key = False
    else:
      self.velocity[1] -= 0.45
    # If something is in a way, start falling
    if self.velocity[1] > 0 and self.checkCollision("up"):
      self.velocity[1] = 0
    # If ground is reached, reset variables
    if self.checkCollision("down"):
      self.is_jumping = False
      self.velocity[1] = 5

  def checkCollision(self, move_direction):
    for solid_tile in self.solid_tiles:
      if self.rect.colliderect(solid_tile["rect"]):
        self.rect = correctRectPosition(
          self.rect, 
          solid_tile["rect"], 
          move_direction
        )
        return True
    for wall in self.walls:
      if (self.rect.colliderect(wall["rect"]) 
          and self.color == self.colors[wall["color"]]
      ):
        self.rect = correctRectPosition(
          self.rect, 
          wall["rect"], 
          move_direction
        )
        return True
    for platform in self.platforms:
      if (self.rect.colliderect(platform["rect"]) 
          and self.color != self.colors[platform["color"]]
      ):
        self.rect = correctRectPosition(
          self.rect, 
          platform["rect"], 
          move_direction
        )
        return True
    return False

  def checkCoinPickup(self):
    for coin in self.coins:
      if isRectCircleCollisionDetected(self.rect, coin.position, coin.radius):
        index_of_picked_coin = self.coins.index(coin)
        self.coins.pop(index_of_picked_coin)
        self.player_info.update({ "score": self.player_info["score"] + 100 })

  def checkFinishCollision(self):
    if self.finish and self.rect.colliderect(self.finish[0]):
      # Start finish level animation
      self.has_finished = True
      self.rect.right = self.finish[0].rect.left

  def checkBorderCollision(self):
    border_x = [0, self.level_end[0]]
    border_y = [0, self.level_end[1]]
    if self.rect.left < border_x[0] or self.rect.right > border_x[1]:
      self.player_info.update({ "alive": False })
    if self.rect.top < border_y[0] or self.rect.bottom > border_y[1]:
      self.player_info.update({ "alive": False })

  def checkInput(self):
    key = pygame.key.get_pressed()
    if key[pygame.K_UP] or key[pygame.K_w] or key[pygame.K_SPACE]:
      self.handleJump()
    if key[pygame.K_LEFT] or key[pygame.K_a]:
      self.handleMoveLeft()
    if key[pygame.K_RIGHT] or key[pygame.K_d]:
      self.handleMoveRight()
    if key[pygame.K_1]:
      self.handleChangeColor("red")
    if key[pygame.K_2]:
      self.handleChangeColor("green")
    if key[pygame.K_3]:
      self.handleChangeColor("blue")

  def animationFinish(self):
    half_of_width_difference = round(
      (self.finish[0].rect.width - self.rect.width) / 2
    )
    finish_center_y = round(
      self.finish[0].rect.top + self.finish[0].rect.height / 2
    )
    player_center_y = round(
      self.rect.top + (self.rect.height / 2)
    )
    # Make sure that player is on the ground
    if (self.rect.bottom < self.finish[0].rect.bottom 
        and self.rect.right <= self.finish[0].rect.left
    ):
      self.gravitySimulation()
    # Horizontal animation
    elif self.rect.left - self.finish[0].rect.left < half_of_width_difference:
      self.rect.left += 2
    # Vertical animation and size change
    elif player_center_y > finish_center_y:
      self.rect.top -= 1
      if self.rect.width > 2 and self.rect.top % 5 == 0:
        self.rect.width -= 2
        self.rect.height -= 2
        self.rect.left += 1
    # Animations are done
    else:
      self.finish_animation_ended = True

  def draw(self, camera):
    rect_to_display = pygame.Rect(
      self.rect.x - camera.screen.x, 
      self.rect.y - camera.screen.y, 
      self.rect.width, 
      self.rect.height
    )
    # Draw player border
    border_color = [200 if value == 255 else 0 for value in self.color]
    pygame.draw.rect(self.screen, border_color, rect_to_display)
    # Draw player
    color_rect = pygame.Rect(
      rect_to_display.left + 2, 
      rect_to_display.top + 2, 
      rect_to_display.width - 4, 
      rect_to_display.height - 4
    )
    pygame.draw.rect(self.screen, self.color, color_rect)

  def update(self):
    if not self.has_finished:
      self.checkInput()
      if self.is_jumping:
        self.jumpSimulation()
      else:
        self.gravitySimulation()
      self.checkCoinPickup()
      self.checkBorderCollision()
      self.checkFinishCollision()
    else:
      self.animationFinish()
      