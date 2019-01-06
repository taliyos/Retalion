import pygame
from random import randint
from math import *

class BonusEnemy():
    """Enemy designed for Bonus Round"""
    def __init__(this, screen, events, player):
        ### Universal Components
        this.screen = screen
        this.events = events

        this.player = player

        this.stage = -1 # Current Stage

        this.center = (this.screen.get_width()/2, this.screen.get_height()/2) # Center of screen

        ### Laser
        this.laser = pygame.image.load("Images/Laser.png").convert_alpha() # Laser image
        this.size = (5,35)
        this.color = (255,0,0)
         
        ### Stage Variables
        this.level = 0
        this.speed = 5
        this.rotation = []

        ### Stage 1 Variables
        this.radius = 500
        this.laserX = []
        this.laserY = []

        ### Stage 2 Variables
        this.fireRate = 80
        this.fireTime = -1
        this.currentLasers = 0
     
    def Update(this):
        if (this.stage == -1):
            this.LaserPattern1()
            this.stage = 0
        elif (this.stage == 1):
            this.LaserPattern2()
            this.stage = 2
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

    def LaserPattern1(this, storeRotation = True):
        for rotation in range(-4500,2*31415,4500):
            angle = rotation/10000
            print(angle)
            x = this.radius * cos(angle)
            y = this.radius * sin(angle)
            this.laserX.append(x + this.center[0])
            this.laserY.append(y + this.center[1])
            xDistance = x + this.center[0] - this.center[0]
            yDistance = this.center[1] - (y+this.center[1])
            if (storeRotation):
                rotation = atan2(yDistance, xDistance)
                this.rotation.append(rotation * 180/pi + 90)

    def LaserPattern2(this):
        this.currentLasers = 0
        this.fireTime = -1
        this.LaserPattern1(False)
        i = 0
        for rotation in range(-4500, 2 * 31415, 4500):
            xDistance = this.laserX[i] - this.player.GetPosition()[0]
            yDistance = this.player.GetPosition()[1] - this.laserY[i]
            rotation = atan2(yDistance, xDistance)
            this.rotation.append(rotation * 180/pi + 90)
            i+=1

    def CheckStage(this):
        if (this.stage == 2):
            if (this.currentLasers == len(this.laserX)):
                return
            if (this.fireTime == this.fireRate):
                this.currentLasers += 1
                this.fireTime = 0 # Unchecked, this variable could cause a crash
            this.fireTime+=1
    def Draw(this):
        lasersToRemove = 0
        for i in range(0,len(this.laserX) - 1):
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
            print("REMOVING LASER")
            this.laserX.pop()
            this.laserY.pop()
            this.rotation.pop()
            lasersToRemove-=1
            this.stage += 1




            