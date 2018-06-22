import cv2
import numpy as np

from pyCAIR.helpers import writeImage as wI

def generateEnergyMap(image, file_extension, file_name):
	image = cv2.cvtColor(image.astype(np.uint8), cv2.COLOR_BGR2GRAY)
	wI(image, ['gray', file_extension, file_name])
	dx = cv2.Sobel(image, cv2.CV_16S, 1, 0, ksize=3)
	abs_x = cv2.convertScaleAbs(dx)
	dy = cv2.Sobel(image, cv2.CV_16S, 0, 1, ksize=3)
	abs_y = cv2.convertScaleAbs(dy)
	output = cv2.addWeighted(abs_x, 0.5, abs_y, 0.5, 0)
	wI(output, ['energy', file_extension, file_name])

def generateColorMap(image, file_extension, file_name):
	img = image
	gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	heatmap1_img = cv2.applyColorMap(gray_img, 3)
	heatmap2_img = cv2.applyColorMap(gray_img, 11)
	superimpose1 = cv2.addWeighted(heatmap1_img, 0.7, img, 0.3, 0)
	superimpose2 = cv2.addWeighted(heatmap2_img, 0.7, img, 0.3, 0)
	wI(superimpose1, ['colormap1', file_extension, file_name])
	wI(superimpose2, ['colormap2', file_extension, file_name])