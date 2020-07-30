# histogram equalization: to adjust contrast of the image


import cv2
import numpy as np
import matplotlib.pyplot as plt


# read the image and convert to grayscale

image = cv2.imread('../images/Lenna.png')
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow("original grayscale image", image)

# calculate the histogram of the original image

hist = cv2.calcHist([image],[0],None, [256],[0,255])

# plot histogram graph

plt.figure()
plt.title("Grayscale Histogram of the original image")
plt.xlabel("bins")
plt.ylabel("Number of pixels")
plt.plot(hist)
plt.show()

# equalization

equalizedImage = cv2.equalizeHist(image)
cv2.imshow("Equalized image", equalizedImage)

# plot the histogram of equalizes image

histEqualized = cv2.calcHist([equalizedImage],[0],None,[256],[0,255])

# plot the histogram

plt.title("Grayscale Histogram of Equalized image")
plt.xlabel("Bins")
plt.ylabel("Number of pixels")
plt.plot(histEqualized)
plt.show()

cv2.waitKey(0)