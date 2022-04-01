import uuid

class RedemtionPlace:
    def __init__(self, id, name, redeemer_id):
        self.id = uuid.uuid4().str()
        self.name = name
        self.redeemer_id = redeemer_id
        
        