import pygame

from src.components.Menu import Menu
from src.components.TransitionSurface import TransitionSurface
from src.components.LoadingScreen import LoadingScreen
from src.components.UserInterface import UserInterface
from src.components.Player import Player
from src.components.Level import Level

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
  platforms = []
  coins = []
  playerScore = [0] # Mutable object (list) - used for easy update every object using it
  level = Level(screen, walls, platforms, coins, colors, levelName="lvl-1")
  player = Player(screen, walls, platforms, coins, colors, playerScore)
  loadingScreen = LoadingScreen(screen, colors, "1 - Test Area", playerScore)
  ui = UserInterface(screen, colors, "1 - Test Area", playerScore)

  level.buildWalls()
  level.buildPlatforms()
  level.buildCoins()

  transition.fadeIn(backgroundFunction=loadingScreen.drawLoadingScreen)
  pygame.time.wait(1000)
  transition.fadeOut(backgroundFunction=loadingScreen.drawLoadingScreen)
  transition.fadeIn(backgroundFunction=level.drawLevel)

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
    # Draw game elements
    screen.fill(colors["background"])
    level.drawLevel()
    player.displayPlayer()
    ui.drawUI()
    # Update screen
    pygame.display.update()

if __name__ == '__main__':
  main()