#!/usr/bin/env python3
import geopandas as gpd
from glob import glob
import numpy as np
import pandas as pd
import geocoder
import difflib
import reverse_geocoder as rg
from geopy.geocoders import Nominatim
import difflib



geolocator = Nominatim(user_agent="MyApp")


shp = glob('*.shp')[0]

geocod = pd.read_table('/home/calixtops/Downloads/1201_zoneamentos/municipios.csv', sep=';')
erro =[]


data_shape = gpd.read_file(shp,crs='4674')

print('--------------------------------------------')
print('')
print('Lendo o arquivo --->' + shp)
print('')
print('--------------------------------------------')

data_shape['LAT']=data_shape.geometry.y

data_shape['LON']=data_shape.geometry.x

a = []
b = []

for mm in data_shape['MUNICIPIO']: 
	mm_table = difflib.get_close_matches(mm, geocod['Municipio2'])[0]
	geocodigo = geocod[geocod['Municipio2'] == mm_table].Codigo.values[0]
	b.append(geocodigo)




data_shape['IBGE_COD'] = b


data_shape.to_file(shp,driver='ESRI Shapefile',encoding='UTF-8',index = False, 
					crs="EPSG:4674")


print('Arquivo salvo!')

