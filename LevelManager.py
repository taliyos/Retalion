from MainMenu import *

class LevelManager():
    """Keeps track of Game Status"""
    def __init__(this, screen, events):
       this.screen = screen
       this.events = events
       this.currentWindow = 0
       this.gameState = -1
       this.mainMenu = MainMenu(screen, this.events)

    def Update(this):
        this.UpdateWindow()

    def UpdateWindow(this):
        if (this.currentWindow == 0):
            # Main Menu
            this.mainMenu.Update(this.gameState)
        elif (this.currentWindow == 1):
            # Game
            print("Game")
        elif (this.currentWindow == 2):
            # game over
            print("game over")

    def GetWindow(this): # returns the current window index
         return this.currentWindow

    def GetGameState(this): # returns the current game state
        return this.gameState


