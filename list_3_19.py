# Sobel and Schar Gradient Detection

import cv2
import numpy as np

# load the image

image = cv2.imread('../images/sudoku.jpg')
cv2.imshow("original image", image)

image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image= cv2.bilateralFilter(image,3,50,50)
cv2.imshow("Blurred Image", image)

# Sobel Gradient Detection

sobelx = cv2.Sobel(image,cv2.CV_64F,1,0,ksize=3)
sobelx = np.uint8(np.absolute(sobelx))
sobely = cv2.Sobel(image,cv2.CV_64F, 0,1,ksize=3)
sobely = np.uint8(np.absolute(sobely))

cv2.imshow("Sobel X", sobelx)
cv2.imshow("Sobel Y", sobely)

# Schar Gradient Detection by passing ksize=-1 in Sobel function
Scharx = cv2.Sobel(image,cv2.CV_64F,1,0,ksize=-1)
Scharx = np.uint8(np.absolute(Scharx))
Schary = cv2.Sobel(image,cv2.CV_64F, 0,1, ksize=-1)
Schary = np.uint8(np.absolute(Schary))


cv2.imshow("Schar X", Scharx)
cv2.imshow("Schar Y", Schary)
cv2.waitKey(0)

