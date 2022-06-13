import cv2
import numpy as np
print (cv2.__version__)
dispW=320
dispH=240
flip = 2
img1=np.zeros((320,240,1), np.uint8)
img1[0:200,0:120]=[255]

img2=np.zeros((320,240,1),np.uint8)
img2[20:300,20:220]=[255]

bitand=cv2.bitwise_and(img1,img2)

camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cam=cv2.VideoCapture(camSet)
#cam=cv2.VideoCapture(0)
print(f'this is the result {cam.read()}')
while True:
    ret , frame = cam.read()
    cv2.imshow('picam',frame)
    cv2.imshow('Image1',img1)
    cv2.moveWindow('Image1',400,0)
    cv2.imshow('Image2',img2)
    cv2.moveWindow('Image2',600,0)
    cv2.imshow('and',bitand)
    cv2.moveWindow('and',0,250)
    cv2.moveWindow('picam',0,0)
    if cv2.waitKey(1)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()
