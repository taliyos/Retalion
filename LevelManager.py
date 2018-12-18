class LevelManager():
    """Keeps track of Game Status"""
    def __init__(this, screen):
       this.screen = screen
       this.currentWindow = 0
       this.gameState = -1

    def Update(this):
        this.UpdateWindow()

    def UpdateWindow(this):
        if (this.currentWindow == 0):
            # Main Menu
            this.screen.fill((250,100,100))
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


