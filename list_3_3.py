# rotation: image rotation around the center of the image

from __future__ import print_function
import cv2
import numpy as np


# load the image

image_path ='../images/test.jpg'
image = cv2.imread(image_path)
(h,w)= image.shape[:2]

# define the translation matrix

center = (h//2, w//2) # divide the height and width to get the integer part
angle = -45
scale = 1.0 # keep the original size of the image after rotation

# rotate the image around the center by 45-degree angle (clockwise)

rotation_matrix = cv2.getRotationMatrix2D(center,angle,scale)

# rotate the image

rotated_image = cv2.warpAffine(image,rotation_matrix,(image.shape[1], image.shape[0]))
cv2.imshow("Rotated Image", rotated_image)
cv2.waitKey(0)