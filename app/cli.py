from flask.cli import with_appcontext, current_app
import click
from app.models.voivodeship import *
from app.models.commune import *
from app.models.district import *

@click.command(name='create_tables')
@with_appcontext
def create_tables():
    ' Create db if does not exist '
    try:
        Voivodeship.create_table()
        District.create_table()
        Commune.create_table()
        print('db created!')
    except:
        print('tables already in db')


@click.command(name='create_admin')
@with_appcontext
def create_admin():
    'Create admin user from flask.peewee admin and auth -> DEFAULT PASSWORD is admin'

    admin = current_app.auth.User(username='admin', email='', admin=True, active=True)
    admin.set_password('admin')
    admin.save()


@click.command(name='import_data')
@with_appcontext
def import_data():
    'import data from TERC file'

    from .utils.csv_import import import_data_form_csv
    import_data_form_csv()

