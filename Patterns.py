import pygame
from pygame.math import Vector2
from Player import *
from math import sin
from math import cos
from random import randint

class CirclePattern():
    """Lasers Fire inwards in a circular pattern"""
    def __init__(this, screen, laser, size, speed, radius, center, timeToLive = 1800):
        ### Universal Components
        this.screen = screen
        
        ### Laser
        this.laser = laser
        this.size = size
        this.speed = 6
        this.totalTime = 0
        this.timeToLive = timeToLive

        this.pos = []
        this.rot = []
        this.frame = 0
        this.inactiveFrames = 50
        this.active = False

        ### Pattern
        this.radius = 1
        this.center = center
        this.increment = 4500

        this.CreateLasers()

    def CreateLasers(this):
        for i in range (-4500, 2 * 31415, this.increment):
            angle = i/10000
            x = this.radius * cos(angle)
            y = this.radius * sin(angle)
            this.pos.append(Vector2(x + this.center.x, y + this.center.y))
            rotation = atan2(-y, x)
            this.rot.append(rotation * 180/pi + 90)

    def Update(this):
        if (this.frame == this.inactiveFrames):
            this.active = True
        if (this.active):
            this.pos = Move(this.pos, this.rot, this.speed)
            if (this.totalTime == this.timeToLive):
                while (len(this.pos) != 0):
                    this.pos.pop()
                    this.rot.pop()
            else:
                this.totalTime += 1
        else:
            this.frame+=1


    def Finished(this):
        if (len(this.pos) == 0):
            return True

class CirclePlayerPattern():
    """Lasers Fire towards Player in a circular pattern"""
    def __init__(this, screen, player, laser, size, speed, radius, center, timeToLive = 1800):
        ### Universal Components
        this.screen = screen
        this.player = player
        
        ### Laser
        this.laser = laser
        this.size = size
        this.speed = speed
        this.totalTime = 0
        this.timeToLive = timeToLive

        this.pos = []
        this.rot = []

        ### Pattern
        this.radius = radius
        this.center = center
        this.time = 15
        this.rate = 25
        this.currentLasers = -1
        this.increment = 7500

        this.CreateLasers()

    def CreateLasers(this):
        for i in range (-4500, 2 * 31415, this.increment):
            angle = i/10000
            x = this.radius * cos(angle)
            y = this.radius * sin(angle)
            this.pos.append(Vector2(x + this.center.x, y + this.center.y))

    def Update(this):
        this.pos = Move(this.pos, this.rot, this.speed)
        if (this.currentLasers < len(this.pos) - 1):
            if (this.time == this.rate):
                this.currentLasers +=1
                this.time = 0
                distance = Vector2(this.pos[this.currentLasers].x - this.player.GetPosition()[0], this.player.GetPosition()[1] - this.pos[this.currentLasers].y)
                rotation = atan2(distance.y, distance.x)
                this.rot.append(rotation * 180/pi + 90)
            else:
                this.time += 1
        if (this.totalTime == this.timeToLive):
            while (len(this.pos) != 0):
                this.pos.pop()
                this.rot.pop()
        else:
            this.totalTime += 1

    def Finished(this):
        if (len(this.pos) == 0):
            return True


class XPattern():
    """Lasers Fire in an X Pattern"""
    def __init__(this, screen, laser, size, speed, radius, center, lasersPerCorner, timeToLive = 1800):
        ### Universal Components
        this.screen = screen
        
        ### Laser
        this.laser = laser
        this.size = size
        this.speed = speed
        this.totalTime = 0
        this.timeToLive = timeToLive

        this.pos = []
        this.rot = []

        ### Pattern
        this.radius = radius
        this.center = center
        this.lasersPerCorner = lasersPerCorner

        this.CreateLasers()

    def CreateLasers(this):
        placement = Vector2(0,this.screen.get_height())
        modifier = Vector2(-1,1)
        for i in range(0,4):
            if (i == 1):
                placement.x = this.screen.get_width()
                modifier.x = 1
            elif (i == 2):
                placement.y = 0
                modifier.y = -1
            elif (i == 3):
                placement.x = 0
                modifier.x = -1
            for j in range(0,this.lasersPerCorner):
                x = ((j*135) + placement.x) * modifier.x
                y = ((j*135) + placement.y) * modifier.y
                this.pos.append(Vector2(x,y))
                distance = Vector2(x - this.center.x, this.center.y - y)
                this.rot.append(atan2(distance.y, distance.x) * 180/pi + 90)

    def Update(this):
        this.pos = Move(this.pos, this.rot, this.speed)
        if (this.totalTime == this.timeToLive):
            while (len(this.pos) != 0):
                this.pos.pop()
                this.rot.pop()
        else:
            this.totalTime += 1

    def Finished(this):
        if (len(this.pos) == 0):
            return True

class EnclosingCirclePattern():
    """Lasers Fire encloses around an area before seperating"""
    def __init__(this, screen, laser, size, speed, radius, center, timeToLive = 1800):
        ### Universal Components
        this.screen = screen
        
        ### Laser
        this.laser = laser
        this.size = size
        this.speed = speed
        this.totalTime = 0
        this.timeToLive = timeToLive

        this.pos = []
        this.rot = []

        ### Pattern
        this.radius = 650
        this.center = center
        this.increment = 4500

        this.CreateLasers()

    def CreateLasers(this):
        for rotation in range(-4500,2*31415,this.increment):
            angle = (rotation)/10000
            angle2 = (rotation+this.increment)/10000
            x = this.radius * cos(angle)
            y = this.radius * sin(angle)
            x2 = this.radius * cos(angle2)
            y2 = this.radius * sin(angle2)
            this.pos.append(Vector2(x + this.center[0], y + this.center[1]))
            rotation = atan2(-y2, x2)
            this.rot.append(rotation * 180/pi + 90)

    def Update(this):
        this.pos = Move(this.pos, this.rot, this.speed)
        if (this.totalTime == this.timeToLive):
            while (len(this.pos) != 0):
                this.pos.pop()
                this.rot.pop()
        else:
            this.totalTime += 1

    def Finished(this):
        if (len(this.pos) == 0):
            return True

def Move(pos, rot, speed):
    for i in range (0, len(rot) - 1):
        pos[i].x -= cos((90-rot[i]) * pi/180) * speed
        pos[i].y -= sin((90-rot[i]) * pi/180) * speed
    return pos
