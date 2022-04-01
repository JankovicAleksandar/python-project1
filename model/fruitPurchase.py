from re import S
import uuid

class FruitPurchase:
    def __init__(self, id, redemtion_place_id, fruit_producer_id, fruit_id, returnable_packaging_id, first_class_quantity, second_class_quantity, third_class_quantity):
        self.id = uuid.uuid4().str()
        self.redemtion_place_id = redemtion_place_id
        self.fruit_producer_id = fruit_producer_id
        self.fruit_id = fruit_id
        self.returnable_packaging_id = returnable_packaging_id
        self.first_class_quantity = first_class_quantity
        self.second_class_quantity = second_class_quantity
        self.third_class_quantity = third_class_quantity
        