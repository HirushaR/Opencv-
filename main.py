import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

#read the image and convert to grayscale
img = cv.imread('watch.jpg', cv.IMREAD_GRAYSCALE)
#cv.IMREAD_GRAYSCALE = 0
#cv.IMREAD_COLOR = 1
#cv.IMREAD_UNCHANGED = -1

#show the image
# cv.imshow('image',img)
# cv.waitKey(0)
# cv.destroyAllWindows()

plt.imshow(img, cmap='gray', interpolation='bicubic')
plt.plot([50, 100], [100, 100], 'c', linewidth=5)
plt.show()

