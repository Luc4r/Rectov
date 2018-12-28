import time
import pygame

from src.components.Menu import Menu
from src.components.TransitionSurface import TransitionSurface
from src.components.LoadingScreen import LoadingScreen
from src.components.DeathScreen import DeathScreen
from src.components.PauseScreen import PauseScreen
from src.components.UserInterface import UserInterface
from src.components.Player import Player
from src.components.Enemy import Enemy
from src.components.Level import Level

from src.utils.getDataFromJSON import getDataFromJSON

colors = getDataFromJSON("src/config/colors.json")
clock = pygame.time.Clock()

def main():
  pygame.init()
  pygame.display.set_caption("Rectov")
  screen = pygame.display.set_mode((1280, 720))
  screen.fill(colors["background"])

  transition = TransitionSurface(screen, clock, colors["background"])
  menu = Menu(screen, colors)

  transition.fadeIn(backgroundFunction=menu.drawMenu)

  while not menu.isGameRunning:
    menu.drawMenu()
    # Update screen
    pygame.display.update()

  transition.fadeOut(backgroundFunction=menu.drawMenu)

  walls = []
  platforms = []
  coins = []
  finish = []
  isGameRunning = [True]
  isGamePaused = [False]
  playerScore = [0]

  level = Level(screen, walls, platforms, coins, finish, colors, levelName="lvl-1")
  player = Player(screen, walls, platforms, coins, finish, colors, playerScore)
  enemy = Enemy(screen, walls, platforms, player, colors, isGameRunning)
  loadingScreen = LoadingScreen(screen, colors, "1 - Test Area", playerScore)
  deathScreen = DeathScreen(screen, colors, playerScore, confirmTransition=transition.fadeOut, backToMainMenu=main)
  pauseScreen = PauseScreen(screen, colors, isGamePaused, confirmTransition=transition.fadeOut, backToMainMenu=main)
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
    # Update screen
    pygame.display.update()
  transition.fadeOut(backgroundFunction=loadingScreen.drawLoadingScreen)
  transition.fadeIn(backgroundFunction=level.drawLevel)

  while isGameRunning[0] and not player.finishAnimationEnded:
    # Max fps
    clock.tick(60)
    # Check special events
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        transition.fadeOut()
        main()
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_p or event.key == pygame.K_ESCAPE:
          isGamePaused[0] = True
          while isGamePaused[0]:
            # Max fps
            clock.tick(60)
            # Draw pause screen elements
            screen.fill(colors["background"])
            enemy.drawEnemy()
            level.drawLevel()
            player.drawPlayer()
            pauseScreen.drawPauseScreen()
            # Update screen
            pygame.display.update()
    # Update moveable objects
    player.update()
    enemy.update()
    # Draw game elements
    screen.fill(colors["background"])
    enemy.drawEnemy()
    level.drawLevel()
    player.drawPlayer()
    ui.drawUI()
    # Update screen
    pygame.display.update()

  transition.fadeOut()
  transition.fadeIn(backgroundFunction=deathScreen.drawDeathScreen)

  while True: # only way to get there is to die or finish the game - otherwise it just gets back to main
    # Max fps
    clock.tick(60)
    # Draw end game screen
    deathScreen.drawDeathScreen()
    # Update screen
    pygame.display.update()

if __name__ == '__main__':
  main()