'''import cv2

desired_size = 368
im_pth = "/home/jdhao/test.jpg"

im = cv2.imread(im_pth)
old_size = im.shape[:2] # old_size is in (height, width) format

ratio = float(desired_size)/max(old_size)
new_size = tuple([int(x*ratio) for x in old_size])

# new_size should be in (width, height) format

im = cv2.resize(im, (new_size[1], new_size[0]))

delta_w = desired_size - new_size[1]
delta_h = desired_size - new_size[0]
top, bottom = delta_h//2, delta_h-(delta_h//2)
left, right = delta_w//2, delta_w-(delta_w//2)

color = [0, 0, 0]
new_im = cv2.copyMakeBorder(im, top, bottom, left, right, cv2.BORDER_CONSTANT,
    value=color)

cv2.imshow("image", new_im)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''

from natsort import natsorted
import os
import cv2

img_path_test = 'images/fig4.png'
_mage = cv2.imread(img_path_test)
print(_mage.shape)
height = _mage.shape[0]
width = _mage.shape[1]

dir_path = 'sequences/fig4/col-wise/seamseq/'
ext = '.png'
output = 'video.avi'

shape = 640, 540
fps = 3

images = [f for f in os.listdir(dir_path) if f.endswith(ext)]
images = natsorted(images)
print(images[0])

fourcc = cv2.VideoWriter_fourcc(*'DIVX')
video = cv2.VideoWriter(output, fourcc, fps, shape)

for image in images:
    image_path = os.path.join(dir_path, image)
    image = cv2.imread(image_path)
    resized=cv2.resize(image,shape) 
    video.write(resized)

video.release()