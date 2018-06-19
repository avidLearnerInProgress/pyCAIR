'''
#Notes
Seam: reduce image size and thereby achieve 'content-aware resizing'
	> connected path of low energy pixels
	> optimal 8 connected path of pixels on single image from T-B or L-R
	> optimality is defined in terms of energy function
	> repeated insertion of seams changes aspect ratio of image
	> energy function: importance of pixels
	> preserve image structure: remove more low energy pixels than higher ones
	> energy functions: gradient magnitude, entrpoy, visual silency, eye-gaze movement
	> Old methods-- (Rely on traditional image resizing operations)
		>> image-retargeting: change size while keeping its features intact
		>> 2 types of image retargeting: T-D & B-T
		>> T-D employs face detectors and B-T employs visual saliency methods(large image cropped to determine the most salient region in image)
		>> image-retargetting to mobile devices: Given a collection of ROI, construct an optimal path through these regions and display them serially 
		>> eye tracking to crop images intelligently

		>> Adaptive grid based document layout system: 
			>>> maintain line of seperation between content and template
			>>> page designer constructs several templates; once content is displayed the most suitable template is used

		>> automatic, non-photorealisitic algorithm for retargetting large images to small size displays
			>>> done by decomposing image into background layer and foreground objects

		>> feature-aware wraping:
			>>> formulation of laplacian editing technique, suited to accommodate similarity constraints on parts of domain

	> main challenge: find optimal boundaries between image fragments
	> computing seams: using dp / shortest path using djikstra / graph cuts 

	> goal: remove unnoticable pizels that blend with surrounding
	> energy function: e1(I) = |d/dx(I)| + |d/dy(I)|

	> to reduce width:
		>> remove pixels with lowest energy in ascending order (but it destroys rectangular form of image)
		>> remove equal low energy pixels from each row of image (but it destroys image content)
		>> to preserve both shape and content: use auto-cropping. i.e. find window with highest energy level
	
	> internal seams: resizing operator which is less restrictive than cropping but preserves image content better than single pixel removal

	> I: nxm image
	> internal vertical seam: 
		>> s^x = {s(i)^x}^n = {(x(i), i)}^n 
		>> i = 1 such that for all i, |x(i) -  x(i-1)| <= 1
		>> x is a mapping of [1, ..., n] -> [1, ..., m]
		>> 8 connected path of pizel in image from top to bottom containing only one pixel in each row of image

	> similarly horizontal seam:
		>> s^y = {s(j)^y}^m = {(j, y(j))}^m 
		>> j = 1 such that for all j, |y(j) - y(j-1)| <= 1
		>> y is mapping of [1, ..., m] -> [1, ..., n]
	
	> given energy function e,
		>> cost of seam: E(S) = E(Is) = summation(i= 1 to n) e(I(si))
		>> optimal seam: s* = min[E(s)] = min[summation(i = 1 to n) e(I(si))]

		>> this optimal seam is possible through dp;
			>>> traverse image from second to last row of image
			>>> compute cummulative minimum energy M for all possible seams for each entry (i,j)
			>>> i.e. M(i,j) = e(i,j) + min(M(i-1, j-1) , M(i-1, j), M(i-1, j+1))
			>>> @ @ @
				  #
				where # is current i,j and @ is the options to consider for minimum
			>>> minimum value of last row in M will denote the end of minimal connected seam
			>>> backtrack from this minimum entry to find optimal seam

	> image retargeting generalises aspect ratio change.
	> image of size n x m will be retargeted to size n' x m'
	> how to order seam carving ? horizontal first ? vertical first ?
	> optimal order of seam carving using Transport map T:

		>> for each target image of size n' x m':
			>>> r = m - m' & c = n - n'
			>>> T(r,c) : minimum cost needed to obtain image of size n-r x m-c
			>>> start at T(0,0) and fill each entry via:
				-> remove horizontal seam from image : n-r x m-c + 1 OR
				-> remove vertical seam from image : n - r + 1 X m - c
				-> DP equation: T(r,c) = min((T(r-1, c)) + E(s^x(In-r-1 x m-c)), 
											 (T(r, c-1) + E(s^y(In-r X m-c-1)))

'''
import numpy as np
import sys
import cv2
from scipy.ndimage.filters import convolve
from tqdm import trange
from PIL import Image
from scipy.ndimage import rotate



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


def cropByColumn(image, display_seams, scale_c):

	rows, columns, _ = image.shape
	
	newcolumns = int(columns * scale_c)
	
	crop = image.copy()

	if display_seams == 0:
		for i in trange(columns - newcolumns):
			crop = carve(crop)
		return crop

	else:
		for i in trange(columns - newcolumns):
			#give me a way to parallelize this portion of code :|
			image = drawSeam(image) 
			crop = carve(crop)
		return image, crop


def cropByRow(image, display_seams, scale_r):

    image = np.rot90(image, 1, (0, 1))
    seam_image, crop_image = cropByColumn(image, display_seams, scale_r)
    crop_image = np.rot90(crop_image, 3, (0, 1))
    seam_image = np.rot90(seam_image, 3, (0, 1))
    
    return seam_image, crop_image


def writeImage(image, args):
	print(args[0])
	print(args[1])
	cv2.imwrite('results/' + str(args[0]) + '.' + str(args[1]), image)
	cv2.destroyAllWindows()

def getFileExtension(ip):
	front, back = ip.split('.')
	return back

def generateEnergyMap(image, file_extension):
	image = cv2.cvtColor(image.astype(np.uint8), cv2.COLOR_BGR2GRAY)
	writeImage(image, ['gray', file_extension])
	dx = cv2.Sobel(image, cv2.CV_16S, 1, 0, ksize=3)
	abs_x = cv2.convertScaleAbs(dx)
	dy = cv2.Sobel(image, cv2.CV_16S, 0, 1, ksize=3)
	abs_y = cv2.convertScaleAbs(dy)
	output = cv2.addWeighted(abs_x, 0.5, abs_y, 0.5, 0)
	writeImage(output, ['energy', file_extension])


def main():
	#usr inpt
	toggle = int(sys.argv[1])
	scale = float(sys.argv[2])
	display_seams = int(sys.argv[3])
	_in = sys.argv[4]


	image = cv2.imread(_in)
	file_extension = getFileExtension(_in)
	print(file_extension)
	generateEnergyMap(image, file_extension)

	image_ = image.copy()


	if toggle == 0:
		#cropbycol
		if display_seams == 1:
			seam_image, crop_image = cropByColumn(image, display_seams, scale)
			writeImage(seam_image, ['column_seams', file_extension])
			writeImage(crop_image, ['column_cropped', file_extension])
			
		else:
			crop_image = cropByColumn(image, display_seams, scale)
			writeImage(crop_image, ['column_cropped', file_extension])

	elif toggle == 1:
		#cropbyrow
		if display_seams == 1:
			seam_image, crop_image = cropByRow(image, display_seams, scale)
			writeImage(seam_image, ['row_seams', file_extension])
			writeImage(crop_image, ['row_cropped', file_extension])

		else:
			crop_image = cropByRow(image, display_seams, scale)
			writeImage(crop_image, ['row_cropped', file_extension])

	elif toggle == 2:
		#cropbyrow&column
		if display_seams == 1:
			seam_col, crop_col = cropByColumn(image, display_seams, scale)
			seam_row, crop_row = cropByRow(image_, display_seams, scale)

			writeImage(seam_col, ['column_seams', file_extension])
			writeImage(seam_row, ['row_seams', file_extension])
			writeImage(crop_col, ['column_cropped', file_extension])
			writeImage(crop_row, ['row_cropped', file_extension])
			
		else:

			crop_col = cropByColumn(image, display_seams, scale)
			crop_row = cropByRow(image, display_seams, scale)
			writeImage(crop_row, ['row_cropped', file_extension])
			writeImage(crop_col, ['column_cropped', file_extension])

	else:
		print('Invalid input!')
		exit()

if __name__ == '__main__':
	main()
