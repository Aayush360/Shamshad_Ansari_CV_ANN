# flipping the image horizontally along the x-axis and vertically along the y-axis

# value: -1 first flip horizontally then vertically

from __future__ import print_function
import cv2
import numpy as np


# load the image

image_path = '../images/Lenna.png'
image = cv2.imread(image_path)

# flip horizontally

flipped_horizontally = cv2.flip(image,1)
cv2.imshow("flipped horizontally", flipped_horizontally)
cv2.waitKey(-1)

# flipped_vertically

flipped_vertically = cv2.flip(image,0)
cv2.imshow("flipped vertically", flipped_vertically)
cv2.waitKey(-1)

# flip horizontally and then vertically

flippedHV = cv2.flip(image, -1)
cv2.imshow(" flipped horizontally and then vertically", flippedHV)
cv2.waitKey(-1)