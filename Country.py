import geopandas as gpd
import numpy as np
import random
import shapely
import triangle

class CountryProvider:

    def __init__( self, min_area = 10 ):
        self._min_area = min_area
        self.handle = self.readFile()
        self._sel_name = ""
    
    def readFile( self ):
        tpd = gpd.read_file('C:/Prog/Domination/TM_WORLD_BORDERS_SIMPL-0.3.shp')
        pd = tpd[ tpd.area > self._min_area ]
        print( "number of countries reduced from", tpd.size, "to", pd.size )
        return pd

    def extractPolygons( self, polygons ):
        for polygon in polygons:
            polygon = shapely.geometry.shape(polygon)
            #poltri = shapely.ops.triangulate(polygon)
            print( "triangle size " + (str)(len(poltri)) )

            c = list(polygon.exterior.coords)
            v = np.array(c)
            i = list(range(len(c)))
            s = np.array(list(zip(i, i[1:] + [i[0]])))
            poltri = triangle.triangulate(tri={'vertices': v, 'segments':s},
                            opts='pq20')
            return poltri
            #(poltri,yield from [polygon] if polygon.geom_type == 'Polygon' else polygon)
            #yield from [poltri] if polygon.geom_type == 'Polygon' else polygon
            

    def getPolygon( self, country_name ):
        if country_name == "RANDOM":
            country_name = self.genRandomName()
        self._sel_name = country_name    
        country = self.handle[self.handle.NAME == country_name]
        pol = self.extractPolygons( country.geometry )
        #poltri = self.extractPolygonsTriangles( country.geometry )
        return pol

    def genRandomName( self ):
        country_list = list(self.handle.NAME)
        nr_country = len(country_list)
        sel_nr = random.randint( 0, nr_country-1 )
        print( sel_nr )
        print( len(country_list) )
        return country_list[sel_nr]
    
    def getSelName( self ):
        return self._sel_name     
        
