# LBP image and histogram calculation and comparision with original image

import cv2
import numpy as np
import skimage.feature as sk
import matplotlib.pyplot as plt


# load the image from the disk, resize it and convert it to grayscale

image = cv2.imread('../images/Lenna.png')
image = cv2.resize(image, (int(image.shape[0]/5), int(image.shape[1]/5)))
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# calculate the histogram of the original image and plot it

originalHist = cv2.calcHist(image,[0],None, [256],[0,256])
plt.figure()
plt.title("Histogram of the original image")
plt.plot(originalHist, color='r')


# calculate the LBP image and histogram over the LBP, then plot the histogram

radius = 3
points = 3*8

# LBP calculation

lbp = sk.local_binary_pattern(image, points, radius, method='default')
lbphist, _= np.histogram(lbp, density=True, bins=256, range=(0,256))

# output format of local_binary_pattern is different and not supported by calcHist Function
# of cv2 so we are using numpy's histogram function

plt.figure()
plt.title(" Histogram of the LBP image")
plt.plot(lbphist, color='g')
plt.show()

# print(type(lbp)) # both are of numpy ndarray type
# print(type(image))

# showing the original and LBP image

cv2.imshow("original image",image)
cv2.imshow("LBP image", lbp)
cv2.waitKey(0)