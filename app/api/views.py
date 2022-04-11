
from app.models import voivodeship
from .errors import *
from app.models.voivodeship import Voivodeship
from app.models.commune import Commune
from app.models.district import District
from app.utils.mvt import MvtTile


from flask import jsonify, request, abort, make_response
from flask.views import MethodView

from flasgger import swag_from



class VoivodeshipsView(MethodView):
    def get(self, page=1):
        """
        Get a list of Voivodeships in Poland

        ---
        tags:
          - wojewodztwa



        components:
          schemas:
            User:
              properties:
                id:
                  type: integer
                name:
                   type: string

        parameters:
          - name: page
            in: path
            type: integer
            required: false
            description: Numer of the paginated resource

        definitions:
          Voivodeship:
            type: object
            properties:
              id:
                type: integer
              name:
                type: string
              woj:
                type: integer

          Error:
              type: object
              properties:
                 error:
                    type: string
                 url :
                    type: string
                 status_code:
                    type: integer


        responses:
          200:
            description: Returns a list of voivodeships
            schema:
                type: array
                items:
                    $ref: '#/definitions/Voivodeship'

          400:
            description: errors
            schema:
                type: array
                items:
                    $ref: '#/definitions/Error'

        """


        result = Voivodeship.get_all(Voivodeship, page)
        all = Voivodeship.counter(Voivodeship)
        if result:
            res = jsonify(
                {
                    "count" : all ,
                    "województwa" : result,
                    'meta' : {
                        'strona' : page,
                        'ile_na_stronę' : 10,
                        'ilość_stron' : round(all/10),
                        'adres_strony' : request.url
                    }
                }
            )

            res.status_code = 200

        else:
            abort(404)

        return res


class VoivodeshipsGeoIntView(MethodView):
    def get(self, id):
        """
        Get a list of Voivodeships in Poland

        ---
        tags:
          - wojewodztwa



        components:
          schemas:
            User:
              properties:
                id:
                  type: integer
                name:
                   type: string

        parameters:
          - name: page
            in: path
            type: integer
            required: false
            description: Numer of the paginated resource

        definitions:
          Voivodeship:
            type: object
            properties:
              id:
                type: integer
              name:
                type: string
              woj:
                type: integer

          Error:
              type: object
              properties:
                 error:
                    type: string
                 url :
                    type: string
                 status_code:
                    type: integer


        responses:
          200:
            description: Returns a list of voivodeships
            schema:
                type: array
                items:
                    $ref: '#/definitions/Voivodeship'

          400:
            description: errors
            schema:
                type: array
                items:
                    $ref: '#/definitions/Error'

        """


        result = Voivodeship.select().where(Voivodeship.voivodeship_number == id).get()


        
        if result:
            res = jsonify(
                {
                  "type": "FeatureCollection",
                  "name": str(result.name),
                  "crs": { "type": "name", "properties": { "name": "urn:ogc:def:crs:EPSG::3857" } },
                  "features": 
                  [
                    { "type": "Feature", "properties": 
                      { "JPT_KOD_JE" : str(id)},
                        'geometry': result.serialize_geometry()
                      
                    }
                  ]
                }
                  
            )

            res.status_code = 200

        else:
            abort(404)
        

        return res


class VoivodeshipsGeoView(MethodView):
    def get(self):
        """
        Get a list of Voivodeships in Poland

        ---
        tags:
          - wojewodztwa



        components:
          schemas:
            User:
              properties:
                id:
                  type: integer
                name:
                   type: string

        parameters:
          - name: page
            in: path
            type: integer
            required: false
            description: Numer of the paginated resource

        definitions:
          Voivodeship:
            type: object
            properties:
              id:
                type: integer
              name:
                type: string
              woj:
                type: integer

          Error:
              type: object
              properties:
                 error:
                    type: string
                 url :
                    type: string
                 status_code:
                    type: integer


        responses:
          200:
            description: Returns a list of voivodeships
            schema:
                type: array
                items:
                    $ref: '#/definitions/Voivodeship'

          400:
            description: errors
            schema:
                type: array
                items:
                    $ref: '#/definitions/Error'

        """


        result = Voivodeship.select()
        if result:

          temp_list = [{ "type": "Feature", "properties": { "JPT_KOD_JE" : str(voivodeship.voivodeship_number)}, "geometry": voivodeship.serialize_geometry() } for voivodeship in result]

          res = jsonify({
                  "type": "FeatureCollection",
                  "name": "Voivodeships",
                  "crs": { "type": "name", "properties": { "name": "urn:ogc:def:crs:EPSG::3857" } },
                  'features': temp_list
                })



          res.status_code = 200

        else:
            abort(404)
        

        return res

class VoivodeshipTilesView(MethodView):
  def get(self, z=0, x=0, y=0):
    mvt_tile = MvtTile(z, x, y)

    if mvt_tile.get_mvt_coordinates() is not None:
      response = make_response(mvt_tile.get_mvt_coordinates())
      response.headers['Content-Type'] = "application/octet-stream"
    else:
      response = make_response('no tile', 204)
    
    return response

class DistrictsView(MethodView):
    def get(self, page=1):
        """
        Get a list of Districts in Poland

        ---
        tags:
          - powiaty

        parameters:
          - in: query
            name: woj
            type: integer
            required: false
            description: Numeric ID of the Voivodeship based in TERC numerology
          - in: path
            name: page
            type: integer
            required: false
            description: Numer of the paginated resource



        components:
          schemas:
            User:
              properties:
                id:
                  type: integer
                name:
                   type: string

        definitions:
          District:
            type: object
            properties:
              id:
                type: integer
              name:
                type: string
              woj:
                type: integer
              pow:
                type: integer

          Error:
              type: object
              properties:
                 error:
                    type: string
                 url :
                    type: string
                 status_code:
                    type: integer


        responses:
          200:
            description: Returns a list of Districts in poland
            schema:
                type: array
                items:
                    $ref: '#/definitions/District'

          400:
            description: errors
            schema:
                type: array
                items:
                    $ref: '#/definitions/Error'

        """


        if request.args.get('woj', type=int) and len(request.args) == 1:

            result = District.search_by_voivodeship_and_paginate(District, page, request.args.get('woj'))
            all = len(District.search_by_voivodeship(District, request.args.get('woj')))

        elif len(request.args) == 0:

            result = District.get_all(District, page)
            all = District.counter(District)


        else:
            abort(400)

        if result:
            res = jsonify(
                {
                    "count": all,
                    "powiaty": result,
                    'meta': {
                        'strona': page,
                        'ilość_stron': round(all / 10),
                        'ile_na_stronę': 10,
                        'adres_strony': request.url
                    }
                }
            )

            res.status_code = 200

        else:
            abort(404)


        return res


class CommuneView(MethodView):
    def get(self, page=1):
        """
                Get a list of Communes in Poland

                ---
                tags:
                  - gminy

                parameters:
                  - in: query
                    name: woj
                    type: integer
                    required: false
                    description: Numeric ID of the Voivodeship based in TERC numerology
                  - in: query
                    name: pow
                    type: integer
                    required: false
                    description: Numeric ID of the District based in TERC numerology



                components:
                  schemas:
                    User:
                      properties:
                        id:
                          type: integer
                        name:
                           type: string

                definitions:
                  Commune:
                    type: object
                    properties:
                      id:
                        type: integer
                      name:
                        type: string
                      woj:
                        type: integer
                      pow:
                        type: integer
                      rodz:
                         type: integer

                  Error:
                      type: object
                      properties:
                         error:
                            type: string
                         url :
                            type: string
                         status_code:
                            type: integer


                responses:
                  200:
                    description: Returns a list of Communes in poland
                    schema:
                        type: array
                        items:
                            $ref: '#/definitions/Commune'

                  400:
                    description: errors
                    schema:
                        type: array
                        items:
                            $ref: '#/definitions/Error'

                """

        if request.args.get('woj', type=int) and request.args.get('pow', type=int) and len(request.args) == 2:
            result = Commune.search_by_voivodeship_and_district_paginate(Commune, page, request.args.get('woj'), request.args.get('pow'))
            all = len(Commune.search_by_voivodeship_and_district(Commune, request.args.get('woj'), request.args.get('pow')))


        elif (request.args.get('woj', type=int) and not request.args.get('pow', type=int)) and len(request.args) == 1:
            result = Commune.search_by_voivodeship_and_paginate(Commune, page, request.args.get('woj'))
            all = len(Commune.search_by_voivodeship(Commune, request.args.get('woj')))



        elif (request.args.get('pow', type=int) and not request.args.get('woj', type=int)) and len(request.args) == 1:
            result = Commune.search_by_district_and_paginate(Commune, page, request.args.get('pow'))
            all = len(Commune.search_by_district(Commune, request.args.get('pow')))


        elif len(request.args) == 0:
            result = Commune.get_all(Commune, page)
            all = Commune.counter(Commune)


        else:
            abort(400)

        if result:
            res = jsonify(
                {
                    "count": all,
                    "powiaty": result,
                    'meta': {
                        'strona': page,
                        'ile_na_stronę': 10,
                        'ilość_stron': round(all / 10),
                        'adres_strony': request.url
                    }
                }
            )

            res.status_code = 200
        else:
            abort(404)

        return res


class StatsView(MethodView):
    def get(self):

        res = jsonify(
                {
                    "woj_count": Voivodeship.counter(Voivodeship),
                    "pow_count": District.counter(District),
                    'gmi_count': Commune.counter(Commune),
                    'woj_name_max_pow' : District.voi_with_max_dist(),
                    'woj_name_max_gmi': Commune.voi_with_max_comm(),
                    'pow_name_max_gmi': Commune.dist_with_max_comm()
                }
            )

        res.status_code = 200


        return res



api_v1.add_url_rule('/wojewodztwa', view_func=VoivodeshipsView.as_view('voivodeships'))

api_v1.add_url_rule('/wojewodztwa/geo', view_func=VoivodeshipsGeoView.as_view('voivodeships_geo'))
api_v1.add_url_rule('/wojewodztwa/geo/<int:id>', view_func=VoivodeshipsGeoIntView.as_view('voivodeships_geo_int'))

api_v1.add_url_rule('/wojewodztwa/tiles', view_func=VoivodeshipTilesView.as_view('voivodeships_tiles'))
api_v1.add_url_rule('/wojewodztwa/tiles/<int:z>/<int:x>/<int:y>', view_func=VoivodeshipTilesView.as_view('voivodeships_tiles_args'))


api_v1.add_url_rule('/wojewodztwa/<int:page>', view_func=VoivodeshipsView.as_view('voivodeships_page'))

api_v1.add_url_rule('/powiaty', view_func=DistrictsView.as_view('districts'))
api_v1.add_url_rule('/powiaty/<int:page>', view_func=DistrictsView.as_view('districts_page'))

api_v1.add_url_rule('/gminy', view_func=CommuneView.as_view('commune'))
api_v1.add_url_rule('/gminy/<int:page>', view_func=CommuneView.as_view('commune_page'))

api_v1.add_url_rule('/stats', view_func=StatsView.as_view('stats'))
