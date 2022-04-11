from app.models import BaseModelMixin
from flask_peewee.db import CharField, IntegerField, ForeignKeyField
from app.models.voivodeship import Voivodeship

class District(BaseModelMixin):
    name = CharField()
    voivodeship = ForeignKeyField(Voivodeship, field='voivodeship_number')
    district_number = IntegerField()

    def __str__(self):
        return f'Powiat: {self.name}, Województwo: {self.voivodeship.name} '

    def __repr__(self):
        return f'Województwo: {self.voivodeship.name} , Powiat: {self.name}'



    def search_by_voivodeship_and_paginate(self, page, arg):

        query = self.select().where(self.voivodeship == arg).paginate(page, 10)

        return [i.serialize for i in query]


    def search_by_voivodeship(self, arg):

        query = self.select().where(self.voivodeship == arg)

        return [i.serialize for i in query]

    @staticmethod
    def voi_with_max_dist():


        qr = District.select(District.voivodeship, fn.COUNT(District.district_number)).group_by(District.voivodeship_id).order_by(fn.COUNT(District.district_number).desc())


        return qr[0].voivodeship.name







    @property
    def serialize(self):
        data = {
            'id': self.id,
            'nazwa' : self.name,
            'woj' : self.voivodeship_id,
            'pow' : self.district_number
        }
        return data