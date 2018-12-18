class Text():
    """Text Rendering"""
    def __init(this, screen, text, x, y, color, size, font):
        this.screen = screen
        this.text = text
        this.x = x
        this.y = y
        this.color = color
        this.size = size
        this.font = font

    def Draw(this):
        this.text = this.font.render(this.text, 1, this.color)
        this.screen.blit(this.text, (this.x, this.y))