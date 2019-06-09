import time
import pygame

from src.components.Menu import Menu
from src.components.TransitionSurface import TransitionSurface
from src.components.Game import Game
from src.components.Tutorial import Tutorial

from src.utils.getDataFromJSON import getDataFromJSON

def main():
  # Get JSON data:
  colors = getDataFromJSON("src/config/colors.json")
  scores = getDataFromJSON("src/data/scores.json")
  # Init game window
  pygame.init()
  pygame.display.set_caption("Rectov")
  screen = pygame.display.set_mode((1280, 720))
  screen.fill(colors["background"])
  # Main file objects
  transition = TransitionSurface(screen, colors)
  menu = Menu(screen, colors, scores)
  game = Game(screen, transition, colors, main)
  tutorial = Tutorial(screen, transition, colors, main)
  # Transition
  transition.fadeIn(background_function=menu.draw)
  # Display menu until user selects "play game" option
  while not menu.is_game_running and not menu.is_tutorial_running:
    # Draw menu
    menu.draw()
    # Update screen
    pygame.display.update()
  # Transition
  transition.fadeOut(background_function=menu.draw)
  # Initialize game
  if menu.is_game_running:
    game.start()
  # Initialize tutorial
  elif menu.is_tutorial_running:
    tutorial.start()

if __name__ == '__main__':
  main()