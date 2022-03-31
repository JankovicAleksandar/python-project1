import uuid

class FruitProducer:
    def __init__(self, id, name, last_name, umcn, phone_number, tax_return_statement, ugovor, plot_area, running_account, redemtion_place_id):
        self.id = uuid.uuid4().str()
        self.name = name
        self.last_name = last_name
        self.umcn = umcn
        self.phone_number = phone_number
        self.tax_return_statement = tax_return_statement
        self.ugovor = ugovor
        self.plot_area = plot_area
        self.running_account = running_account
        self.redemtion_place_id = redemtion_place_id

"umcn - Unique Master Citizen Number = jedinstveni maticni broj gradjanina"
