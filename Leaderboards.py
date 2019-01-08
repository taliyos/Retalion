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
        this.leaderboards = Text(screen, "", screen.get_width()/2, 250, (255,255,255), 18, "Fonts/Roboto.ttf", True, False, False, False, 0, 0, 0);

    def Update(this):
        if (this.state == 0):
            this.GetName();
            this.textInput.Draw()
        elif (this.state == 1):
            file = open("leaderboards.txt", "r")
            text = file.readlines()
            times = []
            times.append(-1)
            for i in range(0, len(text)):
                textCut = str.split(text[i], ": ")
                time = str.split(textCut[1], " seconds")
                times.append(i)
            times.sort(reverse = True)
            for i in range(0, len(times)):
                if (times[i] == -1):
                    this.leaderboards.AddText(this.textInput.GetText() + ": " + str(this.time) + " seconds")
                else:
                    this.leaderboards.AddText(text[times[i]]+"")
            file.close()
            file = open("leaderboards.txt", "a")
            file.write(this.textInput.GetText() + ": " + str(this.time) + " seconds")
            file.close()
            this.state = 2
        elif (this.state == 2):
            this.leaderboards.Draw()

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