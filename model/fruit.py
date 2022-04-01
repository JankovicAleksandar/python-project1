import uuid

class Voce:
    def __init__(self, id, name):
        self.id = uuid.uuid4().str()
        self.name = name