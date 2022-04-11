from flask_peewee.db import Model
from app.extensions import db

class BaseModelMixin(Model):
    class Meta:
        database = db


    def get_all(self, page):
        all = self.select().paginate(page, 10)

        return [i.serialize for i in all]

    def get_all_no_paginate(self):
        all = self.select()

        return [i.serialize for i in all]

    def counter(self):
        return len([i for i in self.select()])