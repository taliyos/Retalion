import pygame
from Events import *

class Display():
    """Generates and maintains the Screen"""
    def __init__(this):
        this.WIDTH = 600
        this.HEIGHT = 800
        this.screen = pygame.display.set_mode((this.WIDTH, this.HEIGHT))
    def Draw(this): # Draws to the screen
        print("TODO")
    def TidyFrame(this): # Renders final frame
        pygame.display.update();
        this.screen.fill((0,0,0))
