import pygame

def correctRectPosition(rect, collision_rect, move_direction):
  new_rect = rect.copy()
  if move_direction == "up":     # Hit the right side of the object
    new_rect.top = collision_rect.bottom
  if move_direction == "right":  # Hit the right side of the object
    new_rect.right = collision_rect.left
  if move_direction == "down":   # Hit the right side of the object
    new_rect.bottom = collision_rect.top
  if move_direction == "left":   # Hit the right side of the object
    new_rect.left = collision_rect.right
  return new_rect

def getNewRectProperties(rect, objects, move_direction):
  for obj in objects:
    if rect.colliderect(obj["rect"]):
      return correctRectPosition(rect, obj["rect"], move_direction)
  return None

def isRectCollisionDetected(rect, objects):
  for obj in objects:
    if rect.colliderect(obj["rect"]):
      return True
  return False

def isRectCircleCollisionDetected(rect, center, r):
  circle_distance_x = abs(center[0] - rect.centerx)
  circle_distance_y = abs(center[1] - rect.centery)
  if (circle_distance_x > rect.w / 2.0 + r) or (circle_distance_y > rect.h / 2.0 + r):
    return False
  if (circle_distance_x <= rect.w / 2.0) or (circle_distance_y <= rect.h / 2.0):
    return True

  corner_x = circle_distance_x - rect.w / 2.0
  corner_y = circle_distance_y - rect.h / 2.0
  corner_distance_square = corner_x ** 2.0 + corner_y ** 2.0
  return (corner_distance_square <= r ** 2.0)