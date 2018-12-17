import pygame
import sys
from pygame.locals import *

class Events():
    """Listens for User Input"""
    def  __init__(this):
        this.leftClick = False
        this.rightClick = False
        this.Left = False
        this.Right = False
        this.Up = False
        this.Down = False

    def Update(this):
        this.leftClick = False
        this.rightClick = False
        for event in pygame.event.get(): # Checks each event
            print(event);
            if (event.type == QUIT): # Application closed
                sys.exit(0)

            if (pygame.mouse.get_pressed()[0]): # Left mouse click
                this.leftClick = True

            if (pygame.mouse.get_pressed()[1]): # Right mouse clicks
                this.rightClick = True

            #if (pygame.key.get_pressed()[)

