import cv2 as cv
import numpy as np

img=np.zeros((1500,1600,3),dtype='uint8')
img.fill(255)

cv.ellipse(img,(120,100),(50,80),-180,0,360,(0,0,255),thickness=-1)
cv.ellipse(img,(100,400),(50,80),-180,0,360,(255,0,255),thickness=-1)
cv.ellipse(img,(400,300),(50,80),-180,0,360,(0,255,255),thickness=-1)
cv.ellipse(img,(600,300),(50,80),-180,0,360,(0,255,0),thickness=-1)
cv.imshow('Background',img)
cv.waitKey(0)