# Contour Detection and Drawing

import cv2
import numpy as np

# load image

image =cv2.imread('../images/sudoku.jpg')
cv2.imshow("original image", image)

# step 1: convert to grayscale
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("grayscale image", image)

# step2: binarize the image

(T, binarized) = cv2.threshold(image,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU )
cv2.imshow("binarized image", binarized)


# Canny function for edge detection

canny = cv2.Canny(binarized,0,255)
cv2.imshow("canny image", canny)

(contours, hierarchy) = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
print(" number of contours determined are ", format(len(contours)))

# type of contour we are interested in :

# RETR_EXTERNAL : to retrieve outermost contours
# RETR_LIST:  to retrieve all contours
# RETR_TREE, RETR_COMP : to retrive hierarchical contours

# CHAIN_APPROX_SIMPLE: removes redundant points and compresses the contours thereby saving memory
# CHAIN_APPROX_NONE: stores all points of the contours

# contours: list of all contours in the image, each contour is a numpy array of (x,y) coordinates of
# boundary points of the objects


copiedImage = image.copy()

cv2.drawContours(copiedImage,contours,-1 , (0,255,0),2)

# -1 of we want to draw all contours, 0 if we want to draw first contour from the list
cv2.imshow("contours", copiedImage)
cv2.waitKey(0)