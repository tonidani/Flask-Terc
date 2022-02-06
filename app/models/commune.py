from app.models import *
from app.models.voivodeship import Voivodeship
from app.models.district import District


class Commune(BaseModelMixin):
    name = CharField()
    voivodeship = ForeignKeyField(Voivodeship, field='voivodeship_number')
    district = IntegerField()
    commune = IntegerField()
    type = IntegerField()


    def __str__(self):
        return f'Gmina: {self.name}, Rodz : {self.type}, Województwo: {self.voivodeship.name} , Powiat: {self.district}'

    def __repr__(self):
        return f'Województwo: {self.voivodeship.name} , Powiat: {self.district}, Gmina: {self.name}, Rodz : {self.type}'

    @property
    def serialize(self):
        data = {
            'id': self.id,
            'nazwa' : self.name,
            'woj' : self.voivodeship_id,
            'pow' : self.district,
            'gmi' : self.commune,
            'rodz' : self.type
        }
        return data


    def search_by_voivodeship_and_district_paginate(self, page, voi, dis):

        query = self.select().where(self.voivodeship == voi, self.district == dis).paginate(page, 10)

        return [i.serialize for i in query]

    def search_by_voivodeship_and_district(self, voi, dis):

        query = self.select().where(self.voivodeship == voi, self.district == dis)

        return [i.serialize for i in query]


    def search_by_voivodeship_and_paginate(self, page, voi):

        query = self.select().where(self.voivodeship == voi).paginate(page, 10)

        return [i.serialize for i in query]

    def search_by_voivodeship(self, voi):

        query = self.select().where(self.voivodeship == voi)

        return [i.serialize for i in query]


    def search_by_district_and_paginate(self, page, dis):

        query = self.select().where(self.district == dis).paginate(page, 10)

        return [i.serialize for i in query]

    def search_by_district(self, dis):

        query = self.select().where(self.district == dis)

        return [i.serialize for i in query]

    @staticmethod
    def voi_with_max_comm():
        qr = Commune.select(Commune.voivodeship, fn.COUNT(Commune.commune)).group_by(
            Commune.voivodeship_id).order_by(fn.COUNT(Commune.commune).desc())

        return qr[0].voivodeship.name

    @staticmethod
    def dist_with_max_comm():
        qr = Commune.select(Commune.district, fn.COUNT(Commune.commune)).group_by(
            Commune.district).order_by(fn.COUNT(Commune.commune).desc())

        dist = District.select().where(District.district_number == qr[0].district)

        return dist[0].name




