"""Bitwise operations:

# for grayscale binary image, the pixel value 0 means off and all value greater than 0 means on

# bitwise AND operations of two image array calculates element-wise conjunction or array and scalar

# bitwise OR operation perform element-wise disjunction of two array or between array and scalar

# bitwise NOT inverts the bit value of an operand

# XOR returns 1 if either but not both operands are 1 else returns 0

"""


import cv2
import numpy as np

# create a circle

circle = cv2.circle(np.zeros((200,200,3), dtype='uint8'),(100,100),90,(255,255,255),-1)
cv2.imshow("A white circle", circle)
cv2.waitKey(0)


# create a square

square = cv2.rectangle(np.zeros((200,200,3), dtype='uint8'),(30,30),(170,170),(255,255,255),-1)
cv2.imshow("A white square", square)
cv2.waitKey(0)

# bitwise AND

bitwiseAnd = cv2.bitwise_and(square,circle)
cv2.imshow("AND operation", bitwiseAnd)
cv2.waitKey(0)

# bitwise OR

bitwiseOr = cv2.bitwise_or(square,circle)
cv2.imshow("OR opearation", bitwiseOr)
cv2.waitKey(0)

# bitwise XOR

bitwiseXor = cv2.bitwise_xor(square,circle)
cv2.imshow("XOR operation", bitwiseXor)
cv2.waitKey(0)

# bitwise NOT

bitwiseNot = cv2.bitwise_not(square,circle)
cv2.imshow("NOT operation", bitwiseNot)
cv2.waitKey(0)

