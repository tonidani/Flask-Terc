from app.models.voivodeship import Voivodeship
from app.models.district import District
from app.models.commune import Commune


def test_create_tables(transaction):
    Voivodeship.create_table()
    District.create_table()
    Commune.create_table()

def test_import_data(transaction):
    pass