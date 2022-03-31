import uuid

class FruitPurchase:
    def __init__(self, id, redemtion_place_id, fruit_producer_id, fruit_id, returnable_packaging_id):
        self.id = uuid.uuid4().str()
        self.redemtion_place_id = redemtion_place_id
        self.fruit_producer_id = fruit_producer_id
        self.fruit_producer_id
        self.returnable_packaging_id = returnable_packaging_id
        