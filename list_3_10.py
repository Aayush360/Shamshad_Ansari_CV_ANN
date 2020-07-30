# splitting and merging channels

# these techniques are useful to perform feature engineering


import cv2
import numpy as np

# load the image

nature = cv2.imread('../images/nature.jpg')

# split the images into component color

(b,g,r) = cv2.split(nature)

# show the blur image
cv2.imshow("blue image", b)
cv2.waitKey(0)


# show the green image
cv2.imshow("green image", g)
cv2.waitKey(0)


# show the red image
cv2.imshow("red image",r)

cv2.waitKey(0)

# merging the splitted components

merged = cv2.merge([b,g,r])
cv2.imshow("merged image", merged)
cv2.waitKey(0)
