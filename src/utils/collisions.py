import pygame

def correctRectPositionOnCollision(rect, collisionRect, moveDirection):
  newRect = rect.copy()
  if moveDirection == "up":     # Hit the right side of the object
    newRect.top = collisionRect.bottom
  if moveDirection == "right":  # Hit the right side of the object
    newRect.right = collisionRect.left
  if moveDirection == "down":   # Hit the right side of the object
    newRect.bottom = collisionRect.top
  if moveDirection == "left":   # Hit the right side of the object
    newRect.left = collisionRect.right
  return newRect

def getNewRectPropertiesOnCollision(rect, objects, moveDirection):
  for obj in objects:
    if rect.colliderect(obj.rect):
      newRect = correctRectPositionOnCollision(rect, obj.rect, moveDirection)
      return newRect
  return None

def isRectCollisionDetected(rect, objects):
  for obj in objects:
    if rect.colliderect(obj.rect):
      return True
  return False

def isRectCircleCollisionDetected(rect, center, r):
  circleDistanceX = abs(center[0] - rect.centerx)
  circleDistanceY = abs(center[1] - rect.centery)

  if (circleDistanceX > rect.w / 2.0 + r) or (circleDistanceY > rect.h / 2.0 + r):
    return False
  if (circleDistanceX <= rect.w / 2.0) or (circleDistanceY <= rect.h / 2.0):
    return True

  cornerX = circleDistanceX - rect.w / 2.0
  cornerY = circleDistanceY - rect.h / 2.0
  cornerDistanceSquare = cornerX ** 2.0 + cornerY ** 2.0
  return (cornerDistanceSquare <= r ** 2.0)