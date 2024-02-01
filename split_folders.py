#!/usr/bin/env python3
from pathlib import Path
from glob import glob
import os
import shutil

for i in glob('*/*/*'):

	print(i)

	shp_folder = i.split('/')[-1]
	root_folder = i.split(shp_folder)[0]


	slds = glob(root_folder + '*/*.sld')
	docs = glob(root_folder + '*/*.doc*') + glob(root_folder + '*/*.txt*') 
	exep = slds + docs 

	shps = 	glob(root_folder + '*/*')

	shps = [x for x in shps if x not in exep]

	if os.path.exists(root_folder + 'SLD') == False:

		os.makedirs(root_folder + 'SLD')
		os.makedirs(root_folder + 'DOCS')
		os.makedirs(root_folder + 'SHP')


	for sld in slds:
		Path(sld).rename(root_folder + 'SLD/' + sld.split('/')[-1])
	for doc in docs:
		Path(doc).rename(root_folder + 'DOCS/' + doc.split('/')[-1])
	for shp in shps:
		Path(shp).rename(root_folder + 'SHP/' + shp.split('/')[-1])




# paths = glob('*/*/12*')


# for path in paths:
# 	shutil.rmtree(path)
