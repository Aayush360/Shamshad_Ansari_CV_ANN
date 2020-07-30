# calculation of image statistics from GLCM

import cv2
import numpy as np
import skimage.feature as sk


# read the image and convert it to grayscale

image = cv2.imread('../images/nature.jpg')
image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

cv2.imshow("original grayscale image", image)

# get the GLCM

glcm = sk.greycomatrix(image,[2],[0,np.pi/2])

# calculate contrast

contrast = sk.greycoprops(glcm, prop='contrast')
print("Contrast is: ", contrast)

# calculate dissimilarity

dissimilarity = sk.greycoprops(glcm, prop="dissimilarity")
print(" dissimilarity is", dissimilarity)

# calculate homogeneity

homogeinity = sk.greycoprops(glcm, prop="homogeneity")
print(" homogeneity is: ", homogeinity)

# calcualte ASM

ASM = sk.greycoprops(glcm, prop = 'ASM')
print("ASM is: ",ASM)

# calculate energy

energy = sk.greycoprops(glcm, prop="energy")
print("energy is: ", energy)

# calculate correlation

correlation = sk.greycoprops(glcm, prop="correlation")
print("correlation is: ", correlation)