import pygame

from src.components.Menu import Menu
from src.components.TransitionSurface import TransitionSurface
from src.components.LoadingScreen import LoadingScreen
from src.components.Wall import Wall
from src.components.Player import Player

from src.utils.getDataFromJSON import getDataFromJSON

colors = getDataFromJSON("src/config/colors.json")

def main():
  pygame.init()
  pygame.display.set_caption("Rectov")
  screen = pygame.display.set_mode((1280, 720))
  screen.fill(colors["background"])

  transition = TransitionSurface(screen, colors["background"])
  menu = Menu(screen, colors)

  transition.fadeIn(backgroundFunction=menu.update)

  while not menu.isGameRunning:
    menu.update()

  transition.fadeOut(backgroundFunction=menu.update)

  walls = []
  for x in range(32):
    Wall(screen, colors, walls, x, y=17)
  Wall(screen, colors, walls, x=22, y=14)
  Wall(screen, colors, walls, x=23, y=13)
  Wall(screen, colors, walls, x=24, y=12)
  Wall(screen, colors, walls, x=25, y=11)
  Wall(screen, colors, walls, x=26, y=15)
  Wall(screen, colors, walls, x=27, y=16)

  player = Player(screen, walls, colors)
  loadingScreen = LoadingScreen(screen, colors, "1 - Test Area", "000000")

  transition.fadeIn(backgroundFunction=loadingScreen.drawLoadingScreen)
  pygame.time.wait(1000)
  transition.fadeOut(backgroundFunction=loadingScreen.drawLoadingScreen)

  clock = pygame.time.Clock()
  running = True
  while running:
    # Max fps
    clock.tick(60)
    # Special keys events
    events = pygame.event.get()
    for event in events:
      if event.type == pygame.QUIT:
        main()
      if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
        main()
    # Update player if key pressed
    player.update()
    # Draw background
    screen.fill(colors["background"])
    # Draw player
    player.displayPlayer()
    # Draw walls
    for wall in walls:
      wall.displayWall()

    pygame.display.update()

if __name__ == '__main__':
  main()