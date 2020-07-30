# smoothing using Gaussian Techniques

import cv2
import numpy as np


# load the image

image = cv2.imread('../images/nature.jpg')
cv2.imshow("original image", image)

# gaussian blurring using 3x3 kernel 0 for standard deviation to calculate from the kernel

GaussianFiltered = cv2.GaussianBlur(image,(3,3),0)
cv2.imshow("gaussain blurred image", GaussianFiltered)
cv2.waitKey(0)