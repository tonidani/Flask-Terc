import os
class Config:
    SECRET_KEY = "some-key" or os.environ.get('SECRET_KEY')
    DEBUG = False
    DB_NAME = 'gis_support' or os.environ.get('DB_NAME')
    DB_HOST = '172.18.0.2' or os.environ.get('DB_HOST')
    DB_PORT = 5432 or os.environ.get('DB_PORT')
    DB_USER = "postgres" or os.environ.get('DB_USER')
    DB_PASSWD = "gis_support" or os.environ.get('DB_PASSWD')

    TESTING = False

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



