import pygame
from Text import *
from Button import *
from Display import *


class MainMenu():
    """Contains instructions for the main menu"""
    def __init__(this, screen):
        this.screen = screen
        this.title = Text(screen, "QuickSlot", screen.get_width()/2, 20, (225,240,230), 30, "Fonts/Roboto.ttf", True, True, True, True, this.screen.get_width()/8, -100, 0.8)
        this.button = Button(screen, "Play", screen.get_width()/2, 300, 200, 50, (100,250,100), (0,0,0))

    def Update(this, gameState):
        this.title.Draw()
        this.button.Draw()
