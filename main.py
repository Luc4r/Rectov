import time
import pygame

from src.components.Menu import Menu
from src.components.TransitionSurface import TransitionSurface
from src.components.LoadingScreen import LoadingScreen
from src.components.UserInterface import UserInterface
from src.components.Player import Player
from src.components.Enemy import Enemy
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

  transition.fadeIn(backgroundFunction=menu.drawMenu)

  while not menu.isGameRunning:
    menu.drawMenu()

  transition.fadeOut(backgroundFunction=menu.drawMenu)

  walls = []
  platforms = []
  coins = []
  playerScore = [0] # Mutable object (list) - used for easy update every object using it
  level = Level(screen, walls, platforms, coins, colors, levelName="lvl-1")
  player = Player(screen, walls, platforms, coins, colors, playerScore, main)
  enemy = Enemy(screen, walls, platforms, player, colors, playerScore)
  loadingScreen = LoadingScreen(screen, colors, "1 - Test Area", playerScore)
  ui = UserInterface(screen, colors, "1 - Test Area", playerScore)

  level.buildLevel()

  transition.fadeIn(backgroundFunction=loadingScreen.drawLoadingScreen)
  # Do a one second break before transition
  timeEnd = time.time() + 1
  while time.time() < timeEnd:
    # Max fps
    clock.tick(60)
    # Draw loading screen (coin animation)
    loadingScreen.drawLoadingScreen()
    pygame.display.update()
  transition.fadeOut(backgroundFunction=loadingScreen.drawLoadingScreen)
  transition.fadeIn(backgroundFunction=level.drawLevel)

  clock = pygame.time.Clock()
  running = True
  while running:
    # Max fps
    clock.tick(60)
    # Update player
    player.update()
    # Draw game elements
    screen.fill(colors["background"])
    enemy.update()
    level.drawLevel()
    player.drawPlayer()
    ui.drawUI()
    # Update screen
    pygame.display.update()

if __name__ == '__main__':
  main()