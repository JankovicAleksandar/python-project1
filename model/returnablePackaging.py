import uuid

class ReturnablePackaging:
    def __init__(self, id, fruit_producer_id, quantity_of_indebted_packaging, quantity_of_packaging_returned):
        self.id = uuid.uuid4().str()
        self.fruit_producer_id = fruit_producer_id
        self.quantity_of_indebted_packaging = quantity_of_indebted_packaging
        self.quantity_of_packaging_returned = quantity_of_packaging_returned