import time
import pygame

from src.components.LoadingScreen import LoadingScreen
from src.components.EndGameScreen import EndGameScreen
from src.components.PauseScreen import PauseScreen
from src.components.UserInterface import UserInterface
from src.components.Level import Level
from src.components.Player import Player

from src.utils.getDataFromJSON import getDataFromJSON

levelsData = getDataFromJSON("src/levels/levels-data.json")

clock = pygame.time.Clock()

class Game:
  def __init__(self, screen, transition, colors, quitGame):
    # Passed attributes
    self.screen = screen
    self.transition = transition
    self.colors = colors
    self.quitGame = quitGame
    # Class attributes
    self.gameInformation = {
      "pause": False
    }
    self.playerInformation = {
      "alive": True,
      "score": 0
    }
    self.level = levelsData["game"][0]

  def checkSpecialEvents(self):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        self.transition.fadeOut()
        self.quitGame()
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_p or event.key == pygame.K_ESCAPE:
          self.gameInformation.update({ "pause": True })

  def loadingScreen(self, level):
    loadingScreen = LoadingScreen(self.screen, self.colors, self.level["name"], self.playerInformation["score"])

    self.transition.fadeIn(backgroundFunction=loadingScreen.draw)
    # Do a one second break before transition
    timeEnd = time.time() + 1
    while time.time() < timeEnd:
      # Max fps
      clock.tick(60)
      # Skip animation when any key is pressed or quit button pressed
      events = pygame.event.get()
      for event in events:
        if event.type == pygame.KEYDOWN or event.type == pygame.QUIT:
          return
      # Draw loading screen (coin animation)
      loadingScreen.draw()
      # Update screen
      pygame.display.update()
    self.transition.fadeOut(backgroundFunction=loadingScreen.draw)

  def deathScreen(self):
    endGameScreen = EndGameScreen(self.screen, self.colors, self.playerInformation, self.transition.fadeOut, self.quitGame, "RECTED")
    self.transition.fadeIn(backgroundFunction=endGameScreen.draw)
    while True: 
      # Max fps
      clock.tick(60)
      # Draw end game screen
      endGameScreen.draw()
      # Update screen
      pygame.display.update()

  def finishScreen(self):
    endGameScreen = EndGameScreen(self.screen, self.colors, self.playerInformation, self.transition.fadeOut, self.quitGame, "Finish!")
    self.transition.fadeIn(backgroundFunction=endGameScreen.draw)
    while True: 
      # Max fps
      clock.tick(60)
      # Draw end game screen
      endGameScreen.draw()
      # Update screen
      pygame.display.update()

  def start(self):
    solidTiles = []
    walls = []
    platforms = []
    coins = []
    enemies = []
    finish = []

    pauseScreen = PauseScreen(self.screen, self.colors, self.gameInformation, self.transition.fadeOut, self.quitGame)
    ui = UserInterface(self.screen, self.colors, self.level["name"], self.playerInformation)
    player = Player(self.screen, self.colors, solidTiles, walls, platforms, coins, finish, self.playerInformation)
    level = Level(self.screen, self.colors, solidTiles, walls, platforms, coins, enemies, finish, player, self.playerInformation, self.level["dataFileName"])
    
    level.build()

    self.loadingScreen(level)

    self.transition.fadeIn(backgroundFunction=level.draw)

    while self.playerInformation["alive"] and not player.finishAnimationEnded:
      # Max fps
      clock.tick(60)
      # Check if any special keys are pressed
      self.checkSpecialEvents()
      # Check if game is paused
      while self.gameInformation["pause"]:
        # Max fps
        clock.tick(60)
        # Draw pause screen elements
        self.screen.fill(self.colors["background"])
        level.draw()
        player.draw()
        pauseScreen.draw()
        # Update screen
        pygame.display.update()
      # Update moveable objects
      level.update()
      player.update()
      # Draw game elements
      self.screen.fill(self.colors["background"])
      level.draw()
      player.draw()
      ui.draw()
      # Update screen
      pygame.display.update()

    self.transition.fadeOut()
    if self.playerInformation["alive"]:
      nextLevelIndex = self.level["id"] + 1
      if len(levelsData["game"]) > nextLevelIndex:
        # Load next level data
        self.level = levelsData["game"][nextLevelIndex]
        # Start new level
        self.start()
      else:
        self.finishScreen()
    else:  
      self.deathScreen()