import pygame
from math import *
from Text import *

class Player():
    """The Player"""
    def __init__(this, screen, events, levelManager):
        ### Universal Components
        this.screen = screen
        this.events = events
        this.levelManager = levelManager

        # Player Properties
        this.speed = 6.8
        this.rotSpeed = 6.89
        this.x = 300
        this.y = 400
        this.rot = 0
        this.size = (50,50)
        this.color = (235,235,235)
        this.player = pygame.image.load("Images/Player.png").convert_alpha()
        this.playerRect = this.player.get_rect()
        this.hp = 3
        this.hpText = Text(screen, ("Health: " + str(this.hp)), 5, 5, (255,255,255), 18, "Fonts/Roboto.ttf", False, False, False, False, 0, 0 , 0)

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
        this.hpText.Draw()
        

    def ClampBoundaries(this):
        if (this.x > this.screen.get_width() + this.size[0]/2):
            this.x = -this.size[0]/2 + 1
        elif (this.x < -this.size[0]/2):
            this.x = this.screen.get_width() + this.size[0]/2 - 1

        if (this.y > this.screen.get_height() + this.size[1]/2):
            this.y = -this.size[1]/2 + 1
        elif (this.y < -this.size[1]/2):
            this.y = this.screen.get_height() + this.size[1]/2 - 1
            
    def SetState(this, state):
        this.state = state

    def GetPosition(this):
        return (this.x, this.y)

    def ChangeHP(this, amount):
        this.hp += amount
        if (this.hp == 0):
            this.levelManager.SetWindow(2)
        this.hpText.SetText("Health: " + str(this.hp))