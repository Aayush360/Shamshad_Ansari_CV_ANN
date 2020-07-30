# Binarization using Adaptive Thresholding

import cv2
import numpy as np

# load the image and convert to grayscale

image = cv2.imread('../images/note.png')
cv2.imshow("original note", image)

image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow(" gray_scale image", image_gray)

# binarization using adaptive thresholding and simple mean

binarized = cv2.adaptiveThreshold(image_gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,7,3)
cv2.imshow(" Binarized image with simple mean", binarized)

# Binarization using adpative thresholding and Gaussian Mean
binarized = cv2.adaptiveThreshold(image_gray,255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,
                                  11,3)

# neighborhood size to consider while calculating the threshold, constant value C that will be
# subtracted from the calculate threshold
# gaussian: takes the weighted mean of the pixel surrounding it, here we consider 7x7 and 1x11
# neighbors and subract a constant c=3 from the calculated threshold value
cv2.imshow("Binarized image with Gaussian Mean", binarized)
cv2.waitKey(0)