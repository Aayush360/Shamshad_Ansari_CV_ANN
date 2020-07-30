# image subtraction:

# two image must be of same size and depth
# for detecting any change/alternation in an image
# level any uneven sections or shadows in an image


from __future__ import print_function
import cv2
import numpy as np


image1path = '../images/cat1.jpeg'
image2path ='../images/cat1.jpeg'

image1 = cv2.imread(image1path)
image2 = cv2.imread(image2path)

# resize the image to make them of the same dimension. this is a must to subtract two images

resizedImage1 = cv2.resize(image1, (int(500*image1.shape[1]/image1.shape[0]),500), interpolation=cv2.INTER_AREA)
resizedImage2 = cv2.resize(image2, (int(500*image2.shape[1]/image2.shape[0]),500), interpolation=cv2.INTER_AREA)

cv2.imshow("resized1", resizedImage1)
cv2.imshow("resized2", resizedImage2)


# subtract image 1 from 2
subImage= cv2.subtract(resizedImage2, resizedImage1)
cv2.imshow("diff 1 from 2",subImage )
cv2.waitKey(0)

# subtract image 2 from 1

cv2.imshow("diff 2 from 1", cv2.subtract(resizedImage1,resizedImage2))
cv2.waitKey(0)

# numpy image subtraction

subtractedImage = resizedImage1-resizedImage2
cv2.imshow("numpy subtracts image", subtractedImage)
cv2.waitKey(0)

# a constant subtraction

sub_const = resizedImage1-50
cv2.imshow("constant subtracted from the image", sub_const)
cv2.waitKey(0)
