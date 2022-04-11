from flask_peewee.db import Field, fn
from shapely import wkb



class GeometryField(Field):
    field_type = 'geometry'

    def db_value(self, value):
        return fn.ST_GeomFromWKB(value, 3857)

    def python_value(self, value):
        return wkb.loads(value, hex=True)

