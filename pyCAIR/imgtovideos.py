from natsort import natsorted
import os,cv2
from pathlib import Path

from pyCAIR.helpers import createFolder as cF

def vid(path):

	dir_path = path
	ext1, ext2 = '.png', '.jpg'
	opath = str(Path(__file__).resolve().parents[0]) + '\\videos'
	cF(opath)	
	a, b = dir_path.rsplit('\\', 1)[0], dir_path.rsplit('\\', 1)[1]
	c, d = a.rsplit('\\', 1)[0], a.rsplit('\\', 1)[1]
	_, f = c.rsplit('\\', 1)[0], c.rsplit('\\', 1)[1]
	vid_name = f + '_' + d + '_' + b + '.avi'
	print(vid_name)
	op = os.path.join(opath, vid_name)

	#exit()
	shape = 640, 540
	fps = 5

	#images = [f for f in os.listdir(dir_path) if f.endswith(ext)]
	images = []
	for f in os.listdir(dir_path):
		if f.endswith(ext1) or f.endswith(ext2):
			images.append(f)

	images = natsorted(images)
	print(images[0])

	fourcc = cv2.VideoWriter_fourcc(*'DIVX')
	video = cv2.VideoWriter(op, fourcc, fps, shape)

	for image in images:
	    image_path = os.path.join(dir_path, image)
	    image = cv2.imread(image_path)
	    resized=cv2.resize(image,shape) 
	    video.write(resized)
	video.release()

def getToProcessPaths(directory):
	
	all_subdirs = [x[0] for x in os.walk(directory)]
	get = []
	for i in range(len(all_subdirs)):
		if all_subdirs[i].endswith('cropseq') or all_subdirs[i].endswith('seamseq'):
			if all_subdirs[i] not in get:
				get.append(all_subdirs[i])

	return get

def generateVideo():
	base_path = str(Path(__file__).resolve().parents[0])
	base_path += "\sequences\\"
	allpaths = getToProcessPaths(base_path)

	for i in range(len(allpaths)):
		cpath = allpaths[i]
		vid(cpath)