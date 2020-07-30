# Ostu's  Binarization:

# automatically determines optimal global threshold from the image histogram

import cv2
import numpy as np

# load the image

image = cv2.imread('../images/note.png')

# convert it to grayscale

image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('Grayscale image', image_gray)

# binarize the image using thresholding

(T, binarizedImage) = cv2.threshold(image_gray,0,255,cv2.THRESH_BINARY+ cv2.THRESH_OTSU)
print(" threshold value with ostu binaraization", T)
cv2.imshow(" binarized image", binarizedImage)

# Binarization with inverse thresholding

(Ti, inverseBinaryImage) = cv2.threshold(image_gray,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
print(" threshold value with ostu inverse binarization", Ti)
cv2.imshow("inverse binarized image", inverseBinaryImage)
cv2.waitKey(0)