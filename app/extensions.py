from peewee import PostgresqlDatabase
from config import Config



db = PostgresqlDatabase(Config.DB_NAME, user=Config.DB_USER, password=Config.DB_PASSWD,
                            host=Config.DB_HOST, port=Config.DB_PORT)