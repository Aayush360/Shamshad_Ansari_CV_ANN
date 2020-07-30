# code to calculate aspect ratio and resizing the image

from __future__ import print_function
import cv2
import numpy as np


# loading and reading the image

image_path = '../images/test.jpg'
image = cv2.imread(image_path)

# get the image shape which returns height, width and channels as a tuple. calculate aspect ratio

(h,w) = image.shape[:2]
aspect_ratio = w/h

# let's resize the image to decrease the height by half of the original image
# maintaining original aspect ratio 

# remember the pixels values must be integers

height = int(0.5*h)
width = int(height*aspect_ratio)
# new image dimension as a tuple

dimension = (height,width)
resized_image = cv2.resize(image,dimension,interpolation=cv2.INTER_AREA)
cv2.imshow('Resized Image', resized_image)

# Resize using x and y factors

resizedWithFactors = cv2.resize(image,None,fx=1.2,fy=1.2,interpolation=cv2.INTER_LANCZOS4)
cv2.imshow('Resized with factors', resizedWithFactors)
cv2.waitKey(0)