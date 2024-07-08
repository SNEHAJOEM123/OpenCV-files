import cv2 as cv

#reading images
img=cv.imread('photos/cat.jpg')
cv.imshow('Cat',img)
cv.waitKey(0)

#reading videos 
capture=cv.VideoCapture('Videos/dog.mp4')
while True:
    isTrue, frame =capture.read() #to capture the video frame by frame
    cv.imshow('Video',frame) #displays each frame using cv.imshow method
    if cv.waitKey(20) and 0xFF==ord('d'): #for breaking out of while loop
        break
capture.release()
cv.destroyAllWindows()        