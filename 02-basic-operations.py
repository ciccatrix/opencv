import cv2
import numpy as np 

img = cv2.imread('tree.jpg')
px = img[100,100] # blue green red 0 1 2
print px

img[100,100] = 100 # don't do this
cv2.imshow('image',img)

cv2.waitKey(0)
cv2.destroyAllWindows()

orig = img.item(10, 10, 2)
img.itemset((10, 10, 2), 100)
chng = img.item(10, 10, 2)
print orig
print chng

print img.shape # rows, columns, # channels. if grayscale only returns rows and columns 

print img.size # number of pixels

print img.dtype # datatype

cut = img[100:200, 900:1000]
img[300:400, 900:1000] = cut
cv2.imshow('image',img)

cv2.waitKey(0)
cv2.destroyAllWindows()


