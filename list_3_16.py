# Binarization using Simple Thresholding

import cv2
import numpy as np


# load the image

image = cv2.imread('../images/note.png')
cv2.imshow('Original image', image)

# convert the image to grayscale

image_gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow('original grayscale image', image_gray)

# Binarize the image using thresholding

(T, binarizedImage) = cv2.threshold(image_gray,60,255,cv2.THRESH_BINARY)
cv2.imshow("Binarized image", binarizedImage)

# binarization with inverse thresholding

(T, inverseBinarizedImage) = cv2.threshold(image_gray,60,255, cv2.THRESH_BINARY_INV)
cv2.imshow("Inverse Binary thresholding", inverseBinarizedImage)

cv2.waitKey(0)

