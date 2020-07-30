# mean filtering or averaging

# as the kernel size increases the effect of blurring increases as well

import cv2
import numpy as np

# load the image

image = cv2.imread('../images/nature.jpg')
cv2.imshow("original park image", image)

# define the kernel

kernel = (3,3)
blurred3X3 = cv2.blur(image,kernel)
cv2.imshow(" 3x3 blurred image", blurred3X3)

blurred5x5 = cv2.blur(image,(5,5))
cv2.imshow("5x5 blurred image", blurred5x5)


blurred7x7 = cv2.blur(image, (7,7))
cv2.imshow(" 7x7 blurred image", blurred7x7)

cv2.waitKey(0)