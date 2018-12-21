from enum import Enum

class Command(Enum):
    LevelChange = 0


def CommandHandler(command, commandParameter):
    if (command == Command.LevelChange):
        print("Command issued")
