#!/usr/bin/env python3
import geopandas as gpd
from glob import glob
import numpy as np
import pandas as pd
import geocoder
import difflib
from geopy.geocoders import Nominatim
from fuzzywuzzy import process, fuzz



geolocator = Nominatim(user_agent="MyApp")


# shp = glob('*.shp')[0]

geocod = pd.read_table('/home/calixtops/Documents/dash-apps/geo_utils/geocod_ibge.csv', sep=';')
erro =[]
shp = '/home/calixtops/Documents/PEA-PEDEA-NEWPHASE/SEMACE_ATUALIZACAO_201123/termo_embargo_poligono_2012-2022/termo_embargo_poligono_2012-2022.shp'


data_shape = gpd.read_file(shp,crs='4674')

a = []
b = []
for index, row in data_shape.iterrows(): 

		i_city = '{}, Ceará'.format(row['MUNICIPIO'])


		if (row['MUNICIPIO'] == 'Pacatuba/CE') or (row['MUNICIPIO'] == 'Sao Goncalo do Amarante'):
			inf_city = geocoder.osm(i_city).town
		else:
			inf_city = geocoder.osm(i_city).municipality

		if inf_city == None:

			inf_city = geocoder.osm(i_city).city
		if inf_city == None:
			inf_city = geocoder.osm(i_city).village

		print('-------------------------------------------------')
		print(row['MUNICIPIO'])
		print(inf_city)
		print('-------------------------------------------------')
		try:
			a.append(geocod[geocod['municipio2'] == inf_city].geocodigo.values[0])
			b.append(inf_city)
		except:
			a.append(geocod[geocod['municipio2'] == row['MUNICIPIO']].geocodigo.values[0])
			b.append(row['MUNICIPIO'])
			print('ATENCAAAAO')


data_shape['geocodigo'] = a

data_shape.to_file(shp,driver='ESRI Shapefile',encoding='UTF-8',index = True, crs="EPSG:4674")
