import numpy as numpy
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('tree.jpg', 0)
cv2.namedWindow('tree in grayscale', cv2.WINDOW_NORMAL)
cv2.imshow('tree in grayscale', img)
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
# plt.xticks(['x']), plt.yticks([]) # to get rid of ticks
plt.show()
k = cv2.waitKey(0)
if k == 27:
	cv2.destroyAllWindows()
elif k == ord('s'):
	cv2.imwrite('savedimage.png', img)
	cv2.destroyAllWindows()
