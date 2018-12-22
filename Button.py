import pygame
from Text import *
from Display import *
from Events import *
from Transitions import *
import Commands

class Button():
    """Creates a clickable button"""
    def __init__(this, screen, events, levelManager, command, commandParameter, txt, x, y, sizeX, sizeY, btnCol, hvrCol, psdCol, txtCol, fadeIn, speed):
        ### Universal Componenets
        this.screen = screen # used to display button
        this.events = events # gets events
        this.levelManager = levelManager

        ### Commands
        this.command = command # button pressed action
        this.commandParameter = commandParameter # extra button press parameter

        ### Button Properties
        this.x = x # x pos
        this.desiredX = x # used with transitions
        this.y = y # y pos
        this.size = (sizeX, sizeY) # size
        this.txt = txt # text

        ### Colors
        this.btnCol = btnCol # button
        this.hvrCol = hvrCol # hover
        this.psdCol = psdCol # pressed
        this.txtCol = txtCol # text

        ### Transitions
        this.fadeIn = fadeIn # whether or not to use a transition
        this.speed = speed # transition speed
        if (this.fadeIn):
            this.x = screen.get_width()

        ### Button State
        this.hover = False
        this.pressed = False
        
        this.text = Text(screen, this.txt, this.x, this.y - this.size[1]/2 + 7, this.txtCol, 30, "Fonts/Roboto.ttf",True, False, False, False, 0, 0, speed)

    def Draw(this):
        if (this.fadeIn):
            this.x = Transitions.FadeInRight(this.x, this.desiredX, this.speed)
            this.text.UpdatePosition(this.x, this.y)

        color = this.btnCol
        if (this.pressed):
            color = this.psdCol
        elif (this.hover):
            color = this.hvrCol

        pygame.draw.rect(this.screen, color, pygame.Rect(this.x-this.size[0]/2, this.y-this.size[1]/2, this.size[0], this.size[1]))
        this.text.Draw()

    def ButtonState(this):
        if (pygame.mouse.get_pos()[0] >= this.x - this.size[0]/2 and pygame.mouse.get_pos()[0] <= this.x + this.size[0]/2 and
                    pygame.mouse.get_pos()[1] >= this.y - this.size[1]/2 and pygame.mouse.get_pos()[1] <= this.y + this.size[1]/2):
            if (this.events.GetMouseDown() and not this.pressed):
                this.pressed = True
            elif (not this.events.GetMouseDown() and this.pressed):
                this.pressed = False
                Commands.CommandHandler(this.levelManager, this.command, this.commandParameter)
            elif (not this.events.GetMouseDown() and not this.pressed):
                this.hover = True
        else:
            this.hover = False
        if (not this.events.GetMouseDown() and this.pressed):
            this.pressed = False