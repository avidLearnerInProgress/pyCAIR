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

def user_input(alignment, scale , display_seam, image, generate):
	'''parser = argparse.ArgumentParser()
	parser.add_argument('-a',
						type = int,
						help = "Alignment of Seam (Vertical/Horizontal/Both) : (0/1/2)",
						required = True)

	parser.add_argument('-s',
						type = float,
						help = "Scale aspect ratio between 0 and 1",
						default = 0.5,
						required = False)

	parser.add_argument('-d',
						type = int,
						help = "Display Seams or not : (1/0)",
						required = True)

	parser.add_argument('-i',
						type = str,
						help = "Path to source image",
						required = True)

	parser.add_argument('-g',
						type = int,
						help = "Generate sequences of image or not : (1/0)",
						required = False)

	argsip = parser.parse_args()
	'''
	argsip = []
	argsip.append(alignment)
	argsip.append(scale)
	argsip.append(display_seam)
	argsip.append(image)
	argsip.append(generate)
	main(argsip)