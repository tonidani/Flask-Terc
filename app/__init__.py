from flask import Flask
from peewee import *
from config import Config
from .extensions import db
from flask_peewee.db import Database
from flask_peewee.auth import Auth
from flask_peewee.admin import Admin
from flasgger import Swagger

from app.models.voivodeship import Voivodeship
from app.models.commune import Commune
from app.models.district import District


def create_app(Config, testing=True):

    app = Flask(__name__)

    if testing is False:
        app.config.from_object(Config)
    else:
        Config.TESTING = True
        Config.DEBUG = True
        app.config.from_object(Config)


    swagger = Swagger(app, template= Config.template)
    db = Database(app)


    #auth = Auth(app, db)
    #admin = Admin(app, auth)
    #auth.User.create_table(fail_silently=True)
    #admin_usr = auth.User(username='admin', email='', admin=True, active=True)
    #admin_usr.set_password('admin')
    #admin_usr.save()
    #admin.register(Voivodeship)
    #admin.register(Commune)
    #admin.register(District)
    #admin.setup()


    from app.api.views import api_v1
    app.register_blueprint(api_v1, url_prefix='/v1/api')


    from app import cli
    app.cli.add_command(cli.create_tables)
    app.cli.add_command(cli.import_data)

    return app


