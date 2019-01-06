import pygame
from math import *

class Player():
    """The Player"""
    def __init__(this, screen, events):
        ### Universal Components
        this.screen = screen
        this.events = events

        # Player Properties
        this.speed = 8.77
        this.rotSpeed = 6.89
        this.image = 0 # TODO
        this.x = 300
        this.y = 400
        this.rot = 0
        this.size = (50,50)
        this.color = (235,235,235)
        this.player = pygame.image.load("Images/Player.png").convert_alpha()
        this.playerRect = this.player.get_rect()

        # State-Specific Properties
        this.state = 0

    def Update(this):
        if (this.CheckControls()):
            this.Movement()
        this.ClampBoundaries()
        this.Draw()

    def CheckControls(this):
        if (this.events.GetHorizontal() != 0 or this.events.GetVertical() != 0):
            return True
        else:
            return False

    def Movement(this):
        this.rot += this.rotSpeed * -this.events.GetHorizontal()
        this.rot %= 360

        this.x += -this.speed * this.events.GetVertical() * cos((this.rot + 90) * (pi/180))
        this.y += this.speed * this.events.GetVertical() * sin((this.rot + 90) * (pi/180))

    def Draw(this):
        surface = pygame.transform.rotate(this.player, this.rot)
        this.playerRect = surface.get_rect()
        this.playerRect.center = (this.x, this.y)
        this.screen.blit(surface, this.playerRect)
        
    def UpdateControls(this):
        if (this.state):
            print("BONUS ROUND CONTROLS")

    def ClampBoundaries(this):
        if (this.x > this.screen.get_width()):
            this.x = this.screen.get_width()
        elif (this.x < 0):
            this.x = 0

        if (this.y > this.screen.get_height()):
            this.y = this.screen.get_height()
        elif (this.y < 0):
            this.y = 0
            
    def SetState(this, state):
        this.state = state
        this.UpdateControls()

    def GetPosition(this):
        return (this.x, this.y)