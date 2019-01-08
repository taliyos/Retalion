import pygame
from Text import *
from Button import *
from Display import *
import Commands
from Commands import *
from Leaderboards import *


class GameOver():
    """GameOver screen"""
    def __init__(this, screen, events, levelManager, time):
        ### Universal Components
        this.screen = screen
        this.events = events
        this.levelManager = levelManager

        this.time = round((time - 250)/60,2)

        this.title = Text(screen, "GAME OVER", screen.get_width()/2, 20, (225,240,230), 50, "Fonts/Roboto.ttf", True, False, False, False, 0, 0, 0)
        this.title = Text(screen, "You played for: " + str(this.time) + " seconds", screen.get_width()/2, 20, (225,240,230), 30, "Fonts/Roboto.ttf", True, False, False, False, 0, 0, 0)
        this.button = Button(screen, events, this.levelManager, Command.LevelChange, 1, "Play Again?", screen.get_width()/2, 300, 200, 50, (100,250,100), (150,255,150), (75,225,75), (0,0,0), False, 11)
        this.boards = Leaderboards(screen, events, this.time)

    def Update(this, gameState):
        this.title.Draw()
        this.button.Draw()
        
        this.button.ButtonState()
        this.boards.Update()
