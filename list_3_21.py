# Canny Edge Detection

import numpy as np
import cv2

# load the image

image = cv2.imread('../images/sudoku.jpg')
cv2.imshow("original image", image)

# convert to grayscale
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# apply the canny function

canny = cv2.Canny(image_gray,50,170)
cv2.imshow("Canny Edges", canny)
cv2.waitKey(0)