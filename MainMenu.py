import pygame
from Text import *
from Button import *
from Display import *
import Commands


class MainMenu():
    """Contains instructions for the main menu"""
    def __init__(this, screen, events):
        this.screen = screen
        this.events = events
        this.title = Text(screen, "QuickSlot", screen.get_width()/2, 20, (225,240,230), 30, "Fonts/Roboto.ttf", True, True, True, True, this.screen.get_width()/8, -100, 0.8)
        this.button = Button(screen, events, Commands. "Play", screen.get_width()/2, 300, 200, 50, (100,250,100), (0,0,0), True, 0.75)

    def Update(this, gameState):
        this.title.Draw()
        this.button.Draw()
        
        this.button.Clicked()
