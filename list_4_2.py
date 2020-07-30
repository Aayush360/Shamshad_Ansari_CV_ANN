# color histogram of 3 channels (rgb)

import cv2
import numpy as np
import matplotlib.pyplot as plt

# read the image

image = cv2.imread('../images/Lenna.png')
cv2.imshow("original image", image)

# opencv stores the color in bgr color sequence

colors = ("blue","green","red")

# creating mask to pass in as an argument

maskImage = cv2.rectangle(np.zeros(image.shape[:2],dtype='uint8'),(50,50),(int(image.shape[1])-50,
                                                                                (int(image.shape[0]/2)-50)),
                                                                            (255,255,255),-1)
# calculate histogram

for i, color in enumerate(colors):
    hist = cv2.calcHist([image],[i],maskImage,[32],[0,256])
    # plot histogram graph
    plt.plot(hist, color=color)

plt.title("RGB color Histogram")
plt.plot("bins")
plt.ylabel("Number of pixels")
plt.show()

cv2.waitKey(0)




