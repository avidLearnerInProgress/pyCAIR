import os, cv2

#Local imports
from pyCAIR.imgtovideos import generateVideo as gV
from pyCAIR.helpers import getFileExtension as gFE
from pyCAIR.helpers import createFolder as cF
from pyCAIR.helpers import writeImage as wI
from pyCAIR.opencv_generators import generateEnergyMap as gEM
from pyCAIR.opencv_generators import generateColorMap as gCM
from pyCAIR.seam_carve import cropByColumn as cBC
from pyCAIR.seam_carve import cropByRow as cBR

def main(argsip):
	#usr inpt
	toggle = argsip[0]
	scale = argsip[1]
	display_seams = argsip[2]
	_in = argsip[3]
	g = argsip[4]

	image = cv2.imread(_in)
	file_extension, file_name = gFE(_in)
	#print(file_extension + " " + file_name)
	root = os.getcwd() + str('\\results\\')
	cF(root + file_name)
	gEM(image, file_extension, file_name)
	gCM(image, file_extension, file_name)
	image_ = image.copy()
	lsit = [file_name, file_extension]

	if toggle == 0:
		#cropbycol
		if display_seams == 1:
			seam_image, crop_image = cBC(image, display_seams, g, lsit, scale)
			wI(seam_image, ['column_seams', file_extension, file_name])
			wI(crop_image, ['column_cropped', file_extension, file_name])
			
		else:
			crop_image = cBC(image, display_seams, g, lsit, scale)
			wI(crop_image, ['column_cropped', file_extension, file_name])

	elif toggle == 1:
		#cropbyrow
		if display_seams == 1:
			seam_image, crop_image = cBR(image, display_seams, g, lsit, scale)
			wI(seam_image, ['row_seams', file_extension, file_name])
			wI(crop_image, ['row_cropped', file_extension, file_name])

		else:
			crop_image = cBR(image, display_seams, g, lsit, scale)
			wI(crop_image, ['row_cropped', file_extension, file_name])

	elif toggle == 2:
		#cropbyrow&column
		if display_seams == 1:
			seam_col, crop_col = cBC(image, display_seams, g, lsit, scale)
			seam_row, crop_row = cBR(image_, display_seams, g, lsit, scale)
			wI(seam_col, ['column_seams', file_extension, file_name])
			wI(seam_row, ['row_seams', file_extension, file_name])
			wI(crop_col, ['column_cropped', file_extension, file_name])
			wI(crop_row, ['row_cropped', file_extension, file_name])
			
		else:
			crop_col = cBC(image, display_seams, g, scale)
			crop_row = cBR(image, display_seams, g, scale)
			wI(crop_row, ['row_cropped', file_extension, file_name])
			wI(crop_col, ['column_cropped', file_extension, file_name])
	else:
		print('Invalid input!')
		exit()

	gV()

def user_input(alignment = 0, scale = 0.5, display_seam = 1, image = 'images/fig4.png', generate = 1):
	argsip = []
	argsip.append(alignment)
	argsip.append(scale)
	argsip.append(display_seam)
	argsip.append(image)
	argsip.append(generate)

	return len(argsip)
	#main(argsip)