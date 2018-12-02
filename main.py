import pygame

from src.components.Menu import Menu
from src.components.Wall import Wall
from src.components.Player import Player

from src.utils.getDataFromJSON import getDataFromJSON

colors = getDataFromJSON("src/config/colors.json")

def main():
  pygame.init()
  pygame.display.set_caption("Rectov")
  screen = pygame.display.set_mode((1280, 720))

  menu = Menu(screen, colors)

  while not menu.isGameRunning:
    menu.update()

  walls = []
  for x in range(32):
    Wall(screen, colors, walls, x, y=17)

  player = Player(screen, colors)

  clock = pygame.time.Clock()
  running = True
  while running:
  	# Max fps
    clock.tick(60)
    # Special keys events
    events = pygame.event.get()
    for event in events:
      if event.type == pygame.QUIT:
        running = False
      if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
        running = False
    # Update player if key pressed
    player.update()
    # Draw background
    screen.fill((22, 22, 22))
    # Draw player
    player.displayPlayer()
    # Draw walls
    for wall in walls:
      wall.displayWall()
    # Update screen
    pygame.display.update()

if __name__ == '__main__':
  main()