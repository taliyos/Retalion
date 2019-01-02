import pygame
from Text import *
from random import randint

class Game():
    """Main Level"""
    def __init__(this, screen, events, levelManager):
        ### Universal Componenets
        this.screen = screen
        this.events = events
        this.levelManager = levelManager

        # Level Properties
        this.state = 0
        this.stageText = Text(screen, "", screen.get_width()/2, 20, (225, 75, 50), 45, "Fonts/Roboto.ttf", True, False, False, False, 0, 0, 0)
        this.colorList = [(225, 50, 50), (50, 225, 50), (50, 50, 225)]
        this.textColor = 0
        this.textState = 1

        # State-Specific Properties
        ## Bonus Round
        this.bonusFrame = 0
        this.frameTime = 0

    def Update(this):
        this.screen.fill((15,15,15))
        this.UpdateState()

    def UpdateState(this):
        if (this.state == 0):
            this.BonusRound()

    def BonusRound(this):
        # Intro text
        if (this.bonusFrame < 250):
            this.stageText.SetText("BONUS ROUND")
            if (this.frameTime < this.bonusFrame):
                this.frameTime = this.bonusFrame + 7
                this.textState*=-1
                this.textColor+=1
                if (this.textColor == len(this.colorList)):
                    this.textColor = 0
                this.stageText.SetColor(this.colorList[this.textColor])
            if (this.textState == 1):
                this.stageText.Draw()
        this.bonusFrame+=1

        # Game
        

    def ForceState(this, state):
        this.state = state
        this.bonusFrame = 0
        
