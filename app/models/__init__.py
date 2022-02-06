from flask_peewee.db import *
from ..extensions import db

class BaseModelMixin(Model):
    class Meta:
        database = db


    def get_all(self, page):
        all = self.select().paginate(page, 10)

        return [i.serialize for i in all]

    def counter(self):
        return len([i for i in self.select()])