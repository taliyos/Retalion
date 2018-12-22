import pygame
from Text import *
from Button import *
from Display import *
import Commands
from Commands import *


class MainMenu():
    """Contains instructions for the main menu"""
    def __init__(this, screen, events, levelManager):
        ### Universal Components
        this.screen = screen
        this.events = events
        this.levelManager = levelManager

        this.title = Text(screen, "QuickSlot", screen.get_width()/2, 20, (225,240,230), 30, "Fonts/Roboto.ttf", True, True, True, True, this.screen.get_width()/8, -100, 12)
        this.button = Button(screen, events, this.levelManager, Command.LevelChange, 1, "Play", screen.get_width()/2, 300, 200, 50, (100,250,100), (150,255,150), (75,225,75), (0,0,0), True, 11)

    def Update(this, gameState):
        this.title.Draw()
        this.button.Draw()
        
        this.button.ButtonState()
