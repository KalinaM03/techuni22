class CharacterExists(Exception):
    def __init__(self, message):
        self.message=message


class InvalidDataFormat(Exception):
    def __init__(self, message):
        self.message=message


class InvalidCommand(Exception):
    def __init__(self, message):
        self.message = message

