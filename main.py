import pygame

from src.components.Menu import Menu

def main():
  pygame.init()
  pygame.display.set_caption("Rectov")
  screen = pygame.display.set_mode((1280, 720))

  menu = Menu(screen)

  while not menu.isGameRunning:
    menu.update()

if __name__ == '__main__':
  main()