from builtins import float
import math
from app.extensions import db
from peewee import fn, Cast, query_to_string
from psycopg2.sql import Literal
import os
from app.models.voivodeship import Voivodeship
from config import Config



class MvtTile:


    
    def __init__(self, x, y, z):
        self.x = x
        self.y= y
        self.z = z
        #self.xmin: float = float(MvtTile.get_tile(self.x, self.y, self.z)[0])
        #self.ymin: float = float(MvtTile.get_tile(self.x, self.y, self.z)[1])
        #self.xmax: float = float(MvtTile.get_tile(self.x + 1, self.y + 1, self.z)[0])
        #self.ymax: float = float(MvtTile.get_tile(self.x + 1, self.y + 1, self.z)[1])
        self.tilefolder = "{}/{}/{}".format(Config.CACHE_PATH, self.z, self.x)
        self.tilepath = "{}/{}.pbf".format(self.tilefolder, self.y)
    '''
    @staticmethod
    def get_tile(x, y, z):
        n = 2.0 ** z
        lon_deg = x / n * 360.0 - 180.0
        lat_rad = math.atan(math.sinh(math.pi * (1 - 2 * y / n)))
        lat_deg = math.degrees(lat_rad)
        return  abs(lon_deg), abs(lat_deg)
    '''
    


    def get_mvt_coordinates(self):

        if not os.path.exists(self.tilepath):

            query3 = f'''
            SELECT ST_AsMVT(tile) FROM (SELECT id, name, 
            ST_AsMVTGeom(geometry, ST_transform( tilebbox({self.z}, {self.x}, {self.y}),3857), 4096, 256, false) AS geom FROM voivodeship) AS tile;'''

            query2 = f'''
            SELECT ST_AsMVT(tile) FROM (SELECT id, name, 
            ST_AsMVTGeom(geometry, 
            ST_Makebox2d(
                ST_transform(
                    ST_SetSrid(ST_MakePoint(%s,%s),4326)
                        ,3857),
                    ST_transform(
                        ST_SetSrid(ST_MakePoint(%s,%s),4326)
                        ,3857)
                        ), 4096, 256, false) AS geom FROM voivodeship
                        WHERE geometry &&
                        ST_transform(ST_MakeEnvelope(%s, %s, %s, %s, 4326),3857)
                        AND ST_Intersects(geometry, ST_transform(ST_MakeEnvelope(%s, %s, %s, %s, 4326),3857))) AS tile;'''

            query = f'''
            SELECT ST_AsMVT(tile) FROM (SELECT id, name, 
            ST_AsMVTGeom(geometry, 
            ST_Makebox2d(
                ST_transform(
                    ST_SetSrid(ST_MakePoint(%s,%s),4326)
                        ,3857),
                    ST_transform(
                        ST_SetSrid(ST_MakePoint(%s,%s),4326)
                        ,3857)
                        ), 4096, 256, false) AS geom FROM voivodeship) AS tile;'''


            #bbox = [self.xmin, self.ymin, self.xmax, self.ymax]

            

            

            #sql = db.execute_sql(gr, (self.xmin, self.ymin, self.xmax, self.ymax,self.xmin, self.ymin, self.xmax, self.ymax,self.xmin, self.ymin, self.xmax, self.ymax))
            
            #Każda możliwa opcja query sql daje ten sam efektu

            tiles_query = Voivodeship.select(
                Voivodeship.id, Voivodeship.name, 
                fn.ST_AsMVTGeom(
                    Voivodeship.geometry,
                    fn.TileBBox(self.z,self.x,self.y, 3857),
                    4096, 50, "true"))

            sql = "SELECT ST_AsMVT(tile) FROM ({}) as tile;".format(query_to_string(tiles_query))
            query = db.execute_sql(sql)
            tile = query.fetchone()[0]
            if not tile:
                return None
            tile_bytes = tile.tobytes()

            if not os.path.exists(self.tilefolder):
                os.makedirs(self.tilefolder)
            with open(self.tilepath, 'wb') as f:
                f.write(tile)
                f.close()
            
            

        tile_bytes = open(self.tilepath, 'rb').read()
        
        return tile_bytes
        
        
            

