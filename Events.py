import pygame
import sys
from pygame.locals import *

class Events():
    """Listens for User Input"""
    def  __init__(this):
        this.leftClick = False
        this.left = False
        this.right = False
        this.up = False
        this.down = False

    def Update(this):
        for event in pygame.event.get(): # Checks each event

            if (event.type == QUIT): # Application closed
                sys.exit(0)

            if (event.type == MOUSEBUTTONDOWN): # Left mouse click
                this.leftClick = True

            elif (event.type == MOUSEBUTTONUP): # Right mouse clicks
                this.leftClick = False
               
            if (event.type == KEYDOWN):
                if (event.key == K_LEFT):
                    this.left = True
                elif (event.key == K_RIGHT):
                    this.right = True
                elif (event.key == K_UP):
                    this.up = True
                elif (event.key == K_DOWN):
                    this.down = True

            if (event.type == KEYUP):
                if (event.key == K_LEFT):
                    this.left = False
                elif (event.key == K_RIGHT):
                    this.right = False
                elif (event.key == K_UP):
                    this.up = False
                elif (event.key == K_DOWN):
                    this.down = False

