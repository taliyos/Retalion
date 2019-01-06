import pygame
from Events import *
from LevelManager import *

class Display():
    """Generates and maintains the Screen"""
    def __init__(this, events):
        this.WIDTH = 600
        this.HEIGHT = 800
        this.events = events
        this.screen = pygame.display.set_mode((this.WIDTH, this.HEIGHT))
        pygame.display.set_caption("Retalion")
        this.levelManager = LevelManager(this.screen, this.events)

    def Update(this): # Draws to the screen
        this.levelManager.Update()

    def TidyFrame(this): # Renders final frame
        pygame.display.update();
        this.screen.fill((0,0,0))
