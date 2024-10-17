class Message():
    def __init__(self, message:str = "Standard Message"):
        self.message = message

    def __str__(self):
        return self.message
