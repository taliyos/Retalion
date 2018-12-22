from enum import Enum

class Command(Enum):
    LevelChange = 0


def CommandHandler(levelManager, command, commandParameter):
    if (command == Command.LevelChange):
        levelManager.SetWindow(commandParameter)