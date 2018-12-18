import pygame

class Text():
    """Text Rendering"""
    def __init__(this, screen, text, x, y, color, size, font, center):
        print("hello and welcome to the initializer")
        this.screen = screen
        this.text = text
        this.x = x
        this.y = y
        this.color = color
        this.size = size
        pygame.font.init() # Initializes the font
        this.font = pygame.font.Font(font, size)
        this.center = center

    def Draw(this):
        text = this.font.render(this.text, 1, this.color)
        textInfo = text.get_rect()
        coords = (this.x, this.y)
        if (this.center):
            coords = (this.x - textInfo.center[0], this.y)
        this.screen.blit(text, coords) # Puts text on the screen
