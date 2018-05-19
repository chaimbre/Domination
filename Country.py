import geopandas as gpd
import numpy as np
import random
import shapely

python_rep = "C:/Prog/Domination/"

class CountryProvider:

    def __init__( self, min_area = 10 ):
        self._min_area = min_area
        self.handle = self.readFile()
        self._sel_name = ""
    
    def readFile( self ):
        tpd = gpd.read_file( python_rep + 'TM_WORLD_BORDERS_SIMPL-0.3.shp')
        pd = tpd[ tpd.area > self._min_area ]
        print( "Number of countries reduced from", tpd.size, "to", pd.size, "/n")
        return pd

    def extractPolygons( self, polygons ):
        for polygon in polygons:
            polygon = shapely.geometry.shape(polygon)
            yield from [polygon] if polygon.geom_type == 'Polygon' else polygon
           
    def getPolygon( self, country_name ):
        if country_name == "RANDOM":
            country_name = self.genRandomName()
        self._sel_name = country_name    
        country = self.handle[self.handle.NAME == country_name]
        pol = self.extractPolygons( country.geometry )
        return pol

    def genRandomName( self ):
        country_list = list(self.handle.NAME)
        return random.choice(country_list)
    
    def getSelName( self ):
        return self._sel_name     
        
