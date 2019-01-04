import pygame
from math import *

class Player():
    """The Player"""
    def __init__(this, screen, events):
        ### Universal Components
        this.screen = screen
        this.events = events

        # Player Properties
        this.speed = 7
        this.rotSpeed = 4.6
        this.image = 0 # TODO
        this.x = 300
        this.y = 300
        this.rot = 0
        this.size = (50,50)
        this.color = (235,235,235)
        this.player = pygame.image.load("Player.png").convert_alpha()
        this.playerRect = this.player.get_rect()

        # State-Specific Properties
        this.state = 0

    def Update(this):
        if (this.CheckControls()):
            this.Movement()
        this.Draw()

    def CheckControls(this):
        if (this.events.GetHorizontal() != 0 or this.events.GetVertical() != 0):
            return True
        else:
            return False

    def Movement(this):
        #print(this.rot)
        this.rot += this.rotSpeed * -this.events.GetHorizontal()
        this.rot %= 360

        #this.playerRect.x += this.speed * this.events.GetHorizontal()
        #this.playerRect.y += this.speed * this.events.GetVertical()
        #print(cos(2*pi))
        this.x += -this.speed * this.events.GetVertical() * cos((this.rot + 90) * (pi/180))
        this.y += this.speed * this.events.GetVertical() * sin((this.rot + 90) * (pi/180))
        print(cos(this.rot * (pi/180)))
        #print(sin(this.rot))
        print()
        #this.y += this.speed * this.events.GetVertical()
        #this.x += this.speed * this.events.GetHorizontal()

    def Draw(this):
        #pygame.draw.rect(this.screen, this.color, pygame.Rect(this.x - this.size[0]/2, this.y - this.size[1]/2, this.size[0], this.size[1]))
        surface = pygame.transform.rotate(this.player, this.rot)
        this.playerRect = surface.get_rect()
        this.playerRect.center = (this.x - 25, this.y-25)
        this.screen.blit(surface, this.playerRect)
        
    def UpdateControls(this):
        if (this.state):
            print("BONUS ROUND CONTROLS")
            
    def SetState(this, state):
        this.state = state
        this.UpdateControls()