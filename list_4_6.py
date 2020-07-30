# HOG calculation


import cv2
import numpy as np
import skimage.feature as sk

# load the image

image = cv2.imread('../images/Lenna.png')
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# resize the image

image = cv2.resize(image, (int(image.shape[0]/5), int(image.shape[1]/5)))

# HOG calculation

(HOG, hogImage) = sk.hog(image,orientations=9, pixels_per_cell=(8,8), cells_per_block=(2,2),
                         visualize=True, transform_sqrt=True,
                         block_norm='L2-Hys', feature_vector=True)


print("Image dimension", image.shape)
print("Feature Vector Dimension", HOG.shape)

# showing the original and HOG image

cv2.imshow("Original image", image)
cv2.imshow("HOG image", hogImage)

cv2.waitKey(0)