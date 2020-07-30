# Drawing a rectangle to an image

from __future__ import print_function
import cv2

image_path = '../images/test.jpg'
image = cv2.imread(image_path)

start = (100,70)
end = (350,100)

# set the thickness and outline

color =(0,255,0)
thickness =5

# draw a rectangle
cv2.rectangle(image,start,end,color,thickness)

# save the modified image with the rectangle drawn to it to a file on a disk

cv2.imwrite('rectangle.jpg', image)

# display the modified image

cv2.imshow('Rectangle', image)
cv2.waitKey(0)
