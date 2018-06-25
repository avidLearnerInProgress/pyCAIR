import os, cv2

def createFolder(directory):
	if not os.path.exists(directory):
		os.makedirs(directory)

def getFileExtension(ip):
	front, back = ip.split('.')
	_, name = front.split('/')
	return back, name

def writeImage(image, args):
	name = 'results/' + str(args[2]) + '/' + str(args[0]) + '.' + str(args[1])
	cv2.imwrite(name, image)
	cv2.destroyAllWindows()

def writeImageG(image, cname, extension, filename, switch, _path = 'col-wise'):
	if switch == 0:
		insert = 'cropseq'
	else:
		insert = 'seamseq'

	name = 'sequences/' + filename + '/' + _path + '/' + insert + '/' + cname + '.' + extension
	cv2.imwrite(name, image)