import pygame
from Text import *
from Display import *


class MainMenu():
    """Contains instructions for the main menu"""
    def __init__(this, screen):
        this.screen = screen
        this.title = Text(screen, "QuickSlot", screen.get_width()/2, 20, (225,240,230), 30, "Fonts/Roboto.ttf", True)

    def Update(this, gameState):
        this.title.Draw()
