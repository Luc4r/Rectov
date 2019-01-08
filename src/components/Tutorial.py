import time
import pygame

from src.components.LoadingScreen import LoadingScreen
from src.components.EndGameScreen import EndGameScreen
from src.components.PauseScreen import PauseScreen
from src.components.Level import Level
from src.components.Player import Player
from src.components.SpriteSheet import SpriteSheet

from src.utils.drawText import drawText, drawTextCentered
from src.utils.sleepWithDrawing import sleepWithDrawing
from src.utils.getDataFromJSON import getDataFromJSON

levelsData = getDataFromJSON("src/levels/levels-data.json")

clock = pygame.time.Clock()

class Tutorial:
  def __init__(self, screen, transition, colors, quitTutorial):
    # Passed attributes
    self.screen = screen
    self.transition = transition
    self.colors = colors
    self.quitTutorial = quitTutorial
    # Class attributes
    self.keysSpriteSheet = SpriteSheet(self.screen, self.colors, "keys.png")
    self.gameInformation = {
      "pause": False,
      "reachedEnd": False,
      "objectivesComplete": False
    }
    self.playerInformation = {
      "alive": True,
      "score": 0
    } 
    self.keysPressed = {
      "1": False,
      "2": False,
      "3": False,
      "jump": False,
      "left": False,
      "right": False,
      "pause": False
    }
    self.level = levelsData["tutorial"][0]

  def resetClassAttributes(self):
    self.gameInformation.update({
      "pause": False,
      "reachedEnd": False,
      "objectivesComplete": False
    })
    self.playerInformation.update({
      "alive": True,
      "score": 0
    }) 
    self.keysPressed.update({
      "1": False,
      "2": False,
      "3": False,
      "jump": False,
      "left": False,
      "right": False,
      "pause": False
    })

  def checkSpecialEvents(self):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        self.transition.fadeOut()
        self.quitTutorial()
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_1:
          self.keysPressed.update({ "1": True })
        if event.key == pygame.K_2:
          self.keysPressed.update({ "2": True })
        if event.key == pygame.K_3:
          self.keysPressed.update({ "3": True })
        if event.key == pygame.K_w or event.key == pygame.K_UP or event.key == pygame.K_SPACE:
          self.keysPressed.update({ "jump": True })
        if event.key == pygame.K_a or event.key == pygame.K_LEFT:
          self.keysPressed.update({ "left": True })
        if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
          self.keysPressed.update({ "right": True })
        if event.key == pygame.K_p or event.key == pygame.K_ESCAPE:
          self.keysPressed.update({ "pause": True })
          self.gameInformation.update({ "pause": True })

  def checkFinishConditions(self):
    if self.level["id"] == 0:
      if self.keysPressed["left"] and self.keysPressed["right"] and self.keysPressed["jump"] and self.keysPressed["pause"]:
        self.gameInformation.update({ "objectivesComplete": True })
    elif self.level["id"] == 2:
      if self.playerInformation["score"] > 0: # score greater than 0 means player picked up a coin
        self.gameInformation.update({ "objectivesComplete": True })

  def writeMessage(self):
    # Messages for first tutorial
    if self.level["id"] == 0:
      drawText(self.screen, text="Move:", x=120, y=100, fontSize=64)
      self.keysSpriteSheet.drawTexture(textureName="a-activated" if self.keysPressed["left"] else "a", x=140, y=180)
      self.keysSpriteSheet.drawTexture(textureName="d-activated" if self.keysPressed["right"] else "d", x=224, y=180)
      drawText(self.screen, text="alternative", x=90, y=250, fontSize=36)
      self.keysSpriteSheet.drawTexture(textureName="left-activated" if self.keysPressed["left"] else "left", x=140, y=290)
      self.keysSpriteSheet.drawTexture(textureName="right-activated" if self.keysPressed["right"] else "right", x=224, y=290)

      drawText(self.screen, text="Jump:", x=520, y=100, fontSize=64)
      self.keysSpriteSheet.drawTexture(textureName="space1-activated" if self.keysPressed["jump"] else "space1", x=500, y=180)
      self.keysSpriteSheet.drawTexture(textureName="space2-activated" if self.keysPressed["jump"] else "space2", x=584, y=180)
      self.keysSpriteSheet.drawTexture(textureName="space3-activated" if self.keysPressed["jump"] else "space3", x=668, y=180)
      drawText(self.screen, text="alternative", x=490, y=250, fontSize=36)
      self.keysSpriteSheet.drawTexture(textureName="w-activated" if self.keysPressed["jump"] else "w", x=540, y=290)
      self.keysSpriteSheet.drawTexture(textureName="up-activated" if self.keysPressed["jump"] else "up", x=624, y=290)

      drawText(self.screen, text="Pause:", x=920, y=100, fontSize=64)
      self.keysSpriteSheet.drawTexture(textureName="esc-activated" if self.keysPressed["pause"] else "esc", x=1000, y=180)
      drawText(self.screen, text="alternative", x=920, y=250, fontSize=36)
      self.keysSpriteSheet.drawTexture(textureName="p-activated" if self.keysPressed["pause"] else "p", x=1000, y=290)
    # Messages for second tutorial
    elif self.level["id"] == 1:
      drawText(self.screen, text="Color change:", x=100, y=100, fontSize=64)
      self.keysSpriteSheet.drawTexture(textureName="1-activated" if self.keysPressed["1"] else "1", x=250, y=180)
      self.keysSpriteSheet.drawTexture(textureName="2-activated" if self.keysPressed["2"] else "2", x=334, y=180)
      self.keysSpriteSheet.drawTexture(textureName="3-activated" if self.keysPressed["3"] else "3", x=418, y=180)
      drawText(self.screen, text="Finish -", x=1050, y=550, fontSize=36)
    # Messages for third tutorial
    elif self.level["id"] == 2:
      drawTextCentered(self.screen, text="Reach the coin!", y=100, fontSize=64)

  def loadingScreen(self, level):
    loadingScreen = LoadingScreen(self.screen, self.colors, self.level["name"], self.playerInformation["score"])

    self.transition.fadeIn(backgroundFunction=loadingScreen.draw)
    # Do a one second break before transition
    sleepWithDrawing(sleepTime=1, drawingFunction=loadingScreen.draw)
    self.transition.fadeOut(backgroundFunction=loadingScreen.draw)

  def finishScreen(self):
    self.transition.fadeIn(backgroundFunction=self.drawFinishScreen)
    # Display finish screen for two seconds
    sleepWithDrawing(sleepTime=1, drawingFunction=self.drawFinishScreen)
    self.transition.fadeOut(backgroundFunction=self.drawFinishScreen)
    self.quitTutorial()

  def drawFinishScreen(self):
    self.screen.fill(self.colors["background"])
    drawTextCentered(self.screen, text="You finished the tutorial!", y=200, fontSize=64)
    drawTextCentered(self.screen, text="Have fun!", y=350, fontSize=36)


  def start(self):
    solidTiles = []
    walls = []
    platforms = []
    coins = []
    enemies = []
    finish = []

    pauseScreen = PauseScreen(self.screen, self.colors, self.gameInformation, self.transition.fadeOut, self.quitTutorial)
    player = Player(self.screen, self.colors, solidTiles, walls, platforms, coins, finish, self.playerInformation)
    level = Level(self.screen, self.colors, solidTiles, walls, platforms, coins, enemies, finish, player, self.playerInformation, self.level["dataFileName"])

    level.build()

    self.loadingScreen(level)

    self.transition.fadeIn(backgroundFunction=level.draw)

    while self.playerInformation["alive"] and not self.gameInformation["objectivesComplete"] and not player.finishAnimationEnded:
      # Max fps
      clock.tick(60)
      # Check if any special keys are pressed
      self.checkSpecialEvents()
      # Check if user fulfilled finish conditions
      self.checkFinishConditions()
      # Check if game is paused
      while self.gameInformation["pause"]:
        # Max fps
        clock.tick(60)
        # Draw pause screen elements
        self.screen.fill(self.colors["background"])
        self.writeMessage()
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
      self.writeMessage()
      level.draw()
      player.draw()
      # Update screen
      pygame.display.update()

    self.transition.fadeOut()
    # Player has not died
    if self.playerInformation["alive"]:
      nextLevelIndex = self.level["id"] + 1
      # There is another tutorial level
      if len(levelsData["tutorial"]) > nextLevelIndex:
        self.level = levelsData["tutorial"][nextLevelIndex]
        self.resetClassAttributes()
        self.start()
      # That was the last level
      else:
        self.finishScreen()
    # Player died - restart level
    else:  
      self.resetClassAttributes()
      self.start()