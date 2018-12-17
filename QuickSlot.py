import pygame
from Display import *
from Events import *

def __init__(): # Intitalizes program

    global clock
    clock = pygame.time.Clock()
    clock.tick(60) # Controls frame rate

    global eventHandler 
    eventHandler = Events() # Listens for mouse and keyboard clicks

    global display
    display = Display() # Initializes the Display

    while True:
        Game()
def Game(): # Master Game update
    eventHandler.Update()
    display.TidyFrame()

__init__()