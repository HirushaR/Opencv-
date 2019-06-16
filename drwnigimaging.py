import numpy as np
import cv2 as cv

img = cv.imread('watch.jpg', cv.IMREAD_COLOR)
cv.line(img, (0, 0), (150, 150), (255, 255, 255), 15)#bgr draw a line
cv.rectangle(img, (15,25) , (200,150), (0,255,0), 5)#draw a reqtangle
cv.circle(img, (100,63), 55 ,(0,0,255) ,1)#circle

pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
#pts = pts.reshape((-1,1,2))
cv.polylines(img, [pts], True, (0, 255, 255), 3)

#write
font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img, 'openCV Tute!',(0,130),font,1,(200,255,255),2,cv.LINE_AA)

cv.imshow('image',img)
cv.waitKey()
cv.destroyAllWindows()