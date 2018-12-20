import pygame
from Text import *

class Button():
    """Creates a clickable button"""
    def __init__(this, screen, txt, x, y, sizeX, sizeY, btnCol, txtCol):
        this.screen = screen
        this.txt = txt
        this.x = x
        this.y = y
        this.size = (sizeX, sizeY) # A tuple is used here but not for x and y since tuples aren't mutable
        this.btnCol = btnCol
        this.txtCol = txtCol
        this.text = Text(screen, this.txt, this.x, this.y - this.size[1]/2 + 7, this.txtCol, 30, "Fonts/Roboto.ttf",True, False, False, False, 0, 0, 0)

    def Draw(this):
        pygame.draw.rect(this.screen, this.btnCol, pygame.Rect(this.x-this.size[0]/2, this.y-this.size[1]/2, this.size[0], this.size[1]))
        this.text.Draw()