from flask import current_app
import json

def convert_to_wkb(coordinates):
    from shapely.geometry import shape

    geom = shape(coordinates)


    return geom.wkb, geom.bounds


def import_data_form_geojson(voivodeship_code : int):
        import os
        #app_path = os.path.join(current_app.root_path, 'utils', 'voivodeship_3857.geojson')
        app_path = os.path.join(current_app.root_path, 'utils', 'voivodeship.geojson')
        file = open(app_path)
        geojson = json.load(file)


        for features in geojson['features']:
           for key, value in features["properties"].items():
                if key == 'JPT_KOD_JE' and int(value) == int(voivodeship_code):
                #if key == 'cartodb_id' and int(value) == int(voivodeship_code):
                    return convert_to_wkb(features['geometry'])
