import time
import pygame

from src.components.LoadingScreen import LoadingScreen
from src.components.EndGameScreen import EndGameScreen
from src.components.PauseScreen import PauseScreen
from src.components.Level import Level
from src.components.Player import Player
from src.components.Camera import Camera
from src.components.SpriteSheet import SpriteSheet

from src.utils.drawText import drawText, drawTextCentered
from src.utils.sleepWithDrawing import sleepWithDrawing
from src.utils.getDataFromJSON import getDataFromJSON

levels_data = getDataFromJSON("src/levels/levels-data.json")

clock = pygame.time.Clock()

class Tutorial:
  def __init__(self, screen, transition, colors, quit_tutorial):
    # Passed attributes
    self.screen = screen
    self.transition = transition
    self.colors = colors
    self.quit_tutorial = quit_tutorial
    # Class attributes
    self.level = levels_data["tutorial"][0] # starting level -> index 0
    self.keys_sprite_sheet = SpriteSheet(self.screen, self.colors, "keys.png")
    self.game_info = {
      "pause": False,
      "reachedEnd": False,
      "objectivesComplete": False
    }
    self.player_info = {
      "spawn": self.level["playerSpawnPoint"],
      "alive": True,
      "score": 0
    } 
    self.keys_pressed = {
      "1": False,
      "2": False,
      "3": False,
      "jump": False,
      "left": False,
      "right": False,
      "pause": False
    }

  def resetClassAttributes(self):
    self.game_info.update({
      "pause": False,
      "reachedEnd": False,
      "objectivesComplete": False
    })
    self.player_info.update({
      "alive": True,
      "score": 0
    }) 
    self.keys_pressed.update({
      "1": False,
      "2": False,
      "3": False,
      "jump": False,
      "left": False,
      "right": False,
      "pause": False
    })

  def checkSpecialEvents(self):
    events = pygame.event.get()
    for event in events:
      if event.type == pygame.QUIT:
        self.transition.fadeOut()
        self.quit_tutorial()
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_1:
          self.keys_pressed.update({ "1": True })
        if event.key == pygame.K_2:
          self.keys_pressed.update({ "2": True })
        if event.key == pygame.K_3:
          self.keys_pressed.update({ "3": True })
        if (event.key == pygame.K_w 
            or event.key == pygame.K_UP 
            or event.key == pygame.K_SPACE
        ):
          self.keys_pressed.update({ "jump": True })
        if event.key == pygame.K_a or event.key == pygame.K_LEFT:
          self.keys_pressed.update({ "left": True })
        if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
          self.keys_pressed.update({ "right": True })
        if event.key == pygame.K_p or event.key == pygame.K_ESCAPE:
          self.keys_pressed.update({ "pause": True })
          self.game_info.update({ "pause": True })

  def checkFinishConditions(self):
    if self.level["id"] == 0:
      if (self.keys_pressed["left"] 
          and self.keys_pressed["right"] 
          and self.keys_pressed["jump"] 
          and self.keys_pressed["pause"]
      ):
        self.game_info.update({ "objectivesComplete": True })
    elif self.level["id"] == 2:
      if self.player_info["score"] > 0: # score greater than 0 means player picked up a coin
        self.game_info.update({ "objectivesComplete": True })

  def writeMessage(self, camera): 
    """ TODO: try to make this piece of code look better """
    # Messages for first tutorial
    if self.level["id"] == 0:
      drawText(self.screen, text="Move:", x=140, y=100, font_size=64)
      self.keys_sprite_sheet.drawTexture(
        texture_name="a-activated" if self.keys_pressed["left"] else "a", 
        x=140, 
        y=180, 
        camera=camera
      )
      self.keys_sprite_sheet.drawTexture(
        texture_name="d-activated" if self.keys_pressed["right"] else "d", 
        x=224, 
        y=180, 
        camera=camera
      )
      drawText(self.screen, text="alternative", x=120, y=250, font_size=36)
      self.keys_sprite_sheet.drawTexture(
        texture_name="left-activated" if self.keys_pressed["left"] else "left", 
        x=140, 
        y=290, 
        camera=camera
      )
      self.keys_sprite_sheet.drawTexture(
        texture_name="right-activated" if self.keys_pressed["right"] else "right", 
        x=224, 
        y=290, 
        camera=camera
      )

      drawText(self.screen, text="Jump:", x=540, y=100, font_size=64)
      self.keys_sprite_sheet.drawTexture(
        texture_name="space1-activated" if self.keys_pressed["jump"] else "space1", 
        x=500, 
        y=180, 
        camera=camera
      )
      self.keys_sprite_sheet.drawTexture(
        texture_name="space2-activated" if self.keys_pressed["jump"] else "space2", 
        x=584, 
        y=180, 
        camera=camera
      )
      self.keys_sprite_sheet.drawTexture(
        texture_name="space3-activated" if self.keys_pressed["jump"] else "space3", 
        x=668, 
        y=180, 
        camera=camera
      )
      drawText(self.screen, text="alternative", x=520, y=250, font_size=36)
      self.keys_sprite_sheet.drawTexture(
        texture_name="w-activated" if self.keys_pressed["jump"] else "w", 
        x=540, 
        y=290, 
        camera=camera
      )
      self.keys_sprite_sheet.drawTexture(
        texture_name="up-activated" if self.keys_pressed["jump"] else "up", 
        x=624, 
        y=290, 
        camera=camera
      )

      drawText(self.screen, text="Pause:", x=950, y=100, font_size=64)
      self.keys_sprite_sheet.drawTexture(
        texture_name="esc-activated" if self.keys_pressed["pause"] else "esc", 
        x=1000, 
        y=180, 
        camera=camera
      )
      drawText(self.screen, text="alternative", x=940, y=250, font_size=36)
      self.keys_sprite_sheet.drawTexture(
        texture_name="p-activated" if self.keys_pressed["pause"] else "p", 
        x=1000, 
        y=290, 
        camera=camera
      )
    # Messages for second tutorial
    elif self.level["id"] == 1:
      drawText(self.screen, text="Color change:", x=160, y=100, font_size=64)
      self.keys_sprite_sheet.drawTexture(
        texture_name="1-activated" if self.keys_pressed["1"] else "1", 
        x=250, 
        y=180, 
        camera=camera
      )
      self.keys_sprite_sheet.drawTexture(
        texture_name="2-activated" if self.keys_pressed["2"] else "2", 
        x=334, 
        y=180, 
        camera=camera
      )
      self.keys_sprite_sheet.drawTexture(
        texture_name="3-activated" if self.keys_pressed["3"] else "3", 
        x=418, 
        y=180, 
        camera=camera
      )
      drawText(self.screen, text="Finish -", x=1090, y=550, font_size=36)
    # Messages for third tutorial
    elif self.level["id"] == 2:
      drawTextCentered(self.screen, text="Reach the coin!", y=100, font_size=64)

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

  def finishScreen(self):
    self.transition.fadeIn(background_function=self.drawFinishScreen)
    # Display finish screen for two seconds
    sleepWithDrawing(sleep_time=1, drawing_function=self.drawFinishScreen)
    self.transition.fadeOut(background_function=self.drawFinishScreen)
    self.quit_tutorial()

  def drawFinishScreen(self):
    self.screen.fill(self.colors["background"])
    drawTextCentered(
      self.screen, 
      text="You finished the tutorial!", 
      y=200, 
      font_size=64
    )
    drawTextCentered(self.screen, text="Have fun!", y=350, font_size=36)

  def start(self):
    solid_tiles = []
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
      self.quit_tutorial
    )
    player = Player(
      self.screen, 
      self.colors, 
      solid_tiles, 
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
      solid_tiles, 
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

    while (self.player_info["alive"] 
          and not self.game_info["objectivesComplete"] 
          and not player.finish_animation_ended
    ):
      # Max fps
      clock.tick(60)
      # Check if any special keys are pressed
      self.checkSpecialEvents()
      # Check if user fulfilled finish conditions
      self.checkFinishConditions()
      # Check if game is paused
      while self.game_info["pause"]:
        # Max fps
        clock.tick(60)
        # Draw pause screen elements
        self.screen.fill(self.colors["background"])
        self.writeMessage(camera)
        level.draw()
        player.draw(camera)
        pause_screen.draw()
        # Update screen
        pygame.display.update()
      # Update moveable objects
      level.update()
      player.update()
      # Draw game elements
      self.screen.fill(self.colors["background"])
      self.writeMessage(camera)
      level.draw()
      player.draw(camera)
      # Update screen
      pygame.display.update()

    self.transition.fadeOut()
    # Player has finished (is alive) - go to next level or display finish screen
    if self.player_info["alive"]:
      next_level_id = self.level["id"] + 1
      # Check if there is another level
      if len(levels_data["tutorial"]) > next_level_id:
        self.level = levels_data["tutorial"][next_level_id]
        self.resetClassAttributes()
        self.start()
      # That was the last level
      else:
        self.finishScreen()
    # Player died - restart level
    else:  
      self.resetClassAttributes()
      self.start()