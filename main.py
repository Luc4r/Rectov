import pygame

from src.components.Menu import Menu

from src.utils.getDataFromJSON import getDataFromJSON

colors = getDataFromJSON("src/config/colors.json")

def main():
  pygame.init()
  pygame.display.set_caption("Rectov")
  screen = pygame.display.set_mode((1280, 720))

  menu = Menu(screen, colors)

  while not menu.isGameRunning:
    menu.update()

if __name__ == '__main__':
  main()