import pygame

from src.components.Menu import Menu

def main():
  pygame.init()
  pygame.display.set_caption("Rectov")
  screen = pygame.display.set_mode((1280, 720))

  menu = Menu(screen)

  for i in range(10):
    menu.drawRect(50 * i, 100)
    print(i)
    pygame.time.delay(300)

if __name__ == '__main__':
  main()