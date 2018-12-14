def collideRectCircle(rect, center, r):
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