# drawing a cricle on a blank canvas

from __future__ import print_function
import cv2
import numpy as np

# create a new canvas

canvas = np.zeros((200,200,3), dtype='uint8')
center =(100,100)
radius1 =50
radius2 = 100
color1 = (0,0,255)
color2 =(255,0,0)
thickness = 5

cv2.circle(canvas,center,radius1,color1,thickness)
cv2.circle(canvas,center, radius2,color2,thickness)
cv2.imwrite("circle.jpg", canvas)
cv2.imshow("Circle", canvas)
cv2.waitKey(0)