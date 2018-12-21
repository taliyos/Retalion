import pygame
from Text import *
from Display import *
from Events import *
from Transitions import *
import Commands

class Button():
    """Creates a clickable button"""
    def __init__(this, screen, events, command, txt, x, y, sizeX, sizeY, btnCol, txtCol, fadeIn, speed):
        this.screen = screen
        this.events = events
        this.command = command
        this.txt = txt
        this.x = x
        this.desiredX = x
        this.y = y
        this.size = (sizeX, sizeY) # A tuple is used here but not for x and y since tuples aren't mutable
        this.btnCol = btnCol
        this.txtCol = txtCol
        this.fadeIn = fadeIn
        this.speed = speed
        if (this.fadeIn):
            this.x = screen.get_width()
        this.text = Text(screen, this.txt, this.x, this.y - this.size[1]/2 + 7, this.txtCol, 30, "Fonts/Roboto.ttf",True, False, False, False, 0, 0, speed)

    def Draw(this):
        if (this.fadeIn):
            this.x = Transitions.FadeInRight(this.x, this.desiredX, this.speed)
            this.text.UpdatePosition(this.x, this.y)
        pygame.draw.rect(this.screen, this.btnCol, pygame.Rect(this.x-this.size[0]/2, this.y-this.size[1]/2, this.size[0], this.size[1]))
        this.text.Draw()

    def Clicked(this):
        if (this.events.GetMouseDown()):
            if (pygame.mouse.get_pos()[0] >= this.x - this.size[0]/2 and pygame.mouse.get_pos()[0] <= this.x + this.size[1]/2 and
                    pygame.mouse.get_pos()[1] >= this.y - this.size[1]/2 and pygame.mouse.get_pos()[1] <= this.y + this.size[1]/2):
                Commands.CommandHandler()