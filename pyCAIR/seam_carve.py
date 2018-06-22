import os
import numpy as np
from scipy.ndimage import rotate
from scipy.ndimage.filters import convolve
from tqdm import trange

from pyCAIR.helpers import writeImage as wI
from pyCAIR.helpers import createFolder as cF
from pyCAIR.helpers import writeImage as wI
from pyCAIR.helpers import writeImageG as wIG

def getEnergy(image):
	
	filter_x = np.array([
		[1.0, 2.0, 1.0],
		[0.0, 0.0, 0.0],
		[-1.0, -2.0, -1.0],
		])

	filter_x = np.stack([filter_x] * 3, axis = 2)

	filter_y = np.array([
		[1.0, 0.0, -1.0],
		[2.0, 0.0, -2.0],
		[1.0, 0.0, -1.0],
		])

	filter_y = np.stack([filter_y] * 3, axis = 2)

	image = image.astype('float32')

	convoluted = np.absolute(convolve(image, filter_x)) + np.absolute(convolve(image, filter_y))

	energy_map = convoluted.sum(axis = 2)

	return energy_map

def getMaps(image):
	rows, columns, _ = image.shape
	energy_map = getEnergy(image)

	current_map = energy_map.copy()
	goback = np.zeros_like(current_map, dtype = np.int)

	for i in range(1, rows):
		for j in range(0, columns):
			if j == 0:
				min_index = np.argmin(current_map[i - 1, j : j + 2])
				goback[i, j] = min_index + j
				min_energy = current_map[i - 1, min_index + j]

			else:
				min_index = np.argmin(current_map[i - 1, j - 1 : j + 2])
				goback[i, j] = min_index + j -1
				min_energy = current_map[i - 1, min_index + j - 1]

			current_map[i, j] += min_energy

	return current_map, goback

def drawSeam(image):

	rows, columns, _ = image.shape
	cMap, goback = getMaps(image)

	mask = np.ones((rows, columns), dtype = np.bool)

	j = np.argmin(cMap[-1])

	for i in reversed(range(rows)):
		mask[i, j] = False
		j = goback[i, j]

	mask = np.logical_not(mask)
	image[...,0][mask] = 0 
	image[...,1][mask] = 0
	image[...,2][mask] = 255

	return image

def carve(image):

	rows, columns, _ = image.shape
	cMap, goback = getMaps(image)

	mask = np.ones((rows, columns), dtype = np.bool)

	j = np.argmin(cMap[-1])

	for i in reversed(range(rows)):
		mask[i, j] = False
		j = goback[i, j]

	mask = np.stack([mask] * 3, axis = 2)
	image = image[mask].reshape((rows, columns - 1, 3))
	
	return image

def cropByColumn(image, display_seams, generate = 0, lsit = None, scale_c = 0.5, fromRow = 0):

	rows, columns, _ = image.shape

	newcolumns = int(columns * scale_c)
	crop = image.copy()

	if fromRow == 1:
		_path = 'row-wise'
	else:
		_path = 'col-wise'

	if display_seams == 0:
		a = 0
		gc = 0
		cF(os.getcwd() + str('\\sequences\\' + lsit[0] + '\\' + _path + '\\cropseq\\'))
		for i in trange(columns - newcolumns):
			if generate == 1:
				crop = carve(crop)
				if i % 5 == 0:
					if fromRow == 1:
						_rotate = crop.copy()
						_rotate = np.rot90(_rotate, 3, (0, 1))
						wIG(_rotate, str(gc)+'. cropped_'+str(i), lsit[1], lsit[0], a, _path)
						gc += 1
					else:
						wIG(crop, str(gc)+'. cropped_'+str(i), lsit[1], lsit[0], a)
						gc += 1
				else:
					pass
			else:
				crop = carve(crop)

		return crop

	else:
		a = 0
		b = 1
		gc_img = 0
		gc_crop = 0
		cF(os.getcwd() + str('\\sequences\\' + lsit[0] + '\\' + _path + '\\cropseq\\'))
		cF(os.getcwd() + str('\\sequences\\' + lsit[0] + '\\' + _path + '\\seamseq\\'))
		for i in trange(columns - newcolumns):
			if generate == 1:
				#give me a way to parallelize this portion of code :|
				image = drawSeam(image) 
				crop = carve(crop)
				if i % 5 == 0:	
					if fromRow == 1:
						_rotate1 = image.copy()
						_rotate2 = crop.copy()
						_rotate1 = np.rot90(_rotate1, 3, (0, 1))
						_rotate2 = np.rot90(_rotate2, 3, (0, 1))
						wIG(_rotate1, str(gc_img)+'. seamed_'+str(i), lsit[1], lsit[0], b, _path)
						wIG(_rotate2, str(gc_crop)+'. cropped_'+str(i), lsit[1], lsit[0], a, _path)
						gc_img += 1
						gc_crop += 1
					else:
						wIG(image,str(gc_img)+'. seamed_'+str(i), lsit[1], lsit[0], b)
						wIG(crop,str(gc_crop)+'. cropped_'+str(i), lsit[1], lsit[0], a)
						gc_img += 1
						gc_crop += 1
				else:
					pass
			else:
				image = drawSeam(image) 
				crop = carve(crop)
				
		return image, crop

def cropByRow(image, display_seams, generate = 0, lsit = None, scale_r = 0.5):

	fromRow = 1
	image = np.rot90(image, 1, (0, 1))
	seam_image, crop_image = cropByColumn(image, display_seams, generate, lsit, scale_r, fromRow)
	crop_image = np.rot90(crop_image, 3, (0, 1))
	seam_image = np.rot90(seam_image, 3, (0, 1))

	return seam_image, crop_image
