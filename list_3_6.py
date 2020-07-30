# image arithmetic and bitwise operations:

# when building cv_applications, we need to enhance the properties of the input image

# addition operation:

from __future__ import print_function
import numpy as np
import cv2


image1path = '../images/zebra.png'
image2path = '../images/nature.jpg'

image1 = cv2.imread(image1path)
image2 = cv2.imread(image2path)

# resize the image to make them of the same dimension. this is must while adding two images

resizedImage1 = cv2.resize(image1,(300,300), interpolation=cv2.INTER_AREA)
resizedImage2 = cv2.resize(image2,(300,300), interpolation=cv2.INTER_AREA)

# this is a simple addition of two images

resultant = cv2.add(resizedImage1,resizedImage2)

# Display the images to see the difference

cv2.imshow('Resized 1', resizedImage1)
cv2.waitKey(0)

cv2.imshow('Resized 2', resizedImage2)
cv2.waitKey(0)

cv2.imshow('resultant ', resultant)
cv2.waitKey(0)

# this is the weighted addition of two images

weightedImage = cv2.addWeighted(resizedImage1,0.7, resizedImage2,0.3,0)
cv2.imshow("weighted image 1", weightedImage)
cv2.waitKey(0)

weightedImage = cv2.addWeighted(resizedImage1,0.7, resizedImage2,0.3,1)
cv2.imshow("weighted image 2", weightedImage)
cv2.waitKey(0)

imageEnhanced = 255*resizedImage1
cv2.imshow("Enhanced image",imageEnhanced)
cv2.waitKey(0)

arrayImage = resizedImage1+resizedImage2
cv2.imshow("Array Image", arrayImage)
cv2.waitKey(0)

