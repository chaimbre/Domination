import geopandas as gpd

country = gpd.read_file('C:/Prog/Domination/TM_WORLD_BORDERS_SIMPL-0.3.shp')

france = country[country.NAME == 'France']

france.plot()

