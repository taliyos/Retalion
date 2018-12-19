import pygame

class Text():
    """Text Rendering"""
    def __init__(this, screen, text, x, y, color, size, font, center, fadeInLeft):
        this.screen = screen
        this.text = text
        this.x = x
        this.desiredX = x
        this.y = y
        this.color = color
        this.desiredColor = color
        this.size = size
        pygame.font.init() # Initializes the font
        this.font = pygame.font.Font(font, size)
        this.center = center
        this.fadeInLeft = fadeInLeft
        if (fadeInLeft):
            this.x = 0
            this.color = (0,0,0)
        this.speed = 1

    def Draw(this):
        if (this.fadeInLeft):
            this.FadeInLeft()

        text = this.font.render(this.text, 1, this.color)
        textInfo = text.get_rect()
        coords = (this.x, this.y)
        if (this.center):
            coords = (this.x - textInfo.center[0], this.y)
        this.screen.blit(text, coords) # Puts text on the screen

    def FadeInLeft(this): # Animation on text
        if (this.x < this.desiredX):
            this.x += 1
        colList = list(this.color)
        for i in range(len(colList)):
            if (colList[i] < this.desiredColor[i]):
                colList[i]+=1
        this.color = tuple(colList)
        
