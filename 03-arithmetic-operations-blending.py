import numpy as numpy
import cv2
from matplotlib import pyplot as plt

img1 = cv2.imread('img.jpg')
img2 = cv2.imread('img2.jpg')

img1 = img1[0:100, 0:100]
img2 = img2[0:100, 0:100]
cv2.imshow('image', img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imshow('image', img2)
cv2.waitKey(0)
cv2.destroyAllWindows()

# blend images
dst = cv2.addWeighted(img1, 0.7, img2, 0.3, 0)
cv2.imshow('image', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

