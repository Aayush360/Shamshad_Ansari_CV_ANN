# Bilateral Blurring

import cv2

# load the image

image = cv2.imread('../images/nature.jpg')
cv2.imshow('original image', image)

# bilateral filtering with kernel 5

filteredImage5 = cv2.bilateralFilter(image,5,150,50)
cv2.imshow("Blurred image 5", filteredImage5)

# image pixel, kernel/ diameter, color threshold, distance from the center

# with kernel 7

filteredImage7 = cv2.bilateralFilter(image,7,160,60)
cv2.imshow("Blurred image 7", filteredImage7)
cv2.waitKey(0)