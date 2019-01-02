import pygame
from Transitions import *

class Text():
    """Text Rendering"""
    def __init__(this, screen, text, x, y, color, size, font, center, fadeInLeft, fadeInTop, fadeColor, startX, startY, speed):
        this.screen = screen
        this.text = text
        this.x = x
        this.desiredX = x
        this.y = y
        this.desiredY = y
        this.color = color
        this.desiredColor = color
        this.size = size
        this.speed = speed
        pygame.font.init() # Initializes the font
        this.font = pygame.font.Font(font, size)
        this.center = center
        this.fadeInLeft = fadeInLeft
        this.fadeInTop = fadeInTop
        this.fadeColor = fadeColor
        if (fadeInLeft):
            this.x = startX
        if (fadeInTop):
            this.y = startY
        if (fadeColor):
            this.color = (0,0,0)

    def Draw(this):
        if (this.fadeInLeft):
            this.x = Transitions.FadeInLeft(this.x, this.desiredX, this.speed)
        this.y = this.desiredY
        if (this.fadeInTop):
            this.y = Transitions.FadeInLeft(this.y, this.desiredY, this.speed)
        if (this.fadeColor):
            this.color = Transitions.FadeInColor(this.color, this.desiredColor, this.speed)
        text = this.font.render(this.text, 1, this.color)
        textInfo = text.get_rect()
        coords = (this.x, this.y)
        if (this.center):
            coords = (this.x - textInfo.center[0], this.y)
        this.screen.blit(text, coords) # Puts text on the screen

    def UpdatePosition(this, x, y):
        this.x = x
        this.y = y

    def SetText(this, text):
        this.text = text

    def GetText(this):
        return this.text

    def SetColor(this, color):
        this.color = color
        