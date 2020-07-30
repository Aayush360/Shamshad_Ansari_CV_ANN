# Cropping:
# removing the unwanted outer area of an image
# it is achieved by slicing the numpy array
# no special function to perform the cropping


from __future__ import print_function
import cv2
import numpy as np


# load the image

image_path = '../images/Lenna.png'
image = cv2.imread(image_path)

# original image
cv2.imshow("original image", image)
cv2.waitKey(0)

# cropped image

cropped_image = image[250:350, 250:380]
cv2.imshow("cropped image", cropped_image)
cv2.waitKey(0)