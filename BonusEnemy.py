import pygame
from random import randint

class BonusEnemy():
    """Enemy designed for Bonus Round"""
    def __init__(this, screen):
        ### Universal Components
        this.screen = screen

        this.rate = 25
        this.frame = -1

        this.size = (5,35)
        this.lasers = []
        this.laserX = []
        this.laserY = []
        this.rotation = []
     
    def Update(this):
        if (this.frame == -1 or this.frame > this.rate):
            this.frame = 0
            this.FireLasers()
        this.frame+=1
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
      
    def Draw(this):
        for x in range(0,len(this.laserX) - 1):
            pygame.draw.rect(this.screen, (255,0,0), pygame.Rect(this.laserX[x]-this.size[0]/2, this.laserY[x]-this.size[1]/2, this.size[0], this.size[1]))
            