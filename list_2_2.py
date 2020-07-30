# Description:

# access and manipulate image pixels

from __future__ import print_function
import cv2

# image path
image_path = '../images/test.jpg'

# read or load image from its path
image = cv2.imread(image_path)

# access pixel at (0,0) location

(b,g,r) = image[0][0]

print('Blue, Green and Red value at 0,0 is', format((b,g,r)))

# manipulate pixel and show modified image

image[:100,:100] = (255,255,0)
cv2.imshow('Modified image', image)
cv2.waitKey(0)