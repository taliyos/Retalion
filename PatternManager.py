import pygame
from pygame.math import Vector2
from random import randint
from math import *
from Patterns import *

class PatternManager():
    """Manages Pattern Deployment"""
    def __init__(this, screen, events, player):
        ### Universal Components
        this.screen = screen
        this.events = events
        this.player = player

        this.center = Vector2(this.screen.get_width()/2, this.screen.get_height()/2) # Center of screen

        ### Laser
        this.laser = pygame.image.load("Images/Laser.png").convert_alpha() # Laser image
        this.size = (5,35)
        this.color = (255,0,0)
         
        ### Stage Variables
        this.level = 0
        this.speed = 10
        this.stage = -55
        this.timeToLive = 1800

        this.patternWait = 250
        this.time = 0
        this.totalTime = 0

        ### Stage 1 Variables
        this.p1 = []
        this.radius = 500

        ### Stage 2 Variables
        this.p2 = []
        this.fireRate = 2
        this.fireTime = -1
        this.currentLasers = -1
        this.buffer = 10
        this.bufferTime =0

        ### Stage 3 Variables
        this.p3 = []

        ### Stage 4 Variables
        this.p4 = []
     
    def Update(this):
        this.AddPattern()
        this.UpdatePatterns()
        this.Draw()
        this.totalTime+=1
        if (this.totalTime == 1000):
            this.player.ChangeHP(1)
            this.totalTime=0
        if (this.bufferTime != 10):
            this.bufferTime +=1

    def AddPattern(this):
        if (this.patternWait > this.time):
            this.time += 1
            return
        this.time = 0
        this.patternWait = randint(100,250)

        choice = randint(0,3)
        center = Vector2(randint(50, this.screen.get_width()-50), randint(50, this.screen.get_height()-50))
        speed = randint(6,9)
        if (choice == 0):
            this.p1.append(CirclePattern(this.screen, this.laser, this.size, speed, this.radius, center))
        elif (choice == 1):
            this.p2.append(CirclePlayerPattern(this.screen, this.player, this.laser, this.size, speed, this.radius, this.center))
        elif (choice == 2):
            this.p3.append(XPattern(this.screen, this.laser, this.size, speed, this.radius, center, randint(25,100)))
        elif (choice == 3):
            this.p4.append(EnclosingCirclePattern(this.screen, this.laser, this.size, speed, randint(20,250), center))

    def UpdatePatterns(this):
        for i in range(-1,len(this.p1) - 1):
            this.p1[i].Update()
            if (this.p1[i].Finished()):
                this.p1.pop(i)
                i-=1
        for i in range(-1,len(this.p2) - 1):
            this.p2[i].Update()
            if (this.p2[i].Finished()):
                this.p2.pop(i)
                i-=1
        for i in range(-1,len(this.p3) - 1):
            this.p3[i].Update()
            if (this.p3[i].Finished()):
                this.p3.pop(i)
                i-=1
        for i in range(-1,len(this.p4) - 1):
            this.p4[i].Update()
            if (this.p4[i].Finished()):
                this.p4.pop(i)
                i-=1

    def Draw(this):
        for i in range(-1,len(this.p1) - 1):
            for j in range(0,len(this.p1[i].pos) - 1):
                surface = pygame.transform.rotate(this.laser, this.p1[i].rot[j])
                position = pygame.Rect(this.p1[i].pos[j].x-this.size[0]/2, this.p1[i].pos[j].y-this.size[1]/2, this.size[0], this.size[1])
                position = surface.get_rect(center = position.center)
                this.screen.blit(surface, position)
                if (this.Collision(position)):
                    this.OnCollision()
        for i in range(-1,len(this.p2) - 1):
            for j in range(0,len(this.p2[i].rot) - 1):
                surface = pygame.transform.rotate(this.laser, this.p2[i].rot[j])
                position = pygame.Rect(this.p2[i].pos[j].x-this.size[0]/2, this.p2[i].pos[j].y-this.size[1]/2, this.size[0], this.size[1])
                position = surface.get_rect(center = position.center)
                this.screen.blit(surface, position)
                if (this.Collision(position)):
                    this.OnCollision()
        for i in range(-1,len(this.p3) - 1):
            for j in range(0,len(this.p3[i].pos) - 1):
                surface = pygame.transform.rotate(this.laser, this.p3[i].rot[j])
                position = pygame.Rect(this.p3[i].pos[j].x-this.size[0]/2, this.p3[i].pos[j].y-this.size[1]/2, this.size[0], this.size[1])
                position = surface.get_rect(center = position.center)
                this.screen.blit(surface, position)
                if (this.Collision(position)):
                    this.OnCollision()
        for i in range(-1,len(this.p4) - 1):
            for j in range(0,len(this.p4[i].pos) - 1):
                surface = pygame.transform.rotate(this.laser, this.p4[i].rot[j])
                position = pygame.Rect(this.p4[i].pos[j].x-this.size[0]/2, this.p4[i].pos[j].y-this.size[1]/2, this.size[0], this.size[1])
                position = surface.get_rect(center = position.center)
                this.screen.blit(surface, position)
                if (this.Collision(position)):
                    this.OnCollision()

    def Collision(this, laser):
        return laser.colliderect(this.player.playerRect)

    def OnCollision(this):
        if (this.bufferTime == 10):
            this.player.ChangeHP(-1)
            this.bufferTime = 0
