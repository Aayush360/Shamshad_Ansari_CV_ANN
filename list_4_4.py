# GLCM calculation using graycomatrix() functions

import cv2
import numpy as np
import skimage.feature as sk



# read the image and convert it to grayscale

image = cv2.imread('../images/nature.jpg')
image =cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

cv2.imshow("grayscale image ", image)

# calculate the GLCM of the grayscale matrix

glcm = sk.greycomatrix(image,[2],[0,np.pi/2])
print(glcm)


