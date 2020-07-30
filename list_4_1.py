# histogram of grayscale image

import cv2
import numpy as np
import matplotlib.pyplot as plt

# read an image and convert it to grayscale

image = cv2.imread('../images/nature.jpg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow("grayscale image", image)

# calculate the histogram

hist = cv2.calcHist([image],[0],None,[32], [0,255])

# hist variable holds the calculation output

# plot the histogram graph

plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("bins")
plt.ylabel(" number of pixels")
plt.plot(hist)
plt.show()

cv2.waitKey(0)



