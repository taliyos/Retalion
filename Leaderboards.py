import pygame
from Text import *

class Leaderboards():
    def __init__(this, screen, events, time):
        ### Universal Componenets
        this.screen = screen
        this.events = events

        this.time = time
        this.state = 0
        this.textInput = Text(screen, "_", screen.get_width()/2, 250, (255,255,255), 18, "Fonts/Roboto.ttf", True, False, False, False, 0, 0, 0);

    def Update(this):
        if (this.state == 0):
            this.GetName();
            this.textInput.Draw()
        elif (this.state == 1):
            file = open("leaderboards.txt", "a")
            text = file.readlines()
            file.write(this.textInput.GetText() + ": " + str(this.time) + " seconds\n")
            file.close()
            this.state = 0

    def GetName(this):
        if (this.events.key != -1):
            if (len(this.textInput.GetText()) > 0 and this.events.key.key == 13):
                this.state = 1
                print("DONE")
            if (this.events.key.unicode == ' '):
                return
            elif (this.events.key.key == 8):
                this.textInput.RemoveLetter()
            elif(len(this.textInput.GetText()) < 7 and this.events.key.key != 13):
                this.textInput.AddText(this.events.key.unicode)