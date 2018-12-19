import math

class Transitions():
    """Library of transititons"""
    @staticmethod
    def FadeInLeft(x, desiredX, speed): # Handles fading from left or top down
        if (x < desiredX):
            x += speed
        elif (x > desiredX):
            x = desiredX
        return x

    @staticmethod
    def FadeInRight(x, desiredX, speed): # Handles fading from right or bottom up
        if (x > desiredX):
            x -= speed
        elif (x < desiredX):
            x = desiredX
        return x

    @staticmethod
    def FadeInColor(color, desiredColor, speed): # Handles fading colors from black to the desired color
        colorList = list(color)
        for i in range(len(colorList)):
            if (colorList[i] < desiredColor[i]):
                colorList[i] += speed

        return tuple(colorList)

    @staticmethod
    def WaveIn(x, desiredX, speed):
        return -100*math.sin(speed/100) + desiredX