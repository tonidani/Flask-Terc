from app.models import *


class Voivodeship(BaseModelMixin):
    name = CharField()
    voivodeship_number = IntegerField(unique=True)

    def __str__(self):
        return f'Województwo: {self.name} , Numer_woj: {self.voivodeship_number}'

    def __repr__(self):
        return f'Województwo: {self.name} , Numer_woj: {self.voivodeship_number}'

    @property
    def serialize(self):
        data = {
            'id': self.id,
            'nazwa' : self.name,
            'woj' : self.voivodeship_number
        }
        return data
