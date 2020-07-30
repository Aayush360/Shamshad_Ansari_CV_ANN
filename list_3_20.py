# Edge detection using Laplacian Derivatives

import cv2
import numpy as np

# load an image and apply Bilateral Filtering

image = cv2.imread('../images/sudoku.jpg')
cv2.imshow("original image", image)

image = cv2.bilateralFilter(image,5,50,50)
cv2.imshow("Blurred image", image)

# laplacian function for edge detection

laplace = cv2.Laplacian(image, cv2.CV_64F)
laplace = np.uint8(np.absolute(laplace))

cv2.imshow("Laplacian Edges", laplace)
cv2.waitKey(0)