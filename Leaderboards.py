import pygame
from Text import *

class Leaderboards():
    def __init__(this, screen, events, time):
        ### Universal Componenets
        this.screen = screen
        this.events = events

        this.time = time
        this.state = 0
        this.textInput = Text(screen, "", screen.get_width()/2, 250, (255,255,255), 18, "Fonts/Roboto.ttf", True, False, False, False, 0, 0, 0)
        this.leaderboards = []
        for i in range(0,5):
            this.leaderboards.append(Text(screen, "", screen.get_width()/2 - 100, 250 + (25*i), (255,255,255), 18, "Fonts/Roboto.ttf", False, False, False, False, 0, 0, 0))

    def Update(this):
        if (this.state == 0):
            this.GetName();
            this.textInput.Draw()
        elif (this.state == 1):
            file = open("leaderboards.txt", "a")
            file.write("\n"+this.textInput.GetText() + ": " + str(this.time) + " seconds")
            file.close()
            file = open("leaderboards.txt", "r")
            scores = file.readlines()
            file.close()
            seperatedScores = []
            if (len(scores) < 5):
                file = open("leaderboards.txt", "a")
                file.write("\nCOMPUTER: 5 seconds")
                file.close()
            for i in range(0, len(scores)):
                textCut = str.split(scores[i], ": ")
                textCut = str.split(textCut[1], " seconds")
                seperatedScores.append((float(textCut[0]), i))
            seperatedScores.sort(reverse = True)
            for i in range(0, 5):
                this.leaderboards[i].AddText(scores[seperatedScores[i][1]])
            this.state = 2
        elif (this.state == 2):
            for i in range(0,5):
                this.leaderboards[i].Draw()

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