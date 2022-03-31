import uuid

class Cena:
    def __init__(self, first_class_price, second_class_price, third_class_price, redemtion_place_id, fruit_id):
        self.id = uuid.uuid4().str()
        self.first_class_price = first_class_price
        self.second_class_price = second_class_price
        self.third_class_price = third_class_price
        self.redemtion_place_id = redemtion_place_id
        self.fruit_id = fruit_id
