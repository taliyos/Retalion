import pygame
from Text import *
from Player import *
from PatternManager import *
from random import randint

class Game():
    """Main Level"""
    def __init__(this, screen, events, levelManager):
        ### Universal Componenets
        this.screen = screen
        this.events = events
        this.levelManager = levelManager

        # Level Properties
        this.stageText = Text(screen, "", screen.get_width()/2, 20, (225, 75, 50), 45, "Fonts/Roboto.ttf", True, False, False, False, 0, 0, 0)
        this.colorList = [(225, 50, 50), (50, 225, 50), (50, 50, 225)]
        this.textColor = 0
        this.textState = 1

        # State-Specific Properties
        this.state = 0
        ## Bonus Round
        this.bonusFrame = 0
        this.frameTime = 0
        this.textStage = 0

        # Objects
        this.player = Player(screen, events, levelManager)
        this.bonusEnemies = 0

        this.time = 0

        this.SetState(0)

    def Update(this):
        this.screen.fill((15,15,15))
        this.UpdateState()

    def UpdateState(this):
        if (this.state == 0):
            this.Ready()
        elif (this.state == 1):
            this.MainGame()

    def Ready(this):
        # Game
        this.player.Update()

        # Intro Text
        if (not this.FlashingText()):
            this.textStage += 1
            this.ChangeText(this.textStage)
        if (this.textStage == 3):
            this.bonusEnemies = PatternManager(this.screen, this.events, this.player)
            this.state = 1

    def MainGame(this):
        # Game
        this.player.Update()
        this.bonusEnemies.Update()
        this.time += 1
        
    def FlashingText(this):
        if (this.textStage > 5):
            return True
        if (this.bonusFrame < 50):
            if (this.bonusFrame % 75 == 0):
                this.textColor+=1
                if (this.textColor == len(this.colorList)):
                    this.textColor = 0
            this.stageText.SetColor(this.colorList[this.textColor])
            if (this.textState == 1):
                this.stageText.Draw()
            this.bonusFrame+=1
            return True
        else:
            this.bonusFrame+=1
            return False

    def ChangeText(this, textStage):
        if (textStage == 0):
            this.stageText.SetText("Ready?")
        elif (textStage == 1):
            this.stageText.SetText("Set...")
        elif (textStage == 2):
            this.stageText.SetText("GO!")
        else:
            this.stageText.SetText("")
        this.textState = 1
        this.bonusFrame = 0

    def SetState(this, state):
        if (state == 0):
            this.stageText.SetText("Ready?")
            this.bonusFrame = 0
            this.player.SetState(state)

        this.state = state