import pygame

def __init__(): # Intitalizes program

    global clock
    clock = pygame.time.Clock()
    clock.tick(60) # Controls frame rate

    while True:
        Game()
def Game(): # Master Game update

__init__();