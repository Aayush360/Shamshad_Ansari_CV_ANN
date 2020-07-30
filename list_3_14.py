# meadian blur: to reduce salt-pepper noise

import cv2
import numpy as np


image = cv2.imread('../images/salt-pepper.png')
cv2.imshow("original noisy image", image)

# median filtering for noise reduction

blurredImage3 = cv2.medianBlur(image,3)
cv2.imshow("Blurred image 3", blurredImage3)

blurredImage5 = cv2.medianBlur(image,5)
cv2.imshow("Blurred Image 5",blurredImage5) # more effective
cv2.waitKey(0)