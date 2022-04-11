from app.models import *
from flask_peewee.db import CharField, IntegerField, fn, DecimalField
from app.models.custom_fields import GeometryField

class Voivodeship(BaseModelMixin):
    name = CharField()
    voivodeship_number = IntegerField(unique=True)
    geometry = GeometryField()
    #bbox_minx = DecimalField()
    #bbox_miny = DecimalField()
    #bbox_maxx = DecimalField()
    #bbox_maxy = DecimalField()

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

    def serialize_geometry(self):
        import geojson
        import json
        return json.loads(geojson.dumps(self.geometry))


