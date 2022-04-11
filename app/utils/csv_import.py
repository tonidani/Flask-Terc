import pandas as pd
from app.utils.import_geojson import import_data_form_geojson
from app.models.commune import Commune
from app.models.voivodeship import Voivodeship
from app.models.district import District
from flask import current_app

def check_time(f):
    def count():
        from time import time
        start = time()
        f()
        end = time()
        print(f"Time to execute the {f.__name__} : {end - start}")

    return count()

@check_time
def import_data_form_csv():
        import os
        app_path = os.path.join(current_app.root_path, 'utils', 'TERC_import.csv')

        with open(app_path) as file:



            df = pd.DataFrame(pd.read_csv(file, na_values=['nan'], keep_default_na=False), columns= ['WOJ', 'POW', 'GMI', 'RODZ', 'NAZWA' , 'NAZWA_DOD'])


            #OPCJA1: sprawdzanie po patternie (nazwy) - Województwa z dużej wszystkie / powiaty wszystkie małe / gmina pierwsza duża reszta male
            #woj = [(Wojewodztwo(woj=row[0], nazwa=row[4]).save()) for i, row in df.iterrows() if row[4].isupper()]
            #powiat = [(Powiat(woj=row[0], pow=int(row[1]), nazwa=row[4]).save()) for i, row in df.iterrows() if row[4].islower()]
            #gmi = [row[2], row[3], row[4]) for i, row in df.iterrows() if row[4][0].isupper() and row[4][1:].islower()]



            #OPCJA2: momencie gdy wielkość liter w nazwie przezstanie mieć znaczenie, sprwadz nazwa_dod (mało efektowen ale bezpieczniejsza opcja niż 1)
            #woj = [(Wojewodztwo(woj=row[0], nazwa=row[4]).save()) for i, row in df.iterrows() if row[5] == 'województwo']
            #powiat = [(Powiat(woj=row[0], pow=int(row[1]), nazwa=row[4]).save()) for i, row in df.iterrows() if row[5] == 'powiat']
            #gmi = [(Gmina(gmi=row[2], rodz=row[3], nazwa=row[4]).save()) for i, row in df.iterrows() if row[3] is not None]

            #OPCJA3 (najlepsza dla mnie) sprawdznie nr pol pola woj gmi rodz zastępując puste wartość (nan) na '' - jezeli jest puste no to wiadomo co jest czym.
            
            #, bbox_minx=round(import_data_form_geojson(row[0])[1][0], 5), bbox_miny=round(import_data_form_geojson(row[0])[1][1], 5), bbox_maxx=round(import_data_form_geojson(row[0])[1][2], 5), bbox_maxy=round(import_data_form_geojson(row[0])[1][3], 5)
            voi = [(Voivodeship(name=row[4], voivodeship_number=row[0], geometry=import_data_form_geojson(row[0])[0]).save()) for i, row in df.iterrows() if ((row[1] == '') and (row[2] == '') and (row[3] == ''))]
            dist = [(District(voivodeship=int(row[0]), district_number=int(row[1]), name=str(row[4])).save()) for i, row in df.iterrows() if ((row[2] and row[3])  == '' and (row[1] != ''))]
            com = [(Commune(commune=int(row[2]), type=int(row[3]), name=str(row[4]), voivodeship=int(row[0]), district=int(row[1])).save()) for i, row in df.iterrows() if (row[3] and row[2]) != '']

            print(f'Voivodeship added to db!')
            print(f'District added to db!')
            print(f'Commune added to db!')


