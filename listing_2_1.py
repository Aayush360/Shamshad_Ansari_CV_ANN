# Description:
# loading, exploring and showing an image


from __future__ import print_function
import cv2

# image path
image_path = '../images/test.jpg'

# read or load image from its path

image = cv2.imread(image_path)

# image is a numpy array

print('dimension of image', image.ndim)
print('image height', format(image.shape[0]))
print('image width', format(image.shape[1]))
print('number of channels', format(image.shape[2]))
print('size of the image array', image.size)
# display the image and wait until the key is pressed

cv2.imshow('my_image', image)
cv2.waitKey(0)
