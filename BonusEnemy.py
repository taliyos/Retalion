import pygame
from pygame.math import Vector2
from random import randint
from math import *

class BonusEnemy():
    """Enemy designed for Bonus Round"""
    def __init__(this, screen, events, player):
        ### Universal Components
        this.screen = screen
        this.events = events
        this.player = player

        this.center = (this.screen.get_width()/2, this.screen.get_height()/2) # Center of screen

        ### Laser
        this.laser = pygame.image.load("Images/Laser.png").convert_alpha() # Laser image
        this.size = (5,35)
        this.color = (255,0,0)
         
        ### Stage Variables
        this.level = 0
        this.speed = 10
        this.rotation = []
        this.stage = -55

        ### Stage 1 Variables
        this.radius = 500
        this.laserX = []
        this.laserY = []

        ### Stage 2 Variables
        this.fireRate = 2
        this.fireTime = -1
        this.currentLasers = -1

        ### Stage 3 Variables
        this.stage3Pos = []
        this.stage3Rot = []
     
    def Update(this):
        if (this.stage == -1):
            this.LaserPattern1(4500, True, (200,200))
            this.stage = 0
        elif (this.stage == 1):
            print("STAGE 2")
            this.LaserPattern2()
            this.stage = 2
        elif (this.stage < -1):
            this.LaserPattern3(25, (100,150))
            this.stage = 5
        this.CheckStage()
        this.Draw()

    def FireLasers(this):
        x = randint(-30, 30)
        y = randint(-30, 30)
        if (x > 0):
            x += this.screen.get_width()
        if (y > 0):
            y += this.screen.get_height()
        this.laserX.append(x)
        this.laserY.append(y)
        yDistance = this.screen.get_height()/2 - y
        xDistance = x-this.screen.get_width()/2
        rotation = atan2(yDistance, xDistance)
        this.rotation.append(rotation * (180/pi) + 90)

    def LaserPattern1(this, increment = 4500, storeRotation = True, center = -1):
        """Circular, Hits a specified portion of the screen"""
        if (center == -1):
            center = this.center
        for rotation in range(-4500,2*31415,increment):
            angle = rotation/10000
            x = this.radius * cos(angle)
            y = this.radius * sin(angle)
            this.laserX.append(x + center[0])
            this.laserY.append(y + center[1])
            if (storeRotation):
                rotation = atan2(-y, x)
                this.rotation.append(rotation * 180/pi + 90)
                
    def LaserPattern2(this):
        """Circular, Dependent on Player Position"""
        this.currentLasers = -1
        this.fireTime = -1
        this.LaserPattern1(500, False)

    def LaserPattern3(this, lasersPerCorner = 25, center = -1):
        """X Shape"""
        # Lasers at each corner
        if (center == -1):
            center = this.center
        placement = Vector2(0,this.screen.get_height())
        modifier = Vector2(-1,1)
        for i in range(0,4):
            print(i)
            if (i == 1):
                placement.x = this.screen.get_width()
                modifier.x = 1
            elif (i == 2):
                placement.y = 0
                modifier.y = -1
            elif (i == 3):
                placement.x = 0
                modifier.x = -1
            for j in range(0,lasersPerCorner):
                x = ((j*100) + placement.x) * modifier.x
                y = ((j*100) + placement.y) * modifier.y
                this.stage3Pos.append(Vector2(x,y))
                distance = Vector2(x - center[0], center[1] - y)
                this.stage3Rot.append(atan2(distance.y, distance.x) * 180/pi + 90)


    def CheckStage(this):
        """Adds rotational values to pattern 2 lasers"""
        if (this.stage == 2):
            if (this.currentLasers == len(this.laserX) - 1):
                return
            if (this.fireTime == this.fireRate or this.currentLasers == -1):
                this.currentLasers += 1
                xDistance = this.laserX[this.currentLasers] - this.player.GetPosition()[0]
                yDistance = this.player.GetPosition()[1] - this.laserY[this.currentLasers]
                rotation = atan2(yDistance, xDistance)
                this.rotation.append(rotation * 180/pi + 90)
                this.fireTime = -1 # Unchecked, this variable could cause a crash
            this.fireTime+=1
            
    def Draw(this):
        lasersToRemove = 0
        for i in range(0,len(this.laserX) - 1):
            if (this.stage == 2 and this.currentLasers < i):
                surface = pygame.transform.rotate(this.laser, 0)
            else:
                surface = pygame.transform.rotate(this.laser, this.rotation[i])
            position = pygame.Rect(this.laserX[i]-this.size[0]/2, this.laserY[i]-this.size[1]/2, this.size[0], this.size[1])
            position = surface.get_rect(center = position.center)
            this.screen.blit(surface, position)

            if (this.stage == 0 or (this.stage == 2 and this.currentLasers >= i)): # Stage is 0 or Stage 2 with fireable laser
                this.laserX[i] -= cos((90-this.rotation[i]) * pi/180) * this.speed
                this.laserY[i] -= sin((90-this.rotation[i]) * pi/180) * this.speed

            if (this.stage == 0 and (this.laserX[i] > 950 or this.laserX[i] < -350)):
                lasersToRemove += 1
        while (lasersToRemove  != 0):
            this.laserX.pop()
            this.laserY.pop()
            this.rotation.pop()
            lasersToRemove-=1

        for i in range (0, len(this.stage3Pos) - 1):
            surface = pygame.transform.rotate(this.laser, this.stage3Rot[i])
            position = pygame.Rect(this.stage3Pos[i].x-this.size[0]/2, this.stage3Pos[i].y-this.size[1]/2, this.size[0], this.size[1])
            position = surface.get_rect(center = position.center)
            this.screen.blit(surface, position)
            
            this.stage3Pos[i].x -= cos((90-this.stage3Rot[i]) * pi/180) * this.speed
            this.stage3Pos[i].y -= sin((90-this.stage3Rot[i]) * pi/180) * this.speed