import geopandas as gpd
import numpy as np
import random
import shapely

python_rep = "C:/Prog/Domination/"

class CountryProvider:

    def __init__(self, min_area = 10):
        self._min_area = min_area
        self.handle = self.readFile()
        self._sel_name = ""
    
    def readFile( self ):
        tpd = gpd.read_file( python_rep + 'TM_WORLD_BORDERS_SIMPL-0.3.shp')
        pd = tpd[tpd.area > self._min_area]
        print( "Number of countries reduced from", tpd.size, "to", pd.size )
        return pd

    def extractPolygons(self, polygons):
        for polygon in polygons:
            polygon = shapely.geometry.shape(polygon)
            yield from [polygon] if polygon.geom_type == 'Polygon' else polygon
           
    def getPolygon(self, country_name="RANDOM"):
        if country_name == "RANDOM":
            country_name = self.genRandomName()
        self._sel_name = country_name    
        country = self.handle[self.handle.NAME == country_name]
        return self.extractPolygons( country.geometry )

    def getAllNames(self):
        return list(self.handle.NAME)
    
    def genRandomName(self):
        return random.choice(self.getAllNames())

    def getSelName(self):
        return self._sel_name     
        
