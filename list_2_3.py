# Drawing a line in an image
from __future__ import print_function
import cv2


# image path
image_path = '../images/test.jpg'

# read or load image from its path
image = cv2.imread(image_path)

# set start and end coordinates

start = (0,0)
end = (image.shape[1], image.shape[0])
# set the color in BGR

color = (255,0,0)
# set thickness in pixel

thickness =4

cv2.line(image,start,end,color,thickness)

# display the modified image

cv2.imshow('Modified image', image)
cv2.waitKey(0)