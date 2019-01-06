from MainMenu import *
from Game import *
from GameOver import *

class LevelManager():
    """Keeps track of Game Status"""
    def __init__(this, screen, events):
        ### Universal Components
        this.screen = screen
        this.events = events

        ### Window Options
        this.currentWindow = 0
        this.gameState = -1

        this.mainMenu = MainMenu(screen, events, this)
        this.game = this.mainMenu
        this.gameOver = this.mainMenu

    def Update(this):
        this.UpdateWindow()

    def UpdateWindow(this):
        if (this.currentWindow == 0):
            # Main Menu
            this.mainMenu.Update(this.gameState)
        elif (this.currentWindow == 1):
            # Game
            this.game.Update()
        elif (this.currentWindow == 2):
            # game over
            this.gameOver.Update(this.gameState)

    def GetWindow(this): # returns the current window index
         return this.currentWindow

    def GetGameState(this): # returns the current game state
        return this.gameState

    def SetWindow(this, window):
        this.currentWindow = window
        if (window == 0):
            this.mainMenu = MainMenu(this.screen, this.events, this)
        elif (window == 1):
            this.game = Game(this.screen, this.events, this)
        elif (window == 2):
            this.gameOver = GameOver(this.screen, this.events, this, this.game.time)


