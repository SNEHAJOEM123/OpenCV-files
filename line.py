import cv2 as cv
import numpy as np

blank=np.zeros((500,500,3),dtype='uint8')
cv.line(blank,(100,250),(300,400),(255,255,255),thickness=3)
cv.imshow('Line',blank)
cv.waitKey(0)

