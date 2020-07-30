# Image Translation: moving image left, right, up, down along x and y axis
#

from __future__ import print_function
import cv2
import numpy as np

# load and read the image

image_path = '../images/test.jpg'
image = cv2.imread(image_path)

# define the translatin Matrix

translation_mat = np.float32([[1,0,-50],[0,1,-30]])

# move the image

moved_image = cv2.warpAffine(image,translation_mat,(image.shape[1], image.shape[0]))

# width and height of the canvas within which we want to move our image
# here we are keeping the size of the canvas the same as the original width and height of the image
cv2.imshow('moved image', moved_image)
cv2.waitKey(0)