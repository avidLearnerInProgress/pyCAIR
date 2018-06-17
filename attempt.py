import sys
import cv2
import numpy as np
from scipy.ndimage.filters import convolve
from tqdm import trange
import matplotlib


def logSeperate(x):
	print(x)

def calculateEnergy(img):
    image = cv2.cvtColor(img.astype(np.uint8), cv2.COLOR_BGR2GRAY)
    #cv2.imwrite("gray.png", image)
    cv2.imshow("gray", image)
    cv2.waitKey(0)
    dx = cv2.Sobel(image, cv2.CV_16S, 1, 0, ksize=3)
    abs_x = cv2.convertScaleAbs(dx)
    dy = cv2.Sobel(image, cv2.CV_16S, 0, 1, ksize=3)
    abs_y = cv2.convertScaleAbs(dy)
    output = cv2.addWeighted(abs_x, 0.5, abs_y, 0.5, 0)
    cv2.imshow("energy", output.astype(np.uint8))
    cv2.waitKey(0)
    return output

def _calculateEnergy(img):

	dx = np.array([ [1.0, 2.0, 1.0],
					[0.0, 0.0, 0.0],
					[-1.0, -2.0, -1.0]
				 ])

	dy = np.array([ [1.0, 0.0, -1.0],
					[2.0, 0.0, -2.0],
					[1.0, 0.0, -1.0]
		         ])

	filter_dx = np.stack([dx]*3, axis = 2)
	filter_dy = np.stack([dy]*3, axis = 2)

	'''print("dx"+ str(filter_dx))
	print("\n")
	print("dy"+ str(filter_dy))
	'''

	img = img.astype('float32')
	_conv = np.absolute(convolve(img, filter_dx)) + np.absolute(convolve(img, filter_dy))
	#print(_conv)
	energy_map = _conv.sum(axis = 2)
	#print(energy_map)
	return energy_map

def generateAxisMap(energy):
	energy = np.int_(energy)
	(rows, columns) = energy.shape[:2]
	axis_map = np.zeros((rows, columns))

	for col in range(columns):
		axis_map[0][col] = energy[0][col]

	for row in range(1, rows):
		for col in range(columns):
			if col == 0:
				axis_map[row][col] = energy[row][col] + min(energy[row-1][col], energy[row-1][col+1])

			elif col == columns-1:
				axis_map[row][col] = energy[row][col] + min(energy[row-1][col], energy[row-1][col-1])

			else:
				axis_map[row][col] = energy[row][col] + min(energy[row-1][col-1], energy[row-1][col], energy[row-1][col+1])

	return axis_map


def calculateSeams(value_map):

	(rows, columns) = value_map.shape[:2]
	axis_map = np.int_(value_map)

	print(rows)
	print(columns)

	logSeperate("#--Seperator--#\n")
	print("ValueMap:")
	print(value_map[-1])

	seam = np.zeros(rows) #matrix of zeros
	current_active_column = np.argmin(value_map[-1]) #find index of minimum value from last column of axis map
	
	seam_cost = 0
	seam[-1] = current_active_column #copy index of active index into last cell of seam matrix
	
	logSeperate("#--Seperator--#\n")
	print("Seam:")
	print(seam)

	#print(value_map[rows-1][current_active_column])

	seam_cost += value_map[rows-1][current_active_column] #gets the minimum value from its index

	logSeperate("#--Seperator--#\n")
	print("Initial Seam Cost:")
	print(seam_cost)

	for row in range(rows-2, -1, -1): #traversing in reverse direction x, x-1, x-2 ..
		print(seam[row+1]) #
		print(seam[row])
		if seam[row+1] == 0:
			min_values = (value_map[row][current_active_column], value_map[row][current_active_column+1])
			seam[row] = np.argmin(min_values)
			current_active_column = np.argmin(min_values)
			



def main():
	ip = cv2.imread("castle_big.png")
	#ene = calculateEnergyFast(ip)
	new_img = ip
	#ene = calculateEnergy(ip)

	#for pixel in range(10):
	image_energy = calculateEnergy(new_img)
	axis_map = generateAxisMap(image_energy)
	calculateSeams(axis_map)


if __name__ == '__main__':
	main()

