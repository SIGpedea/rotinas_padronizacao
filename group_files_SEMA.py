#!/usr/bin/env python3
import geopandas as gpd
from glob import glob
import numpy as np
import os
import shutil

'''




'''

shps = glob('*.shp')


for i in shps:
	fname = i.split('.')[0]
	files = glob(fname + '*')
	os.mkdir(fname)
	for j in files:
		shutil.move(j, fname)