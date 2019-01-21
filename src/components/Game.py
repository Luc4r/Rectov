import time
import pygame

from src.components.LoadingScreen import LoadingScreen
from src.components.EndGameScreen import EndGameScreen
from src.components.PauseScreen import PauseScreen
from src.components.UserInterface import UserInterface
from src.components.Level import Level
from src.components.Player import Player
from src.components.Camera import Camera

from src.utils.getDataFromJSON import getDataFromJSON
from src.utils.sleepWithDrawing import sleepWithDrawing

levels_data = getDataFromJSON("src/levels/levels-data.json")
clock = pygame.time.Clock()

class Game:
  def __init__(self, screen, transition, colors, quit_game):
    # Passed attributes
    self.screen = screen
    self.transition = transition
    self.colors = colors
    self.quit_game = quit_game
    # Class attributes
    self.level = levels_data["game"][0] # starting level -> index 0
    self.game_info = {
      "pause": False
    }
    self.player_info = {
      "spawn": self.level["playerSpawnPoint"],
      "alive": True,
      "score": 0
    }

  def checkSpecialEvents(self):
    events = pygame.event.get()
    for event in events:
      if event.type == pygame.QUIT:
        self.transition.fadeOut()
        self.quit_game()
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_p or event.key == pygame.K_ESCAPE:
          self.game_info.update({ "pause": True })

  def loadingLevelScreen(self, level):
    loading_screen = LoadingScreen(
      self.screen, 
      self.colors, 
      self.level["name"], 
      self.player_info["score"]
    )
    self.transition.fadeIn(background_function=loading_screen.draw)
    # Do a one second break before transition
    sleepWithDrawing(sleep_time=1, drawing_function=loading_screen.draw)
    self.transition.fadeOut(background_function=loading_screen.draw)

  def endGameScreen(self, end_message):
    end_game_screen = EndGameScreen(
      self.screen, 
      self.colors, 
      self.player_info, 
      self.transition.fadeOut, 
      self.quit_game, 
      end_message
    )
    self.transition.fadeIn(background_function=end_game_screen.draw)
    while True: 
      # Max fps
      clock.tick(60)
      # Draw end game screen
      end_game_screen.draw()
      # Update screen
      pygame.display.update()

  def start(self):
    solidTiles = []
    walls = []
    platforms = []
    coins = []
    enemies = []
    finish = []

    level_end = [self.level["length"][0] * 40, self.level["length"][1] * 40]

    pause_screen = PauseScreen(
      self.screen, 
      self.colors, 
      self.game_info, 
      self.transition.fadeOut, 
      self.quit_game
    )
    ui = UserInterface(
      self.screen, 
      self.colors, 
      self.level["name"], 
      self.player_info
    )
    player = Player(
      self.screen, 
      self.colors, 
      solidTiles, 
      walls, 
      platforms, 
      coins, 
      finish, 
      self.player_info, 
      level_end
    )
    camera = Camera(player, level_end)
    level = Level(
      self.screen, 
      self.colors, 
      camera,
      solidTiles, 
      walls, 
      platforms, 
      coins, 
      enemies, 
      finish, 
      player, 
      self.player_info, 
      self.level["dataFileName"]
    )

    level.build()
    self.loadingLevelScreen(level)
    self.transition.fadeIn(background_function=level.draw)

    while self.player_info["alive"] and not player.finish_animation_ended:
      # Max fps
      clock.tick(60)
      # Check if any special keys are pressed
      self.checkSpecialEvents()
      # Check if game is paused
      while self.game_info["pause"]:
        # Max fps
        clock.tick(60)
        # Draw pause screen elements
        self.screen.fill(self.colors["background"])
        level.draw()
        player.draw(camera)
        pause_screen.draw()
        # Update screen
        pygame.display.update()
      # Update moveable objects
      level.update()
      player.update()
      camera.update()
      # Draw game elements
      self.screen.fill(self.colors["background"])
      level.draw()
      player.draw(camera)
      ui.draw()
      # Update screen
      pygame.display.update()

    self.transition.fadeOut()
    # Player has finished (is alive) - go to next level or display end game screen
    if self.player_info["alive"]:
      next_level_id = self.level["id"] + 1
      # Check if there is another level
      if len(levels_data["game"]) > next_level_id:
        # Load next level data
        self.level = levels_data["game"][next_level_id]
        # Start new level
        self.start()
      # That was the last level
      else:
        self.endGameScreen("Finish!")
    # Player died - death screen
    else:  
      self.endGameScreen("RECTED")