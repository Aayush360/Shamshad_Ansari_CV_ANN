# masking: hiding or filtering of and image

# we put focus on certain portion of the image while applying mask on the remaining portion


# masking using Bitwise AND operation

import cv2
import numpy as np

# load an image

nature = cv2.imread('../images/nature.jpg')
cv2.imshow("original nature image", nature)

# create a rectangular mask

maskImage = cv2.rectangle(np.zeros(nature.shape[:2],dtype='uint8'),(50,50),(int(nature.shape[1])-50,
                                                                                (int(nature.shape[0]/2)-50)),
                                                                            (255,255,255),-1)
cv2.imshow("mask image", maskImage)
cv2.waitKey(0)

# using bitwise and operaion to perfrom masking

masked = cv2.bitwise_and(nature,nature,mask=maskImage)
cv2.imshow("masked image", masked)
cv2.waitKey(0)

