import os


class Config:
    SECRET_KEY = "some-key" or os.environ.get('SECRET_KEY')
    DEBUG = False
    DB_NAME = 'gis_support' or os.environ.get('DB_NAME')
    DB_HOST = 'db' or os.environ.get('DB_HOST')
    DB_PORT = 5432 or os.environ.get('DB_PORT')
    DB_USER = "postgres" or os.environ.get('DB_USER')
    DB_PASSWD = "gis_support" or os.environ.get('DB_PASSWD')

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    CACHE_PATH = os.path.join(BASE_DIR,'cache')

    DATABASE = {
        'name': DB_NAME,
        'engine': 'peewee.PostgresqlDatabase',
        'host': DB_HOST,
        'port' : DB_PORT,
        'user' : DB_USER,
        'password' : DB_PASSWD
    }

    template = {
        "title": "Sample TERC IMPORT API",
        "doc_dir": '. / app / api / docs /',
        "description": "This is a sample API to see information about territorial organization in Poland.",
        "contact": {
            "name": "Toni Rodriguez",
            "email": "tonidani@gmail.com"
        },

        "version": "1.0.1"
    }

    template_folder = os.path.abspath('app/front/templates')


