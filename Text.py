import pygame

class Text():
    """Text Rendering"""
    def __init__(this, screen, text, x, y, color, size, font):
        this.screen = screen
        this.text = text
        this.x = x
        this.y = y
        this.color = color
        this.size = size
        pygame.font.init() # Initializes the font
        this.font = pygame.font.Font(font, size)

    def Draw(this):
        this.text = this.font.render(this.text, 1, this.color, None)
        this.screen.blit(this.text, (this.x, this.y))